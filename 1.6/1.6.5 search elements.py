from selenium import webdriver
import time


url = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    required_fields = browser.find_elements_by_css_selector("input[required]")
    for field in required_fields:
        field.send_keys("slonik")

    time.sleep(7)

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    time.sleep(2)

    message_element = browser.find_element_by_tag_name("h1")
    message = message_element.text
    print(message_element)
    assert message == "Congratulations! You have successfully registered!"

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
