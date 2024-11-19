from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_message_about_addition(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADDITION), "Message about addition is not presented"

    def should_match_product_name_in_message(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE)
        assert name_product.text == name_in_message.text, \
            "The product name in the message does not match the added product"

    def should_be_message_with_basket_total(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_WITH_BASKET_TOTAL), "Message with basket total is not presented"

    def should_basket_total_equal_product_price(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert basket_total.text == product_price.text, "The basket total is not equal to the product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDITION), \
            "Message about addition is presented, but should not be"

    def should_not_be_success_message_after_delay(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDITION), \
            "Message about addition is presented, but should have disappeared"

