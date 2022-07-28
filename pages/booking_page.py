from .base_page import BasePage
from datetime import datetime


class BookingPage(BasePage):
    current_date = datetime.now()
    # TODO def fill_date_and_time_with_current_date_plus_one_day(self):
