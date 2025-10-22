import pytest
from utilities.browser_manager import get_driver
from pages.login_page import LoginPage
import pytest

def test_login_logout():
    driver = get_driver("chrome")
    login_page = LoginPage(driver)

    login_page.open()
    assert login_page.is_login_page_displayed()

    login_page.login("krgauravoutlook@gmail.com", "guru#62052")  # replace with valid account
    print("✅ Logged in successfully!")

    login_page.logout()
    assert login_page.is_login_page_displayed()
    print("✅ Logged out successfully!")

    driver.quit()
