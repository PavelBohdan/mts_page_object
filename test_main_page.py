from pages.main_page import MainPage
from constants import WAITER_USERNAME, WAITER_PASSWORD


class TestMainPage:
    def test_login_and_log_out_as_waiter(self, browser):
        link = "https://mts-devonfw-core.cloud.okteto.net"
        main_page = MainPage(browser, link)
        main_page.open()
        # main_page.navigate_to_subpage('restaurant') // Not working at this moment
        main_page.username_is_not_visible(WAITER_USERNAME)
        main_page.click_user_button()
        main_page.login_pop_up_is_visible()
        main_page.login_button_on_popup_is_disabled()
        main_page.fill_username_on_login_popup(WAITER_USERNAME)
        main_page.fill_password_on_login_popup(WAITER_PASSWORD)
        main_page.click_login_button_on_popup()
        main_page.login_pop_up_is_not_visible()
        main_page.navigate_to_subpage('orders')
        main_page.username_is_visible(WAITER_USERNAME)
        main_page.click_logged_user_button()
        main_page.username_pop_up_is_visible()
        main_page.click_sign_out_on_user_menu_popup()
        main_page.username_is_not_visible(WAITER_USERNAME)



