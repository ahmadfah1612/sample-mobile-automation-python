import pytest
import os
from appium import webdriver

from helpers.custom_logger import CustomLogger

logger = CustomLogger("TestLogger").get_logger()


def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android", help="Platform to run tests on: android or ios"
    )


@pytest.fixture(scope='function')
def driver(request):
    platform = request.config.getoption("--platform").lower()

    if platform == 'android':
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "sample.apk"),
            "automationName": "UiAutomator2"
        }
    elif platform == 'ios':
        desired_caps = {
            "platformName": "iOS",
            "deviceName": "iPhone Simulator",
            "app": "/path/to/your/ios_app.app",
            "automationName": "XCUITest"
        }
    else:
        raise ValueError("Invalid platform. Choose 'android' or 'ios'.")

    driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.failed:
            logger.error(f"Test '{report.nodeid}' - Result: {report.outcome}")
        elif report.passed:
            logger.info(f"Test '{report.nodeid}' - Result: {report.outcome}")
        elif report.skipped:
            logger.warning(f"Test '{report.nodeid}' - Result: {report.outcome}")
