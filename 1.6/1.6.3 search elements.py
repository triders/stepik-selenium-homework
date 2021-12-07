import time

from selenium import webdriver

url = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(1)

    elements = browser.find_elements_by_tag_name("input")

    for element in elements:
        element.send_keys("no")

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
