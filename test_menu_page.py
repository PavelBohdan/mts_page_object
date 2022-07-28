from pages.main_page import MainPage
from constants import WAITER_USERNAME, WAITER_PASSWORD

class TestMenuPage:
    def test_add_thai_green_chicken_curry_with_extra_tofu_and_extra_curry(self, browser):
        link = "https://mts-devonfw-core.cloud.okteto.net"
        main_page = MainPage(browser, link)
        main_page.open()
        # main_page.navigate_to_subpage('restaurant') // Not working at this moment
        menu_page = main_page.click_menu_on_top_bar()
        menu_page.navigate_to_subpage('menu')
        menu_page.click_check_box_tofu_thai_green_chicken_curry()
        menu_page.click_check_box_extra_curry_thai_green_chicken_curry()
        menu_page.click_add_to_order_thai_green_chicken_curry()
        menu_page.check_resume_booking_pop_up_is_visible()
        menu_page.check_additional_option_in_the_order('Tofu')
        menu_page.check_additional_option_in_the_order('Extra curry')
        menu_page.check_save_button_is_not_active()

