from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ITEM_BTN), 'Add to basket button is not presented'
    
    def add_product_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_ITEM_BTN)
        add_btn.click()
#        self.solve_quiz_and_get_code()
    
    def should_be_success_msg(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), 'There is no success message'
    
    def is_product_name_match(self):
        res = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text

        assert res, 'Product\'s name is not same'
    
    def should_be_basket_price_msg(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MSG), 'There is no basket price message'
    
    def is_basket_price_equal_book_price(self):
        res = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split()[0] == self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG).text.split()[0]

        assert res, 'Product\'s price is not matches with basket price'

    def should_not_be_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
        "Success message is presented, but should not be"
    
    def success_msg_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_PRICE_MSG), \
        "Success message is not disappeared, but should be"
