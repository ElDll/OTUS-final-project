import logging


from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class CommonMethods:
    def __init__(self, driver):
        self.driver = driver

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log", encoding='UTF-8')
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def find_element(self, by: By, selector: str, timeout=5) -> WebElement:
        self.logger.info("Find element {}".format(selector))
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector)), message=f'No such element {selector}')

    def click_element(self, by: By, selector: str):
        self.logger.info("Clicking element: {}".format(selector))
        self.find_element(by, selector).click()

    def input_value(self, by: By, selector: str, value):
        self.logger.info("Input {} in input {}".format(value, selector))
        self.find_element(by, selector).send_keys(value)

    def check_element(self, by: By, selector: str):
        """
        Обертка над WebDriverWait и expected_condition. Поиск элемента,
        который отобразился не только
        в DOM дереве, но и имеет высоту/ширину - явно отобразился на странице.
        """
        self.logger.info("Check if element {} is present".format(selector))
        try:
            self.find_element(by, selector)
            return WebDriverWait
        except TimeoutException:
            return False







