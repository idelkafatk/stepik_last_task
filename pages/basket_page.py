from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators

class BasketPage(BasePage):
    def there_are_no_items(self):
        assert self.is_element_present(*BasePageLocators.NO_ITEMS), "Basket has items"
        assert True
  
    def is_message_about_no_items(self):
        message = self.browser.find_element(*BasePageLocators.MESSAGE_NO_ITEMS).text
        assert "Ваша корзина пуста" in message, "Can't see message"
        assert True