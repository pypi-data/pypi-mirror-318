import pytest


@pytest.fixture(scope="function")
def su():
    if pytest.__version__:
        raise AssertionError("setup error")
    yield pytest.__version__


@pytest.fixture(scope="function")
def td():
    if pytest.__version__:
        raise AssertionError("teardown error")
    yield pytest.__version__


@pytest.mark.title("测试错误信息")
def test_error(su, td):
    assert su == pytest.__version__ and td == pytest.__version__
