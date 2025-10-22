from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    # ✅ Locators
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BTN = (By.XPATH, "//button[@data-qa='login-button']")
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Logout')]")
    LOGGED_IN_USER = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # ✅ Navigate to website
    def open(self):
        self.driver.get("https://automationexercise.com/")
        print("🌐 Opened Automation Exercise homepage")

    # ✅ Click on Login link and verify login page
    def is_login_page_displayed(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()
            self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
            print("✅ Login page displayed successfully")
            return True
        except TimeoutException:
            print("❌ Login page not loaded properly")
            return False

    # ✅ Perform login
    def login(self, email, password):
        try:
            self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
            self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()
            # Wait until "Logged in as" appears
            self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_USER))
            print(f"✅ Logged in successfully as {email}")
        except TimeoutException:
            print("❌ Login failed — check credentials or page load issue")

    # ✅ Perform logout
    def logout(self):
        try:
            print("🕵️ Checking for Logout button...")
            logout_button = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN))
            logout_button.click()
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK))
            print("✅ Logout successful!")
        except TimeoutException:
            print("❌ Logout button not found or not clickable")

