from selenium import webdriver


url = "http://suninjuly.github.io/cats.html"

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get(url)

    browser.find_element_by_id("button")
