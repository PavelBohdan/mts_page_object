from selenium import webdriver
import pytest



@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()
