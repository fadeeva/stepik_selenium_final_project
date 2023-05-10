from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY),\
        'Basket is not empty, but should be.'

    def should_be_empty_basket_msg(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG),\
        'There is no empty basket message, but should be.'
