# import pytest
# from utilities.browser_manager import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def test_search_product():
#     driver = get_driver("chrome")
#     driver.get("https://automationexercise.com/products")
#
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
#     search_box.send_keys("Tshirt")
#     driver.find_element(By.ID, "submit_search").click()
#
#     results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "productinfo")))
#     assert results.is_displayed()
#     print("✅ Product search successful!")
#
#     driver.quit()


#2

# import pytest
# from utilities.browser_manager import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def test_search_product():
#     print("Launching Chrome browser...")
#     driver = get_driver("chrome")
#
#     print("Navigating to product page...")
#     driver.get("https://automationexercise.com/products")
#
#     wait = WebDriverWait(driver, 10)
#
#     print("Locating search box...")
#     search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
#
#     print("Entering product name: 'Tshirt'")
#     search_box.send_keys("Tshirt")
#
#     # print("Entering product name: 'JEANS'")
#     # search_box.send_keys("JEANS")
#
#     print("Clicking search button...")
#     driver.find_element(By.ID, "submit_search").click()
#
#     print("Waiting for search results to appear...")
#     results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "productinfo")))
#
#     print("Verifying search results are displayed...")
#     assert results.is_displayed()
#
#     print("✅ Product search successful!")
#
#     print("Closing browser...")
#     driver.quit()



#
# #-3
# # File: tests/test_search_product.py
# import pytest
# from utilities.browser_manager import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.mark.parametrize("browser_name", ["chrome", "firefox", "edge"])
# def test_search_product(browser_name):
#     print(f"🚀 Launching {browser_name.capitalize()} browser...")
#     driver = get_driver(browser_name)
#
#     try:
#         print("🌐 Navigating to product page...")
#         driver.get("https://automationexercise.com/products")
#
#         wait = WebDriverWait(driver, 10)
#
#         print("🔍 Locating search box...")
#         search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
#
#         print("⌨️ Entering product name: 'Tshirt'")
#         search_box.send_keys("Tshirt")
#
#         print("🖱️ Clicking search button...")
#         driver.find_element(By.ID, "submit_search").click()
#
#         print("⏳ Waiting for search results to appear...")
#         results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "productinfo")))
#
#         print("✅ Verifying search results are displayed...")
#         assert results.is_displayed()
#
#         print("🎉 Product search successful!")
#
#     finally:
#         print("🧹 Closing browser...")
#         driver.quit()
#


#-4
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


# --------------------------
# Get driver function
# --------------------------
def get_driver(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.set_page_load_timeout(45)
    return driver


# --------------------------
# Test case
# --------------------------
@pytest.mark.parametrize("browser_name", ["chrome"])
def test_search_product(browser_name):
    print(f"\n🚀 Launching {browser_name.capitalize()} browser...")
    driver = get_driver(browser_name)

    try:
        print("🌐 Navigating to product page...")
        driver.get("https://automationexercise.com/products")

        print("🔍 Waiting for search box...")
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_product"))
        )

        print("⌨️ Typing search term...")
        search_input.clear()
        search_input.send_keys("TSHIRTS")

        print("🖱️ Clicking search button...")
        search_button = driver.find_element(By.ID, "submit_search")
        search_button.click()

        print("⏳ Waiting for results...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
        )

        print("✅ Search results appeared!")
        assert "Searched Products" in driver.page_source

    except Exception as e:
        print(f"❌ Test failed on {browser_name}: {e}")
        raise

    finally:
        print("🧹 Closing browser...")
        driver.quit()
