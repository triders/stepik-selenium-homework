import time
import math
from selenium import webdriver

url = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(3)

    print(browser.window_handles)

    journey_button = browser.find_element_by_css_selector("button.btn")
    journey_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)

    print(browser.window_handles)

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

    print(browser.switch_to.alert.text)
