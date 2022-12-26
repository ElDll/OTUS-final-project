import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.1.76")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--bv")
    parser.addoption("--url", action="store", default='http://192.168.1.76:8081')
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    executor = request.config.getoption("--executor")

    if executor == "local":
        caps = {'goog:chromeOptions': {}}
        if browser == 'chrome':
            _driver = webdriver.Chrome(desired_capabilities=caps)
        elif browser == 'firefox:':
            _driver = webdriver.Firefox(desired_capabilities=caps)
        elif browser == 'opera':
            _driver = webdriver.Opera(desired_capabilities=caps)
        else:
            raise pytest.UsageError("--browser_name should be Chrome or Firefox or Opera")

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Alexey",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": False
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        options = Options()
        if browser == "opera":
            options.add_experimental_option('w3c', True)

        _driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )

    _driver.implicitly_wait(3)
    _driver.get(request.config.getoption("--url"))
    _driver.log_level = log_level
    _driver.logger = logger
    _driver.test_name = request.node.name

    yield _driver
    _driver.quit()
