from .pages.main_page import MainPage

# pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
#def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()


#def test_add_to_cart(browser):
#    page = ProductPage(url="", browser)   # инициализируем объект Page Object
#    page.open()                           # открываем страницу в браузере
#    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
#    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
#    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
