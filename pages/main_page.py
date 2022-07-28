from .base_page import BasePage
from .menu_page import MenuPage
from .booking_page import BookingPage
from .locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def click_user_button(self):
        user_button = self.find_element(MainPageLocators.USER_BUTTON_LOCATOR)
        user_button.click()

    def username_is_not_visible(self, username):
        assert self.is_element_not_present(MainPageLocators.USER_NAME_LOCATOR)

    def username_is_visible(self, username):
        assert self.is_element_present(MainPageLocators.USER_NAME_LOCATOR)

    def login_pop_up_is_visible(self):
        self.browser.switch_to.frame(self.find_element(MainPageLocators.LOGIN_POP_UP_FRAME_LOCATOR))
        assert self.is_element_present(MainPageLocators.LOGIN_POP_UP_LOCATOR)

    def login_pop_up_is_not_visible(self):
        assert self.is_element_not_present(MainPageLocators.LOGIN_POP_UP_LOCATOR)

    def login_button_on_popup_is_disabled(self):
        assert self.is_element_not_active(MainPageLocators.LOGIN_BUTTON_LOCATOR)

    def fill_username_on_login_popup(self, username):
        username_field = self.find_element(MainPageLocators.USERNAME_FIELD_LOCATOR)
        username_field.send_keys(username)

    def fill_password_on_login_popup(self, password):
        password_field = self.find_element(MainPageLocators.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(password)

    def click_login_button_on_popup(self, timeout=4):
        login_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_LOCATOR))
        login_button.click()

    def click_logged_user_button(self):
        user_button = self.find_element(MainPageLocators.LOGGED_USER_BUTTON_LOCATOR)
        user_button.click()

    def username_pop_up_is_visible(self):
        self.browser.switch_to.frame(self.find_element(MainPageLocators.USER_MENU_POPUP_FRAME_LOCATOR))
        assert self.is_element_present(MainPageLocators.USER_MENU_POPUP_LOCATOR)

    def click_sign_out_on_user_menu_popup(self):
        signout_button = self.find_element(MainPageLocators.SIGN_OUT_BUTTON_LOCATOR)
        signout_button.click()

    def click_menu_on_top_bar(self):
        menu_button = self.find_element(MainPageLocators.MENU_BUTTON_LOCATOR)
        menu_button.click()
        return MenuPage(self.browser, self.url)

    def click_book_table_on_top_bar(self):
        book_button = self.find_element(MainPageLocators.BOOK_BUTTON_LOCATOR)
        book_button.click()
        return BookingPage(self.browser, self.url)