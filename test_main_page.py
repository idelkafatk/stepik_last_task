from .pages.locators import LoginPageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
link = "http://selenium1py.pythonanywhere.com/ru/"

# def test_guest_can_go_to_login_page(browser):
    #page = MainPage(browser, link)
    #page.open()
    #page.go_to_login_page()

# def test_guest_should_see_login_link(browser):
    #page = MainPage(browser, link)
    #page.open()
    #page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.there_are_no_items()
    page.is_message_about_no_items()


