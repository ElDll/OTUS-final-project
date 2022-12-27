import sys

import allure
from selenium.common import TimeoutException

from .common_methods import CommonMethods
from .locators import CatalogPageLocators


class CatalogPage(CommonMethods):
    """В этом классе описаны методы для работы со страницей каталога"""

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу товара")
    def go_to_product_page(self):
        try:
            self.click_element(*CatalogPageLocators.IMAC_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод go_to_product_page завершился ошибкой')