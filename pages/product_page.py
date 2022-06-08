from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    def find_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()
    
    def solve_quiz_and_get_code(self):
        self.browser.implicitly_wait(5)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print 
  
    def should_be_msg_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "Product name not found on message"
        
    def compare_basket_and_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text

        assert product_price == basket_price, "Product price and basket price is not equal"
        
    