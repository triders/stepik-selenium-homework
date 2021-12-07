import time
import math
from selenium import webdriver

url = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(url)

    journey_button = browser.find_element_by_css_selector("button.trollface.btn")
    journey_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

    print(browser.switch_to.alert.text)
