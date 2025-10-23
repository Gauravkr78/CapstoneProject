# pages/scroll_zoom_page.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class ScrollZoomPage:
    def __init__(self, browser="chrome"):
        """Initialize Chrome or Edge browser"""
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError("Browser must be 'chrome' or 'edge'")

        self.driver.maximize_window()
        print(f"✅ Browser '{browser}' launched successfully.")

    def open_website(self, url):
        """Open a website"""
        print(f"🌐 Opening website: {url}")
        self.driver.get(url)
        time.sleep(3)

    def scroll_down(self, pixels=1000):
        """Scroll down"""
        print(f"⬇️ Scrolling down {pixels} pixels...")
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(2)

    def scroll_up(self, pixels=1000):
        """Scroll up"""
        print(f"⬆️ Scrolling up {pixels} pixels...")
        self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
        time.sleep(2)

    def scroll_to_bottom(self):
        """Scroll to bottom of the page"""
        print("📜 Scrolling to bottom of page...")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def zoom_in(self, percentage=150):
        """Zoom in (default 150%)"""
        print(f"🔎 Zooming in to {percentage}%...")
        self.driver.execute_script(f"document.body.style.zoom='{percentage}%';")
        time.sleep(2)

    def zoom_out(self, percentage=80):
        """Zoom out (default 80%)"""
        print(f"🔍 Zooming out to {percentage}%...")
        self.driver.execute_script(f"document.body.style.zoom='{percentage}%';")
        time.sleep(2)

    def reset_zoom(self):
        """Reset zoom to 100%"""
        print("🔁 Resetting zoom to 100%...")
        self.driver.execute_script("document.body.style.zoom='100%';")
        time.sleep(2)

    def close_browser(self):
        """Close the browser"""
        print("🧹 Closing browser...")
        time.sleep(2)
        self.driver.quit()
        print("✅ Browser closed successfully.")
