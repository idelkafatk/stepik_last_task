from .base_page import BasePage
from .login_page import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url(By.CSS_SELECTOR, "#login_link")
        self.should_be_login_form(By.CSS_SELECTOR, "#login_form")
        self.should_be_register_form(By.CSS_SELECTOR, "#register_form")

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login url is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True