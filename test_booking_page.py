from pages.main_page import MainPage


class TestBookingPage:
    def test_book_a_table(self, browser):
        link = "https://mts-devonfw-core.cloud.okteto.net"
        main_page = MainPage(browser, link)
        main_page.open()
        booking_page = main_page.click_book_table_on_top_bar()
        booking_page.navigate_to_subpage('bookTable')
        # Check if “book a table” view is present if not click “book a table” tab- - don't understand.
