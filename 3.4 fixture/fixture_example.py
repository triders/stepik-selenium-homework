import pytest
import time
from selenium import webdriver


URL = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def browser():
    print('\nstart browser for test')
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # call fixture browser as a parameter
    def test_guest_must_see_login_link(self, browser):
        browser.get(URL)
        login_link = browser.find_element_by_css_selector("a#login_link")
        time.sleep(2)

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(URL)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        time.sleep(2)
