import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# pytest -v -s -m need_review test_product_page.py
@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.password = str(time.time())
        self.email = self.password + "@fakemail.org"
        new_user = LoginPage(browser, 'http://selenium1py.pythonanywhere.com')
        new_user.open()
        new_user.go_to_login_page()
        new_user.should_be_login_page()
        new_user.register_new_user(self.email, self.password)
        new_user.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_msg()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_success_msg()
        page.is_product_name_match()
        page.should_be_basket_price_msg()
        page.is_basket_price_equal_book_price()


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    ])
def test_guest_can_add_product_to_basket(link, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket(promo=True)
        page.should_be_success_msg()
        page.is_product_name_match()
        page.should_be_basket_price_msg()
        page.is_basket_price_equal_book_price()


@pytest.mark.skip
def test_guest_should_be_add_btn(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_msg()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_msg_should_be_disappeared()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_msg()
