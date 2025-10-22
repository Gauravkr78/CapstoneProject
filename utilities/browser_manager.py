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




# File: utilities/browser_manager.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver(browser="chrome"):
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise Exception(f"Unsupported browser: {browser}")

    # Common settings
    driver.set_page_load_timeout(15)   # Reduced page load timeout
    driver.implicitly_wait(5)          # Reduced implicit wait
    driver.maximize_window()

    return driver
