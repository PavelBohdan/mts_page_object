from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        return self.browser.get(self.url)

    def find_element(self, locator, timeout=2):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            return None

    def find_elements(self, locator, timeout=2):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except TimeoutException:
            return None

    def is_element_present(self, locator, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_not_present(self, locator, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_active(self, locator, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def is_element_not_active(self, locator, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def navigate_to_subpage(self, subpage_name):
        url = self.browser.current_url
        assert subpage_name in url
