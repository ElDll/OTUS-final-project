from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Search"]')
    NAV_BAR = (By.CSS_SELECTOR, '.nav.navbar-nav')
    LOGO_FIELD = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    PROFILE_BUTTON = (By.CSS_SELECTOR, '.fa.fa-user')
    REGISTER_BTN = (By.XPATH, "//a[normalize-space()='Register']")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')
    SELECT_CURRENCY_BTN = (By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle']")
    SELECT_DOLLAR = (By.CSS_SELECTOR, "button[name='USD']")
    SELECT_EURO = (By.CSS_SELECTOR, "button[name='EUR']")
    SELECT_POUND = (By.CSS_SELECTOR, "button[name='GBP']")
    BASKET_BUTTON_TEXT = (By.CSS_SELECTOR, ".btn.btn-inverse.btn-block.btn-lg.dropdown-toggle > span")
    PRODUCT_PRICE = (By.XPATH, "//p[contains(text(),'{}')]")
    DESKTOPS_BTN = (By.XPATH, "//a[normalize-space()='Desktops']")
    DESKTOPS_MAC_BTN = (By.XPATH, "//a[normalize-space()='Mac (1)']")


class CatalogPageLocators:
    LEFT_NAVBAR = (By.CSS_SELECTOR, '#column-left')
    PRODUCT_CARD = (By.CSS_SELECTOR, '.product-thumb')
    BASKET_BTN_CARD = (
        By.CSS_SELECTOR,'div[class="product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12"] button:nth-child(1)')
    LIKE_BTN_CARD = (
        By.CSS_SELECTOR, 'button[type="button"][data-toggle="tooltip"][data-original-title="Add to Wish List"]')
    SORT_BTN = (By.CSS_SELECTOR, '#input-sort')
    IMAC_BTN = (By.XPATH, "//img[@title='iMac']")


class ProductPageLocators:
    PRODUCT_PHOTO = (By.CSS_SELECTOR, 'ul[class="thumbnails"] li:nth-child(1) a:nth-child(1)')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'ul[class="list-unstyled"] li h2')
    ADD_BTN = (By.XPATH, '//button[@id="button-cart"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div[class="col-sm-4"] h1')
    LIKE_PRODUCT_BTN = (By.CSS_SELECTOR, 'div[id="product-product"] div[class="btn-group"] button:nth-child(1)')


class AdminAuthPageLocators:
    ADMIN_TITLE = (By.CSS_SELECTOR, '.panel-title')
    USER_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_BTN = (By.CSS_SELECTOR, 'a[href="http://192.168.1.76:8081/admin/index.php?route=common/forgotten"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')


class AdminMainPageLocators:
    CATALOG_BTN = (By.CSS_SELECTOR, ".parent.collapsed[href='#collapse1']")
    PRODUCTS_BTN = (By.XPATH, "//ul[@class='collapse in']/li[2]/a")


class AdminProductPageLocators:
    ADD_PRODUCT_BTN = (By.XPATH, "//i[@class='fa fa-plus']")
    TABLE_ELEMENTS = (By.XPATH, "//table[@class='table table-bordered table-hover']/tbody//tr//td[contains(text(),'{}')]")
    PAGINATION_BAR = (By.XPATH, "//ul[@class='pagination']//li//a[contains(text(),'{}')]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    DELETE_BTN = (By.CSS_SELECTOR, ".btn.btn-danger")
    TABLE_CELL_ELEMENTS = (By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr[{}]/td")
    CELL_CHECKBOX = (By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr[{}]/td/input")


class AddFormLocators:
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "#input-name1")
    META_TAG_FIELD = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_BTN = (By.CSS_SELECTOR, "a[href='#tab-data']")
    MODEL_FIELD = (By.CSS_SELECTOR, "#input-model")
    SAVE_PRODUCT_BTN = (By.CSS_SELECTOR, "button[type='submit']")


class RegisterPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_FIELD = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-confirm')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'input[value="Continue"]')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[value='1'][name='agree']")
    CREATED_HEADER = (By.CSS_SELECTOR, "div[id='content'] h1")
