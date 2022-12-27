import itertools
import sys
import allure

from selenium.common import TimeoutException
from .common_methods import CommonMethods
from .locators import AdminAuthPageLocators, AdminMainPageLocators, AdminProductPageLocators, AddFormLocators
from data.admin_credentials import login, password
from data.product_add_data import product_name, meta_tag_title, model


class AdminPage(CommonMethods):
    """В этом классе описаны методы для работы со страницой админа"""

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Авторизация в админ аккаунте")
    def login(self):
        try:
            self.input_value(*AdminAuthPageLocators.USER_FIELD, login)
            self.input_value(*AdminAuthPageLocators.PASSWORD_FIELD, password)
            self.click_element(*AdminAuthPageLocators.LOGIN_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод go_to_register_page завершился ошибкой')

    @allure.step("Переход на страницу с товарами")
    def go_to_products_page(self):
        try:
            self.click_element(*AdminMainPageLocators.CATALOG_BTN)
            self.click_element(*AdminMainPageLocators.PRODUCTS_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод go_to_register_page завершился ошибкой')

    @allure.step("Добавление нового товара")
    def add_product(self):
        try:
            self.click_element(*AdminProductPageLocators.ADD_PRODUCT_BTN)
            self.input_value(*AddFormLocators.PRODUCT_NAME_FIELD, product_name)
            self.input_value(*AddFormLocators.META_TAG_FIELD, meta_tag_title)
            self.click_element(*AddFormLocators.DATA_BTN)
            self.input_value(*AddFormLocators.MODEL_FIELD, model)
            self.click_element(*AddFormLocators.SAVE_PRODUCT_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод go_to_register_page завершился ошибкой')

    @allure.step("Удаление товара")
    def delete_product(self):
        """
        Метод ищет товар перебирая ячейки таблицы и сравнивая product_name

        Конструкция try/catch в цикле осуществялет пагинацию если не было найдено элемента с product_name
        Если товар был найден - далее находим и кликаем на чек-бокс у этого товара
        Затем нажимаем на кнопку Удалить
        """

        for page_number in itertools.count():
            for cell_number in itertools.count():
                cell = self.driver.find_elements(
                    AdminProductPageLocators.TABLE_CELL_ELEMENTS[0], AdminProductPageLocators.TABLE_CELL_ELEMENTS[1].format(cell_number+1))
                if len(cell) == 0:
                    try:
                        self.click_element(
                            AdminProductPageLocators.PAGINATION_BAR[0],
                            AdminProductPageLocators.PAGINATION_BAR[1].format(page_number + 2))
                        break
                    except TimeoutException:
                        allure.attach(
                            body=self.driver.get_screenshot_as_png(),
                            name="screenshot_image",
                            attachment_type=allure.attachment_type.PNG)
                        raise AssertionError("Товар не найден")
                elif cell[2].text == product_name:
                    self.click_element(
                        AdminProductPageLocators.CELL_CHECKBOX[0], AdminProductPageLocators.CELL_CHECKBOX[1].format(cell_number+1))
                    self.click_element(*AdminProductPageLocators.DELETE_BTN)
                    confirm_alert = self.driver.switch_to.alert
                    confirm_alert.accept()
                    return
                else:
                    continue

    @allure.step("Проверка нахождения товара в таблице")
    def check_product_in_table(self):
        """
        Метод ищет товар по полю Product name в таблице на странице админа

        1-ая конструкция try/catch - переключает на 1 страницу таблицы. Если уже включена 1-ая страница таблицы, то
        будет TimeoutException - который обрабатывается

        Цикл:

        1-ая конструкция try/catch в цикле перебирает поля Product name и ищет в ней поле со значением product_name
        2-ая конструкция try/catch в цикле осуществялет пагинацию если не было найдено элемента с product_name (в формат
        передается номер страницы)
        """

        try:
            self.click_element(
                AdminProductPageLocators.PAGINATION_BAR[0],
                AdminProductPageLocators.PAGINATION_BAR[1].format(1))
        except TimeoutException:
            pass
        for page_number in itertools.count():
            try:
                self.find_element(
                    AdminProductPageLocators.TABLE_ELEMENTS[0], AdminProductPageLocators.TABLE_ELEMENTS[1].format(product_name))
                return True
            except TimeoutException:
                try:
                    self.click_element(
                        AdminProductPageLocators.PAGINATION_BAR[0], AdminProductPageLocators.PAGINATION_BAR[1].format(page_number+2))
                    continue
                except TimeoutException:
                    allure.attach(
                        body=self.driver.get_screenshot_as_png(),
                        name="screenshot_image",
                        attachment_type=allure.attachment_type.PNG)
                    return False
