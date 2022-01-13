import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CSS_SELECTOR = "pre.smart-hints__hint"
URL_LIST = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

URL_LIST_1 = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236903/step/1"
]

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(6)
    yield browser
    browser.quit()


@pytest.mark.parametrize('URL', URL_LIST)
def test_return_ufo_message(browser: webdriver.Chrome, URL):
    browser.get(URL)
    answer = math.log(int(time.time()))
    answer_field = browser.find_element_by_css_selector("textarea.ember-text-area.ember-view")
    answer_field.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector("button.submit-submission")
    submit_button.click()
    congrats_message_text = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    if congrats_message_text != "Correct!":
        print("\nUFO_MESSAGE_PART:", congrats_message_text)
