from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK          = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID  = (By.CSS_SELECTOR, '#login_link_inc')
    VIEW_BASKET_BUTTON  = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs .btn.btn-default')
    USER_ICON           = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, '#content_inner>.basket-title.hidden-xs')
    EMPTY_BASKET_MSG    = (By.CSS_SELECTOR, '#content_inner>p')


class LoginPageLocators():
    LOGIN_FORM          = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM       = (By.CSS_SELECTOR, '#register_form')
    
    EMAIL               = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD            = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD     = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BTN    = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary[value=Register]')


class MainPageLocators():
    LOGIN_LINK          = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators():
    ADD_ITEM_BTN        = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    
    PRODUCT_NAME        = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE       = (By.CSS_SELECTOR, '.col-sm-6.product_main p')
    
    SUCCESS_MSG         = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success div strong')
    BASKET_PRICE_MSG    = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info div p strong')
