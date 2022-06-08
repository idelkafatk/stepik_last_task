from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.find_basket_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_msg_about_adding()
    page.compare_basket_and_product_price()

