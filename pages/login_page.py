from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in str(self.browser.current_url), 'LoginPage url is not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'
        
        assert self.is_element_present(*LoginPageLocators.EMAIL), 'Email input is not presented'
        assert self.is_element_present(*LoginPageLocators.PASSWORD), 'Password input is not presented'
        assert self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD), 'Repeat Password input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BTN), 'Registration button input is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
    
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)
        
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        password_input = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        password_input.send_keys(password)
        
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        register_btn.click()
