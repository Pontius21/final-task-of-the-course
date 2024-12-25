from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_THAT_BASKET_IS_EMPTY), "Message that the basket is empty is not presented"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Product is presented, but should not be"
