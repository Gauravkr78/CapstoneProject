import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="module")
def driver():
    """Initialize Chrome driver and navigate to home page"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://automationexercise.com/")
    print("🌐 Opened Automation Exercise website")
    hide_ads(driver)
    yield driver
    driver.quit()


def hide_ads(driver):
    """Hide overlapping ads and iframes that block clicks"""
    try:
        driver.execute_script("""
            document.querySelectorAll('iframe, .ads, .ad, .ad-container, #ad_sidebar')
            .forEach(el => el.style.display='none');
        """)
        print("🛡️ Ads hidden successfully.")
    except Exception:
        pass


def test_add_to_cart_and_checkout(driver):
    wait = WebDriverWait(driver, 20)
    actions = ActionChains(driver)

    # Step 1: Verify Home page
    assert "Automation Exercise" in driver.title, "❌ Home page title not found!"
    print("✅ Home page visible successfully")

    # Step 2: Click on 'Signup / Login'
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]")))
    login_btn.click()
    print("🧭 Navigated to Login page")

    # Step 3: Log in using valid credentials
    email = "krgauravoutlook@gmail.com"
    password = "guru#62052"
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='login-email']"))).send_keys(email)
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    print("🔐 Login attempted")

    # Step 4: Verify successful login
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logout')]")))
    print("✅ Logged in successfully")

    # Step 5: Click on 'Products' page
    hide_ads(driver)
    products_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']")))
    products_btn.click()
    print("🛍️ Navigated to Products page")
    hide_ads(driver)

    # Step 6: Add first product to cart
    first_product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='productinfo text-center'])[1]"))
    )
    actions.move_to_element(first_product).perform()
    add_first = first_product.find_element(By.XPATH, ".//a[@class='btn btn-default add-to-cart']")
    driver.execute_script("arguments[0].click();", add_first)
    print("🛒 Added first product to cart")

    # Step 7: Continue shopping
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']")))
    continue_btn.click()
    print("🛍️ Continued shopping")

    # Step 8: Add second product to cart
    second_product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='productinfo text-center'])[2]"))
    )
    actions.move_to_element(second_product).perform()
    add_second = second_product.find_element(By.XPATH, ".//a[@class='btn btn-default add-to-cart']")
    driver.execute_script("arguments[0].click();", add_second)
    print("🛒 Added second product to cart")

    # Step 9: Click 'View Cart'
    view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']")))
    driver.execute_script("arguments[0].click();", view_cart)
    print("🛒 Viewing cart page")

    # Step 10: Verify both products added
    cart_rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@id,'product')]")))
    assert len(cart_rows) >= 2, "❌ Expected 2 products in cart!"
    print(f"✅ {len(cart_rows)} products are in the cart")

    # Step 11: Proceed to Checkout
    checkout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-default check_out']")))
    driver.execute_script("arguments[0].click();", checkout_btn)
    print("💳 Proceeding to checkout")

    # Step 12: Confirm Address and Review Order
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Address Details']")))
    print("✅ Address details visible")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Review Your Order']")))
    print("✅ Order review section visible")

    # Step 13: Place Order
    place_order_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Place Order']")))
    driver.execute_script("arguments[0].click();", place_order_btn)
    print("📝 Clicked on 'Place Order'")

    # Step 14: Fill payment details
    wait.until(EC.visibility_of_element_located((By.NAME, "name_on_card"))).send_keys("Gaurav Kumar")
    driver.find_element(By.NAME, "card_number").send_keys("".join([str(random.randint(0, 9)) for _ in range(16)]))
    driver.find_element(By.NAME, "cvc").send_keys("123")
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    driver.find_element(By.NAME, "expiry_year").send_keys("2030")
    print("💳 Payment details entered")

    # Step 15: Pay and Confirm Order
    driver.find_element(By.ID, "submit").click()
    print("✅ Payment submitted")

    # Step 16: Verify success message
    success_msg = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]"))
    )
    assert success_msg.is_displayed(), "❌ Order confirmation not displayed!"
    print("🎉 Order placed successfully!")

    # Step 17: Click 'Continue'
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']")))
    driver.execute_script("arguments[0].click();", continue_btn)
    print("🏁 Order process completed successfully!")

