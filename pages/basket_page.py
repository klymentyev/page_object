from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)


    def basket_is_empy_message(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text, \
               "Empty basket message is missed"
