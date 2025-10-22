# import pytest
# from utilities.browser_manager import get_driver
# from pages.signup_page import SignupPage
# import time
#
# def test_existing_email_signup():
#     driver = get_driver("chrome")
#     signup_page = SignupPage(driver)
#
#     try:
#         signup_page.open()
#
#         # Step 1: Verify home page is visible
#         if "Automation Exercise" in driver.title:
#             print("✅ Home page is visible successfully")
#         else:
#             pytest.fail("❌ Home page title is incorrect")
#
#         # Step 2: Click 'Signup / Login'
#         signup_page.click_signup_login()
#         print("🧭 Clicked on 'Signup / Login'")
#
#         # Step 3: Verify 'New User Signup!' is visible
#         if signup_page.is_visible(signup_page.NAME_INPUT):
#             print("✅ 'New User Signup!' is visible")
#         else:
#             pytest.fail("❌ 'New User Signup!' section not visible")
#
#         # Step 4: Enter existing email
#         name = "Gaurav Kumar"
#         existing_email = "krgauravoutlook@gmail.com"  # make sure it's registered
#         signup_page.type(signup_page.NAME_INPUT, name)
#         signup_page.type(signup_page.EMAIL_INPUT, existing_email)
#         signup_page.click(signup_page.SIGNUP_BTN)
#
#         time.sleep(2)  # Optional: allow error to appear
#
#         # Step 5: Verify error message
#         if signup_page.is_email_already_exists_visible():
#             print("✅ Error message 'Email Address already exist!' verified successfully!")
#         else:
#             driver.save_screenshot("error_message_not_found.png")
#             pytest.fail("❌ Expected error message 'Email Address already exist!' not found. Screenshot saved.")
#
#     except Exception as e:
#         driver.save_screenshot("test_exception.png")
#         pytest.fail(f"❌ Test failed due to unexpected error: {e}. Screenshot saved.")
#
#     finally:
#         driver.quit()



#  ---2
import pytest
from utilities.browser_manager import get_driver
from pages.signup_page import SignupPage
import time

def test_existing_email_signup():
    # Pass headless=True to run without UI in CI, set it to False for local debugging
    driver = get_driver("chrome", headless=True)  # Run headless mode
    signup_page = SignupPage(driver)

    try:
        signup_page.open()

        # Step 1: Verify home page is visible
        if "Automation Exercise" in driver.title:
            print("✅ Home page is visible successfully")
        else:
            pytest.fail("❌ Home page title is incorrect")

        # Step 2: Click 'Signup / Login'
        signup_page.click_signup_login()
        print("🧭 Clicked on 'Signup / Login'")

        # Step 3: Verify 'New User Signup!' is visible
        if signup_page.is_visible(signup_page.NAME_INPUT):
            print("✅ 'New User Signup!' is visible")
        else:
            pytest.fail("❌ 'New User Signup!' section not visible")

        # Step 4: Enter existing email
        name = "Gaurav Kumar"
        existing_email = "krgauravoutlook@gmail.com"  # make sure it's registered
        signup_page.type(signup_page.NAME_INPUT, name)
        signup_page.type(signup_page.EMAIL_INPUT, existing_email)
        signup_page.click(signup_page.SIGNUP_BTN)

        time.sleep(2)  # Optional: allow error to appear

        # Step 5: Verify error message
        if signup_page.is_email_already_exists_visible():
            print("✅ Error message 'Email Address already exist!' verified successfully!")
        else:
            driver.save_screenshot("error_message_not_found.png")
            pytest.fail("❌ Expected error message 'Email Address already exist!' not found. Screenshot saved.")

    except Exception as e:
        driver.save_screenshot("test_exception.png")
        pytest.fail(f"❌ Test failed due to unexpected error: {e}. Screenshot saved.")

    finally:
        driver.quit()
