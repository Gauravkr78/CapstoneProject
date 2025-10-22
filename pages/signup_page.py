#
# # Working -01
# # from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from pages.base_page import BasePage
# import time
#
# class SignupPage(BasePage):
#     # Locators
#     NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
#     EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
#     SIGNUP_BTN = (By.XPATH, "//button[@data-qa='signup-button']")
#     ACCOUNT_CREATED_MSG = (By.XPATH, "//h2[@data-qa='account-created']")
#     CONTINUE_BTN = (By.XPATH, "//a[@data-qa='continue-button']")
#     LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
#     LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
#     LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
#     LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
#     LOGOUT_BTN = (By.XPATH, "//a[@href='/logout']")  # ✅ fixed locator
#
#     def open(self):
#         self.driver.get("https://automationexercise.com/login")
#         print("🌐 Opened Automation Exercise login/signup page")
#         self.hide_ads()
#
#     def hide_ads(self):
#         """Hide common advertisements or popups."""
#         try:
#             self.driver.execute_script("""
#                 document.querySelectorAll('iframe, .ads, .ad-banner, .popup, #ads, #ad-sidebar')
#                     .forEach(el => el.style.display='none');
#             """)
#             print("🛡️ Ads hidden from page.")
#         except Exception:
#             pass
#
#     def register_or_login_existing_user(self, name, email, password):
#         """Try to register; fallback to login if account exists."""
#         self.hide_ads()
#         try:
#             self.type(self.NAME_INPUT, name)
#             self.type(self.EMAIL_INPUT, email)
#             self.click(self.SIGNUP_BTN)
#             print("✅ New signup form opened, proceeding with registration...")
#             self.fill_registration_form(password)
#         except Exception as e:
#             print(f"⚠️ Signup failed, trying login instead: {e}")
#             self.type(self.LOGIN_EMAIL, email)
#             self.type(self.LOGIN_PASSWORD, password)
#             self.click(self.LOGIN_BUTTON)
#
#     def fill_registration_form(self, password):
#         """Fill the signup form completely and create the account."""
#         self.hide_ads()
#         try:
#             # Fill details
#             self.type((By.ID, "password"), password)
#             self.type((By.ID, "first_name"), "Gaurav")
#             self.type((By.ID, "last_name"), "Kumar")
#             self.type((By.ID, "address1"), "123 Test Street")
#             self.type((By.ID, "state"), "Karnataka")
#             self.type((By.ID, "city"), "Bangalore")
#             self.type((By.ID, "zipcode"), "560001")
#             self.type((By.ID, "mobile_number"), "9876543210")
#             print("✅ Registration form filled successfully.")
#
#             # Create account
#             self.hide_ads()
#             self.click((By.XPATH, "//button[@data-qa='create-account']"))
#             print("✅ Clicked 'Create Account' button.")
#
#             if self.is_visible(self.ACCOUNT_CREATED_MSG):
#                 print("🎉 Account created successfully!")
#
#             self.click(self.CONTINUE_BTN)
#             time.sleep(2)
#
#         except Exception as e:
#             print(f"⚠️ Registration form submission failed: {e}")
#
#     def is_logged_in(self):
#         """Check if user is logged in."""
#         self.hide_ads()
#         try:
#             return self.is_visible(self.LOGGED_IN_TEXT)
#         except NoSuchElementException:
#             return False
#
#     def logout(self):
#         """Logout the current user."""
#         self.hide_ads()
#         try:
#             if self.is_logged_in():
#                 print("🚪 Attempting to log out...")
#                 logout_btn = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BTN))
#                 self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_btn)
#                 try:
#                     self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()
#                 except Exception:
#                     self.driver.execute_script("arguments[0].click();", logout_btn)
#                 print("✅ Logged out successfully!")
#                 time.sleep(2)
#             else:
#                 print("⚠️ Cannot logout, user is not logged in.")
#         except Exception as e:
#             print(f"⚠️ Logout failed: {e}")


