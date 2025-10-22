# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def click(self, locator):
#         self.wait.until(EC.element_to_be_clickable(locator)).click()
#
#     def type(self, locator, text):
#         element = self.wait.until(EC.visibility_of_element_located(locator))
#         element.clear()
#         element.send_keys(text)
#
#     def get_text(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator)).text
#
#     def is_visible(self, locator):
#         try:
#             self.wait.until(EC.visibility_of_element_located(locator))
#             return True
#         except:
#             return False




# File: pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Wait for element to be clickable, then click."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        """Wait for input to be visible, clear it, then type text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return visible text of an element."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Check if element is visible on the page."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
