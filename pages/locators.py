from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > :nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ABOUT_ADDITION = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner h1")
    MESSAGE_WITH_BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    MESSAGE_THAT_BASKET_IS_EMPTY = (By.XPATH, "//p[contains(text(), 'basket is empty')]")
    PRODUCT = (By.CSS_SELECTOR, ".basket-items")
