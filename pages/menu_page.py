from .base_page import BasePage
from .locators import MainPageLocators, MenuPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage(BasePage):
    def click_check_box_tofu_thai_green_chicken_curry(self):
        check_box = self.find_element(MenuPageLocators.CHECK_BOX_TOFU_THAI_GREEN_CHICKEN_CURRY_LOCATOR)
        check_box.click()

    def click_check_box_extra_curry_thai_green_chicken_curry(self):
        check_box = self.find_element(MenuPageLocators.CHECK_BOX_EXTRA_CURRY_THAI_GREEN_CHICKEN_CURRY_LOCATOR)
        check_box.click()

    def click_add_to_order_thai_green_chicken_curry(self):
        check_box = self.find_element(MenuPageLocators.ADD_TO_ORDER_BUTTON_LOCATOR)
        check_box.click()

    def check_resume_booking_pop_up_is_visible(self):
        assert self.is_element_present(MenuPageLocators.RESUME_BOOKING_POP_UP_TITLE_LOCATOR)

    def check_additional_option_in_the_order(self, ingredients):
        assert ingredients.lower() in self.find_element(MenuPageLocators.ADDITIONAL_OPTIONS_LOCATOR).text.lower()

    def check_save_button_is_not_active(self):
        assert self.is_element_not_active(MenuPageLocators.SEND_BUTTON_LOCATOR)