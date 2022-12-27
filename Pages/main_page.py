import sys
import allure

from selenium.common import TimeoutException
from .common_methods import CommonMethods
from .locators import MainPageLocators


class MainPage(CommonMethods):
    """В этом классе описаны методы для работы с главной страницей"""

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу каталога")
    def go_to_catalog_page(self):
        try:
            self.click_element(*MainPageLocators.DESKTOPS_BTN)
            self.click_element(*MainPageLocators.DESKTOPS_MAC_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод go_to_catalog_page завершился ошибкой')

    @allure.step("Переход на страницу регистрации")
    def go_to_register_page(self):
        try:
            self.click_element(*MainPageLocators.PROFILE_BUTTON)
            self.click_element(*MainPageLocators.REGISTER_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод go_to_register_page завершился ошибкой')

    @allure.step("Смена отображаемой валюты")
    def change_currency(self, currency):
        self.click_element(*MainPageLocators.SELECT_CURRENCY_BTN)
        if currency == 'dollar':
            self.click_element(*MainPageLocators.SELECT_DOLLAR)
        elif currency == 'euro':
            self.click_element(*MainPageLocators.SELECT_EURO)
        elif currency == 'pound':
            self.click_element(*MainPageLocators.SELECT_POUND)
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError('Передана неверная валюта')

    @allure.step("Проверка отображаемой валюты на главной странице")
    def check_currency_on_main_page(self, currency):
        basket_price = self.find_element(*MainPageLocators.BASKET_BUTTON_TEXT)
        if currency == 'dollar':
            try:
                self.find_element(MainPageLocators.PRODUCT_PRICE[0], MainPageLocators.PRODUCT_PRICE[1].format('$602.00'))
                if basket_price.text[-5] == '$':
                    return True
            except TimeoutException:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                return False
        elif currency == 'euro':
            try:
                self.find_element(MainPageLocators.PRODUCT_PRICE[0], MainPageLocators.PRODUCT_PRICE[1].format('472.33€'))
                if basket_price.text[-1] == '€':
                    return True
            except TimeoutException:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                return False
        elif currency == 'pound':
            try:
                self.find_element(MainPageLocators.PRODUCT_PRICE[0], MainPageLocators.PRODUCT_PRICE[1].format('£368.73'))
                if basket_price.text[-5] == '£':
                    return True
            except TimeoutException:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                return False
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError('Передана неверная валюта/Что-то пошло не так')

