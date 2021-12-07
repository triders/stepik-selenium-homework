from selenium.webdriver.common.print_page_options import PrintOptions
from selenium import webdriver

""" 
print page as html 
https://www.selenium.dev/documentation/webdriver/browser_manipulation/
"""

url = "https://www.selenium.dev/documentation/webdriver/browser_manipulation/"


with webdriver.Chrome("headless") as browser:
    browser.get(url)

    print_options = PrintOptions()
    print_options.page_ranges = ['1-2']




