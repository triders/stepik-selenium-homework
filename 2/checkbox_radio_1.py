import math
import time
from selenium import webdriver

url = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome() #резервируется оперативка, открывается визуальное очко
    browser.get(url)

    time.sleep(3)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()

    submit_button = browser.find_element_by_css_selector("form>button.btn.btn-default")
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()