# #2
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pages.base_page import BasePage
#
# class SignupPage(BasePage):
#     # Locators
#     SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
#     NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
#     EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
#     SIGNUP_BTN = (By.XPATH, "//button[@data-qa='signup-button']")
#     EMAIL_ALREADY_EXISTS_MSG = (By.XPATH, "//*[contains(text(),'Email Address already exist')]")
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def open(self):
#         self.driver.get("https://automationexercise.com/")
#         self.driver.maximize_window()
#         self.hide_ads()
#
#     def hide_ads(self):
#         """Try removing ads if they block elements."""
#         try:
#             self.driver.execute_script("""
#                 document.querySelectorAll('iframe').forEach(el => el.remove());
#             """)
#         except Exception:
#             pass
#
#     def click(self, locator):
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         element.click()
#
#     def type(self, locator, text):
#         element = self.wait.until(EC.visibility_of_element_located(locator))
#         element.clear()
#         element.send_keys(text)
#
#     def is_visible(self, locator):
#         try:
#             self.wait.until(EC.visibility_of_element_located(locator))
#             return True
#         except Exception:
#             return False
#
#     def click_signup_login(self):
#         self.click(self.SIGNUP_LOGIN_LINK)
#
#     def is_email_already_exists_visible(self):
#         try:
#             self.hide_ads()
#             return self.wait.until(
#                 EC.visibility_of_element_located(self.EMAIL_ALREADY_EXISTS_MSG)
#             ).is_displayed()
#         except Exception:
#             return False
#
#     # ✅ NEW METHOD (added below existing ones)
#     def register_or_login_existing_user(self, name, email, password=None):
#         """
#         Attempts to register a user. If email already exists, advises login.
#         `password` is unused for now but included for future login functionality.
#         """
#         self.click_signup_login()
#
#         if self.is_visible(self.NAME_INPUT):
#             print("🔐 Attempting to sign up...")
#             self.type(self.NAME_INPUT, name)
#             self.type(self.EMAIL_INPUT, email)
#             self.click(self.SIGNUP_BTN)
#
#             if self.is_email_already_exists_visible():
#                 print("⚠️ Email already exists. Please login instead.")
#             else:
#                 print("✅ Signup successful or continued to next step.")
#         else:
#             print("❌ Signup form not visible.")

#
# # this  working for existing_email
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pages.base_page import BasePage
#
# class SignupPage(BasePage):
#     # Locators
#     SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
#     NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
#     EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
#     SIGNUP_BTN = (By.XPATH, "//button[@data-qa='signup-button']")
#     EMAIL_ALREADY_EXISTS_MSG = (By.XPATH, "//*[contains(text(),'Email Address already exist')]")
#     LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout')]")
#     LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def open(self):
#         self.driver.get("https://automationexercise.com/")
#         self.driver.maximize_window()
#         self.hide_ads()
#
#     def hide_ads(self):
#         """Try removing ads if they block elements."""
#         try:
#             self.driver.execute_script("""
#                 document.querySelectorAll('iframe').forEach(el => el.remove());
#             """)
#         except Exception:
#             pass
#
#     def click(self, locator):
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         element.click()
#
#     def type(self, locator, text):
#         element = self.wait.until(EC.visibility_of_element_located(locator))
#         element.clear()
#         element.send_keys(text)
#
#     def is_visible(self, locator):
#         try:
#             self.wait.until(EC.visibility_of_element_located(locator))
#             return True
#         except Exception:
#             return False
#
#     def click_signup_login(self):
#         self.click(self.SIGNUP_LOGIN_LINK)
#
#     def is_email_already_exists_visible(self):
#         try:
#             self.hide_ads()
#             return self.wait.until(
#                 EC.visibility_of_element_located(self.EMAIL_ALREADY_EXISTS_MSG)
#             ).is_displayed()
#         except Exception:
#             return False
#
#     def register_or_login_existing_user(self, name, email, password=None):
#         """
#         Attempts to register a user. If email already exists, advises login.
#         Password is included for future use.
#         """
#         self.click_signup_login()
#
#         if self.is_visible(self.NAME_INPUT):
#             print("🔐 Attempting to sign up...")
#             self.type(self.NAME_INPUT, name)
#             self.type(self.EMAIL_INPUT, email)
#             self.click(self.SIGNUP_BTN)
#
#             if self.is_email_already_exists_visible():
#                 print("⚠️ Email already exists. Please login instead.")
#             else:
#                 print("✅ Signup successful or continued to next step.")
#         else:
#             print("❌ Signup form not visible.")
#
#     def is_logged_in(self):
#         """
#         Check if the user is logged in by looking for 'Logged in as' or 'Logout' link.
#         """
#         try:
#             return self.is_visible(self.LOGOUT_LINK) or self.is_visible(self.LOGGED_IN_TEXT)
#         except Exception:
#             return False




