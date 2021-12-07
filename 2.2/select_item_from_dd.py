import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(2)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    result = str(num1 + num2)

    drop_down_selector = Select(browser.find_element_by_tag_name("select"))
    drop_down_selector.select_by_visible_text(result)

    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()

# function intentoReady(a){"loading"===document.readyState?document.addEventListener("DOMContentLoaded",a):a(event)}intentoReady(()=>{(function(a,b,c,d,e,f,g,h,i,j){i=c.getElementById(a),j=!1,i?"block"===i.style.display&&(j=!0):j=!0,b.IntentoTranslateObject=e,b[e]||(j?b[e]=function(){b[e].q||(b[e].q=[]),b[e].q.push(arguments)}:b[e]=function(){}),j&&(g=c.createElement(d),h=c.getElementsByTagName(d)[0],g.id=e,g.src=f,g.async=1,h.parentNode.insertBefore(g,h))})("s4-titlerow",window,document,"script","it","https://static.inten.to/ikea-eguide/translate.js"),it("translate")});
