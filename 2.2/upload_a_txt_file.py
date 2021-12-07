import os
import time
from selenium import webdriver


url = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
# print(current_dir)
file_path = os.path.join(current_dir, "zero.txt")
# print(file_path)


try:
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(1)

    first_name = browser.find_element_by_css_selector("input[name='firstname'")
    last_name = browser.find_element_by_css_selector("input[name='lastname'")
    email = browser.find_element_by_css_selector("input[name='email'")
    upload_txt_file = browser.find_element_by_id("file")

    first_name.send_keys("Zeleniy")
    last_name.send_keys("Slonik")
    email.send_keys("zs@mail.ru")
    upload_txt_file.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector(".btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
