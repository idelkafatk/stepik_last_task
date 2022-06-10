from .pages.locators import ProductPageLocators
from .pages.element_page import ProductPage
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.find_basket_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser,links): 
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.find_basket_button()
    page.solve_quiz_and_get_code()
    page.message_is_disappeared()