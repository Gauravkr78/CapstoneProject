# # corrected -1
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from selenium.webdriver.firefox.service import Service as FirefoxService
# # from selenium.webdriver.edge.service import Service as EdgeService
# # from webdriver_manager.chrome import ChromeDriverManager
# # from webdriver_manager.firefox import GeckoDriverManager
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# #
# # def get_driver(browser="chrome"):
# #     if browser.lower() == "chrome":
# #         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# #     elif browser.lower() == "firefox":
# #         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# #     elif browser.lower() == "edge":
# #         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# #     else:
# #         raise Exception("Unsupported browser!")
# #
# #     driver.maximize_window()
# #     driver.implicitly_wait(10)
# #     return driver
#
#
# # File: utilities/browser_manager.py
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# def get_driver(browser="chrome"):
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser.lower() == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     elif browser.lower() == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     else:
#         raise Exception("Unsupported browser!")
#
#     # ✅ Reduced timeouts
#     driver.set_page_load_timeout(15)   # Page load timeout reduced to 15 seconds
#     driver.implicitly_wait(5)          # Implicit wait reduced to 5 seconds
#     driver.maximize_window()
#
#     return driver




# File: utilities/browser_manager.py-2  working any prob then rev -3
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# def get_driver(browser="chrome"):
#     browser = browser.lower()
#
#     if browser == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--disable-notifications")
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#
#     elif browser == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.set_preference("dom.webnotifications.enabled", False)
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
#
#     elif browser == "edge":
#         options = webdriver.EdgeOptions()
#         options.add_argument("--disable-notifications")
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
#
#     else:
#         raise Exception(f"Unsupported browser: {browser}")
#
#     # Common settings
#     driver.set_page_load_timeout(15)   # Reduced page load timeout
#     driver.implicitly_wait(5)          # Reduced implicit wait
#     driver.maximize_window()
#
#     return driver


#file -3# utilities/browser_manager.py
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver(browser="chrome", headless=False):
    """
    Returns a Selenium WebDriver instance for the specified browser.

    Args:
        browser (str): Browser type ("chrome", "firefox", "edge").
        headless (bool): Whether to run in headless mode.

    Returns:
        WebDriver: Configured Selenium WebDriver instance.
    """

    # Force headless mode on CI (GitHub Actions)
    if os.getenv("CI"):
        headless = True

    browser = browser.lower()

    # --- Chrome ---
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")

        # Optional: remove --user-data-dir if exists
        if "--user-data-dir" in options.arguments:
            options.arguments.remove("--user-data-dir")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    # --- Firefox ---
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    # --- Edge ---
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    else:
        raise Exception(f"Unsupported browser: {browser}")

    # --- Common settings ---
    driver.set_page_load_timeout(15)
    driver.implicitly_wait(5)
    driver.maximize_window()

    return driver
