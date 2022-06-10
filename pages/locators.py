from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")
    NO_ITEMS = (By.CSS_SELECTOR, "div.content") 
    MESSAGE_NO_ITEMS = (By.CSS_SELECTOR, "div.content p")
