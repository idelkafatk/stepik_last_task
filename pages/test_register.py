import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
        link = self.link
        page = LoginPage(browser, link)
        page.open() 
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page.open()
        page.should_not_be_success_message()   
    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page.open()
        page.find_basket_button()
        page.should_not_be_success_message()
