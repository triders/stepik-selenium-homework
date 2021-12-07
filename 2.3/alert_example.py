import time
from selenium import webdriver


url = "https://example.com"

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(3)

    browser.execute_script("alert('Hello')")
    time.sleep(2)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)

    browser.execute_script("prompt('Hello')")
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.send_keys("hi")
    prompt.accept()
    time.sleep(2)

