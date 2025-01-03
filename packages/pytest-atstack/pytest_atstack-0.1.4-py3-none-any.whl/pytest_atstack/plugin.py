"""pytest-RESEND
实时同步测试执行结果, 通过包装内置插件实现

环境变量
需要在配置文件中声明以环境变量方式读取
1. RESEND_URL
2. RESEND_TOKEN
3. RESEND_NAME
需要在CI环境流水线构建之前自动生成报告日期
4. RESEND_START
linux: export RESEND_START=$(date "+%Y%m%d%H%M%S")

同步API
1. /api/projects(GET) token => project_id
2. /api/reports(GET, POST) name, start => report_id
3. /api/tests(POST) report_id => insert
"""

import configparser
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List
from urllib.parse import ParseResult, urljoin, urlparse

import pytest
import requests

logging.basicConfig(
    format="[RESEND] %(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


@dataclass
class BaseConfig:
    url: str
    token: str
    name: str


@dataclass
class ResendConfig(BaseConfig):
    start: datetime


def is_valid_url(url: str) -> bool:
    try:
        result: ParseResult = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def check_resend_config(config: pytest.Config) -> bool | dict:
    if not config.getoption("resend"):
        return False
    parser = configparser.ConfigParser()
    parser.read(config.inipath)
    if "resend" not in parser.sections():
        return False
    url = parser.get("resend", "url")
    token = parser.get("resend", "token")
    name = parser.get("resend", "name")
    if not all([is_valid_url(url), token, name]):
        return False
    return {"url": url, "token": token, "name": name}


def pytest_addoption(parser: pytest.Parser):
    group = parser.getgroup("resend")
    start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    group.addoption(
        "--resend",
        action="store_const",
        const=start,
        default=start,
        help="resend test results.",
    )


def pytest_configure(config: pytest.Config):
    resend = check_resend_config(config)
    if not resend:
        return
    resend_time = config.getoption("resend")
    resend = ResendConfig(**resend, start=resend_time)
    setattr(config, "resend", resend)


def pytest_report_header(config: pytest.Config, start_path):
    if not check_resend_config(config):
        return
    resend: ResendConfig = config.resend
    return "RESEND URL: {0} TOKEN: {1} NAME: {2} START: {3}".format(
        resend.url, resend.token, resend.name, resend.start
    )


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
                case "title":
                    if not mark.args:
                        return
                    markers.setdefault("title", mark.args[0])
                case "owner":
                    if not mark.args:
                        return
                    markers.setdefault("owner", mark.args[0])
                case "severity":
                    if not mark.args:
                        return
                    markers.setdefault("severity", mark.args[0])
                case "tag":
                    if not mark.args:
                        return
                    markers.setdefault("tag", list(mark.args))
        except (IndexError, KeyError, AttributeError):
            logging.warning(f"can not found test label for {item.name}")
            continue
    return markers


def get_status(status: List[str]):
    for state in status:
        if state != "passed":
            return state
    return "passed"


@pytest.hookimpl(trylast=True)
def pytest_collection_finish(session: pytest.Session):
    if not check_resend_config(session.config):
        return
    resend: ResendConfig = session.config.resend
    try:
        url = urljoin(resend.url, "/api/projects")
        response = requests.get(url, params={"token": resend.token}).json()
        assert response.get("success"), response.get("message")
        projectId = response.get("data").get("projectId")
        total = len(session.items)
        url = urljoin(url, "/api/reports")
        report = {
            "name": resend.name,
            "start": resend.start,
            "total": total,
            "projectId": projectId,
        }
        response = requests.post(url, json=report).json()
        assert response.get("success"), response.get("message")
    except requests.RequestException as e:
        logging.error(f"failed to fetch project id with token {resend.token}: {e}")
    except AssertionError as e:
        logging.error(f"invalid response from API: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    if not check_resend_config(item.config):
        return
    report: pytest.TestReport = outcome.get_result()
    error = str(report.longrepr) if report.outcome == "failed" else None
    content = {
        "status": report.outcome,
        "duration": round(report.duration, 2),
        "error": error,
    }
    if not getattr(item, "result", None):
        title_name = "__allure_display_name__"
        title = item.name
        try:
            title = getattr(getattr(item, "obj"), title_name)
        except AttributeError:
            pass
        markers = get_markers(item)
        mark_title = markers.get("title", None)
        if mark_title:
            markers.pop("title")
        result = {
            "name": item.name,
            "title": mark_title if mark_title else title,
            "marks": markers,
        }
        setattr(item, "result", result)
    result = getattr(item, "result", {})
    result[report.when] = content


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item: pytest.Item, nextitem):
    _ = yield
    if not check_resend_config(item.config):
        return
    resend: ResendConfig = item.config.resend
    stages = ["setup", "call", "teardown"]
    result = getattr(item, "result", {})
    status = [result[when].get("status") for when in stages if when in result]
    result["status"] = get_status(status)
    duration = sum(result.get(when, {}).get("duration", 0) for when in stages)
    result["duration"] = round(duration, 2)
    try:
        url = urljoin(resend.url, "/api/reports")
        response = requests.get(
            url,
            params={
                "name": resend.name,
                "start": resend.start,
            },
        ).json()
        assert response.get("success"), response.get("message")
        reportId = response.get("data").get("reportId")
        if workerInput := getattr(item.config, "workerinput", None):
            result["workerId"] = workerInput.get("workerid")
        result.update(reportId=reportId)
        url = urljoin(resend.url, "/api/tests")
        response = requests.post(url, json=result).json()
        assert response.get("success"), response.get("message")
    except Exception as e:
        logging.warning(f"failed to send report: {e}")
