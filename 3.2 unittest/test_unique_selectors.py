import unittest

from selenium import webdriver


url1 = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"


class TestRequiredFields(unittest.TestCase):

    def test_url1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        browser.get(url1)

        first_name_field = browser.find_element_by_css_selector("input[required].form-control.first")
        last_name_field = browser.find_element_by_css_selector("input[required].form-control.second")
        email_field = browser.find_element_by_css_selector("input[required].form-control.third")

        required_fields = [first_name_field, last_name_field, email_field]

        for field in required_fields:
            field.send_keys("slonik")

        button = browser.find_element_by_css_selector("button.btn.btn-default")
        button.click()

        message_element = browser.find_element_by_tag_name("h1")
        message = message_element.text

        self.assertEqual(message, "Congratulations! You have successfully registered!",
                         f"Cannot find the success message on the page.")


    def test_url2(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(url2)

        first_name_field = browser.find_element_by_css_selector("input[required].form-control.first")
        last_name_field = browser.find_element_by_css_selector("input[required].form-control.second")
        email_field = browser.find_element_by_css_selector("input[required].form-control.third")

        required_fields = [first_name_field, last_name_field, email_field]

        for field in required_fields:
            field.send_keys("slonik")

        button = browser.find_element_by_css_selector("button.btn.btn-default")
        button.click()

        message_element = browser.find_element_by_tag_name("h1")
        message = message_element.text

        self.assertEqual(message, "Congratulations! You have successfully registered!",
                         f"Cannot find the success message on the page.")


if __name__ == "__main__":
    unittest.main()
