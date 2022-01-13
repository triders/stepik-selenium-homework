import pytest
from selenium import webdriver


URL = 'http://selenium1py.pythonanywhere.com/'


# @pytest.fixture(scope="function")
# def browser():
#     print('\nStarting a browser for test')
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nQuitting the browser")
#     browser.quit()


class TestMainPage1():
    # call fixture browser as a parameter
    @pytest.mark.smoke
    def test_guest_must_see_login_link(self, browser):
        browser.get(URL)
        login_link = browser.find_element_by_css_selector("a#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(URL)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
