from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button.click()

    def book_name_check(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGE).text, \
               "Added book does not match with selected book"

    def price_check(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text, \
               "Added book price does not match with selected book price"

    def solve_quiz_and_get_code(self):
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
            print("No second alert presented")