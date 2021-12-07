import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, timeout=15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    print(browser.switch_to.alert.text)


