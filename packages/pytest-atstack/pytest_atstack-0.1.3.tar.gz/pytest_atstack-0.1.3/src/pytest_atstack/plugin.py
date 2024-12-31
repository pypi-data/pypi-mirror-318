import logging
import os
from typing import List, Literal, TypeAlias

import pytest
import requests
from urllib.parse import urljoin
from loguru import logger

Status: TypeAlias = Literal["passed", "failed", "skipped", "broken", "unkown"]


def pytest_addoption(parser):
    group = parser.getgroup("atstack")
    group.addoption(
        "--atstack",
        action="store_true",
        default=False,
        help="Send test results to atstack.",
    )


def pytest_report_header(config, start_path):
    atstack = config.getoption("atstack")
    url = os.environ.get("ATSTACK_URL")
    token = os.environ.get("ATSTACK_PROJECT_TOKEN")
    id = os.environ.get("ATSTACK_REPORT_ID")
    return "ATSTACK: {0} URL: {1} TOKEN: {2} ID: {3}".format(atstack, url, token, id)


def get_allure_markers(markers: dict, mark: pytest.Mark) -> dict:
    label_type = mark.kwargs.get("label_type")
    match label_type:
        case "owner":
            if not mark.args:
                return
            markers.setdefault("owner", mark.args[0])
        case "severity":
            if not mark.args:
                return
            severity = getattr(mark.args[0], "value", None)
            markers.setdefault("severity", severity)
        case "tag":
            markers.setdefault("tag", list(mark.args))
    return markers


def get_markers(item: pytest.Item) -> dict:
    markers = {}
    for mark in item.iter_markers():
        try:
            match mark.name:
                case "allure_label":
                    get_allure_markers(markers, mark)
                case "owner":
                    if not mark.args:
                        return
                    markers.setdefault("owner", mark.args[0])
        except (IndexError, KeyError, AttributeError):
            logger.warning(f"can not found test label for {item.name}")
            continue
    return markers


def is_atstack(item: pytest.Item) -> bool | tuple[str, str, str]:
    atstack = item.config.getoption("--atstack")
    vars = ["ATSTACK_URL", "ATSTACK_PROJECT_TOKEN", "ATSTACK_REPORT_ID"]
    url, token, id = [os.environ.get(var, None) for var in vars]
    return (url, token, id) if all([atstack, url, token, id]) else False


def get_status(status: List[str]) -> Status:
    for state in status:
        if state != "passed":
            return state
    return "passed"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    if ats := is_atstack(item):
        _, token, id = ats
        report = outcome.get_result()
        error = str(report.longrepr) if report.outcome == "failed" else None
        result = {
            "status": report.outcome,
            "duration": report.duration,
            "error": error,
        }
        if not getattr(item, "atstack", None):
            title_name = "__allure_display_name__"
            title = item.name
            try:
                title = getattr(getattr(item, "obj"), title_name)
            except AttributeError:
                logger.warning(f"can not found allure title: {item.name}")
            content = {
                "project_token": token,
                "report_id": id,
                "name": item.name,
                "title": title,
                "marks": get_markers(item),
            }
            setattr(item, "atstack", content)
        atstack = getattr(item, "atstack")
        atstack[report.when] = result


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item: pytest.Item, nextitem):
    _ = yield
    if ats := is_atstack(item):
        url, *_ = ats
        stages = ["setup", "call", "teardown"]
        atstack = getattr(item, "atstack", {})
        status = [atstack[when].get("status") for when in stages if when in atstack]
        atstack["status"] = get_status(status)
        duration = sum(atstack.get(when, {}).get("duration", 0) for when in stages)
        atstack["duration"] = "{:.2f}".format(duration)
        try:
            url = urljoin(url, "/api/reports")
            response = requests.post(url, json=atstack).json()
            assert response.get("success"), response.get("message")
            logger.success(f"₳₮ {atstack.get('title')}")
        except Exception as e:
            logger.info(atstack)
            logger.warning(e)
