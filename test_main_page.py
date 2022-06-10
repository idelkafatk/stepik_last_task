from .pages.locators import LoginPageLocators
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.there_are_no_items()
    page.is_message_about_no_items()