from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class SignupPage(BasePage):
    # Locators
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH, "//button[@data-qa='signup-button']")
    EMAIL_ALREADY_EXISTS_MSG = (By.XPATH, "//*[contains(text(),'Email Address already exist')]")
    ACCOUNT_CREATED_MSG = (By.XPATH, "//h2[@data-qa='account-created']")
    CONTINUE_BTN = (By.XPATH, "//a[@data-qa='continue-button']")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout')]")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGOUT_BTN = (By.XPATH, "//a[@href='/logout']")  # Keeps both names for compatibility

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://automationexercise.com/login")
        self.driver.maximize_window()
        print("🌐 Opened Automation Exercise login/signup page")
        self.hide_ads()

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def hide_ads(self):
        """Hide common advertisements or popups."""
        try:
            self.driver.execute_script("""
                document.querySelectorAll('iframe, .ads, .ad-banner, .popup, #ads, #ad-sidebar')
                    .forEach(el => el.style.display='none');
            """)
            print("🛡️ Ads hidden from page.")
        except Exception:
            pass

    def click_signup_login(self):
        """Clicks the Signup/Login link from the homepage."""
        self.click(self.SIGNUP_LOGIN_LINK)

    def is_email_already_exists_visible(self):
        """Checks if the 'Email Address already exist!' message appears."""
        try:
            self.hide_ads()
            return self.wait.until(
                EC.visibility_of_element_located(self.EMAIL_ALREADY_EXISTS_MSG)
            ).is_displayed()
        except Exception:
            return False

    def register_or_login_existing_user(self, name, email, password=None):
        """
        Attempts to register a user. If already registered, fallback to login.
        """
        self.hide_ads()
        try:
            self.type(self.NAME_INPUT, name)
            self.type(self.EMAIL_INPUT, email)
            self.click(self.SIGNUP_BTN)
            print("✅ New signup form opened, proceeding with registration...")
            self.fill_registration_form(password)
        except Exception as e:
            print(f"⚠️ Signup failed, trying login instead: {e}")
            try:
                self.type(self.LOGIN_EMAIL, email)
                self.type(self.LOGIN_PASSWORD, password)
                self.click(self.LOGIN_BUTTON)
                print("✅ Logged in using fallback login form.")
            except Exception as login_err:
                print(f"❌ Login also failed: {login_err}")

    def fill_registration_form(self, password):
        """Fill out the full registration form after clicking 'Signup'."""
        self.hide_ads()
        try:
            self.type((By.ID, "password"), password)
            self.type((By.ID, "first_name"), "Gaurav")
            self.type((By.ID, "last_name"), "Kumar")
            self.type((By.ID, "address1"), "123 Test Street")
            self.type((By.ID, "state"), "Karnataka")
            self.type((By.ID, "city"), "Bangalore")
            self.type((By.ID, "zipcode"), "560001")
            self.type((By.ID, "mobile_number"), "9876543210")
            print("✅ Registration form filled successfully.")

            self.hide_ads()
            self.click((By.XPATH, "//button[@data-qa='create-account']"))
            print("✅ Clicked 'Create Account' button.")

            if self.is_visible(self.ACCOUNT_CREATED_MSG):
                print("🎉 Account created successfully!")

            self.click(self.CONTINUE_BTN)
            time.sleep(2)

        except Exception as e:
            print(f"⚠️ Registration form submission failed: {e}")

    def is_logged_in(self):
        """Check if user is logged in based on 'Logged in as' or Logout link."""
        self.hide_ads()
        try:
            return self.is_visible(self.LOGOUT_LINK) or self.is_visible(self.LOGGED_IN_TEXT)
        except NoSuchElementException:
            return False

    def logout(self):
        """Log the user out if currently logged in."""
        self.hide_ads()
        try:
            if self.is_logged_in():
                print("🚪 Attempting to log out...")
                logout_btn = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BTN))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_btn)
                try:
                    self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", logout_btn)
                print("✅ Logged out successfully!")
                time.sleep(2)
            else:
                print("⚠️ Cannot logout, user is not logged in.")
        except Exception as e:
            print(f"⚠️ Logout failed: {e}")
