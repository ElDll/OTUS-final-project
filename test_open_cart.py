import pytest
import allure

from .Pages.locators import MainPageLocators
from .Pages.locators import CatalogPageLocators
from .Pages.locators import ProductPageLocators
from .Pages.locators import AdminAuthPageLocators
from .Pages.locators import RegisterPageLocators
from .Pages.admin_page import AdminPage
from .Pages.main_page import MainPage
from .Pages.register_page import RegisterPage
from .Pages.common_methods import CommonMethods


@allure.title('Поиск элементов на main page')
@pytest.mark.main_page
@pytest.mark.parametrize('locator',
                         [MainPageLocators.SEARCH_FIELD,
                          MainPageLocators.NAV_BAR,
                          MainPageLocators.LOGO_FIELD,
                          MainPageLocators.PROFILE_BUTTON,
                          MainPageLocators.BASKET_BUTTON]
                         )
def test_main_page(driver, locator):
    main_page = CommonMethods(driver)
    assert main_page.check_element(*MainPageLocators.SEARCH_FIELD), f'Element not found {locator[1]}'


@allure.title('Поиск элементов на catalog page')
@pytest.mark.catalog_page
@pytest.mark.parametrize('locator',
                         [CatalogPageLocators.LEFT_NAVBAR,
                          CatalogPageLocators.PRODUCT_CARD,
                          CatalogPageLocators.BASKET_BTN_CARD,
                          CatalogPageLocators.LIKE_BTN_CARD,
                          CatalogPageLocators.SORT_BTN]
                         )
def test_catalog_page(driver, locator):
    catalog_page = CommonMethods(driver)
    assert catalog_page.check_element(*locator), f'Element not found {locator[1]}'


@allure.title('Поиск элементов на product page')
@pytest.mark.product_page
@pytest.mark.parametrize('locator',
                         [ProductPageLocators.PRODUCT_PHOTO,
                          ProductPageLocators.PRODUCT_PRICE,
                          ProductPageLocators.ADD_BTN,
                          ProductPageLocators.PRODUCT_NAME,
                          ProductPageLocators.LIKE_PRODUCT_BTN]
                         )
def test_catalog_page(driver, locator):
    product_page = CommonMethods(driver)
    assert product_page.check_element(*locator), f'Element not found {locator[1]}'


@allure.title('Поиск элементов на admin page')
@pytest.mark.admin_page
@pytest.mark.parametrize('locator',
                         [AdminAuthPageLocators.ADMIN_TITLE,
                          AdminAuthPageLocators.USER_FIELD,
                          AdminAuthPageLocators.PASSWORD_FIELD,
                          AdminAuthPageLocators.FORGOTTEN_BTN,
                          AdminAuthPageLocators.LOGIN_BTN]
                         )
def test_catalog_page(driver, locator):
    admin_page = CommonMethods(driver)
    assert admin_page.check_element(*locator), f'Element not found {locator[1]}'


@allure.title('Поиск элементов на register page')
@pytest.mark.register_page
@pytest.mark.parametrize('locator',
                         [RegisterPageLocators.FIRST_NAME_FIELD,
                          RegisterPageLocators.LAST_NAME_FIELD,
                          RegisterPageLocators.EMAIL_FIELD,
                          RegisterPageLocators.TELEPHONE_FIELD,
                          RegisterPageLocators.CONTINUE_BTN]
                         )
def test_catalog_page(driver, locator):
    register_page = CommonMethods(driver)
    assert register_page.check_element(*locator), f'Element not found {locator[1]}'


@allure.title('Добавление продуктов в админ панели')
@pytest.mark.add_product
def test_add_product(driver):
    admin_page = AdminPage(driver)
    admin_page.login()
    admin_page.go_to_products_page()
    admin_page.add_product()
    assert admin_page.check_product_in_table(), 'Товар не добавлен/Не отображается в таблице'


@allure.title('Удаление продуктов в админ панели')
@pytest.mark.delete_product
def test_delete_product(driver):
    admin_page = AdminPage(driver)
    admin_page.login()
    admin_page.go_to_products_page()
    admin_page.delete_product()
    assert not admin_page.check_product_in_table(), 'Товар не удален из таблицы'


@allure.title('Регистрация нового акканута')
def test_register_user(driver):
    main_page = MainPage(driver)
    main_page.go_to_register_page()
    register_page = RegisterPage(driver)
    register_page.register_user()
    assert register_page.check_created_header(), 'Аккаунт не создан'


@allure.title('Смена валюты в магазине')
@pytest.mark.parametrize('currency',
                         ['dollar',
                          'euro',
                          'pound']
                         )
def test_change_currency(driver, currency):
    main_page = MainPage(driver)
    main_page.change_currency(currency)
    assert main_page.check_currency_on_main_page(currency), 'Изменение валюты прошло неудачно'







