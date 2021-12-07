import math
import time
from selenium import webdriver

url = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(url)

    time.sleep(3)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()
    assert robot_checkbox.get_attribute("enabled"), "somehow the checkbox appeared not in the checked state 0_o"

    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()

    submit_button = browser.find_element_by_css_selector("form>button.btn.btn-default")
    submit_button.click()

