import pytest
from utilities.browser_manager import get_driver
from pages.signup_page import SignupPage

def test_signup_add_customer():
    driver = get_driver("chrome")
    signup_page = SignupPage(driver)
    signup_page.open()

    personal_name = "Gaurav Kumar"
    personal_email = "gauravtest123@gmail.com"   # use a fresh test email if possible
    personal_password = "12345"

    print(f"🧾 Trying to register or login using existing account: {personal_email}")

    signup_page.register_or_login_existing_user(personal_name, personal_email, personal_password)

    assert signup_page.is_logged_in(), "❌ Login/Signup failed!"
    print("✅ Account accessed successfully!")

    signup_page.logout()
    driver.quit()
