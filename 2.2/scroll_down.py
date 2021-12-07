import time
import math
from selenium import webdriver


url = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    result = str(calc(x_value))

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robot_radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(7)
    browser.quit()
