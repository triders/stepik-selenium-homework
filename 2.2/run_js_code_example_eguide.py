import time
from selenium import webdriver

script = 'function intentoReady(a){"loading"===document.readyState?document.addEventListener("DOMContentLoaded",a):a(event)}intentoReady(()=>{(function(a,b,c,d,e,f,g,h,i,j){i=c.getElementById(a),j=!1,i?"block"===i.style.display&&(j=!0):j=!0,b.IntentoTranslateObject=e,b[e]||(j?b[e]=function(){b[e].q||(b[e].q=[]),b[e].q.push(arguments)}:b[e]=function(){}),j&&(g=c.createElement(d),h=c.getElementsByTagName(d)[0],g.id=e,g.src=f,g.async=1,h.parentNode.insertBefore(g,h))})("s4-titlerow",window,document,"script","it","https://static.inten.to/ikea-eguide/translate.js"),it("translate")});'

url = "https://ikeaklon.infocaption.com/Home?"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(4)

    login_field = browser.find_element_by_css_selector("input[name='username']")
    pwd_field = browser.find_element_by_css_selector("input[name='password']")
    submit_button = browser.find_element_by_css_selector("button[type='submit']")

    login_field.send_keys("intento")
    pwd_field.send_keys("translation")
    submit_button.click()

    time.sleep(5)

    browser.execute_script(script)

finally:
    time.sleep(10)
    browser.quit()
