from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url
        self.should_be_login_form
        self.should_be_register_form

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "FAIL"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
   
    def register_new_user(self):
        email_1 = str(time.time()) + "@fakemail.org"
        email = self.browser.find_element(*BasePageLocators.EMAIL)
        email.send_keys(email_1)
        password = self.browser.find_element(*BasePageLocators.PASSWORD)
        password.send_keys("idelka2000")
        password = self.browser.find_element(*BasePageLocators.PASSWORD_2)
        password.send_keys("idelka2000")
        button = self.browser.find_element(By.NAME, "registration_submit")
        button.click()