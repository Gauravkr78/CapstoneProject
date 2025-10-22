# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from pages.base_page import BasePage
#
# class ProductsPage(BasePage):
#     # Locators
#     PRODUCTS_BTN = (By.XPATH, "//a[@href='/products']")
#     ALL_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'All Products')]")
#     PRODUCT_LIST = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
#     FIRST_VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
#     PRODUCT_NAME = (By.XPATH, "//h2[@class='title text-center' or @class='product-information']//b")
#     PRODUCT_CATEGORY = (By.XPATH, "//p[contains(text(),'Category')]")
#     PRODUCT_PRICE = (By.XPATH, "//span[contains(text(),'Rs.')]")
#     PRODUCT_AVAILABILITY = (By.XPATH, "//b[contains(text(),'Availability')]")
#     PRODUCT_CONDITION = (By.XPATH, "//b[contains(text(),'Condition')]")
#     PRODUCT_BRAND = (By.XPATH, "//b[contains(text(),'Brand')]")
#
#     def open_home_page(self):
#         """Open Automation Exercise home page"""
#         self.driver.get("https://automationexercise.com/")
#         print("🌐 Navigated to Automation Exercise home page")
#
#     def go_to_products_page(self):
#         """Click on 'Products' button"""
#         self.click(self.PRODUCTS_BTN)
#         print("🛍️ Clicked on 'Products' button")
#
#     def verify_all_products_page(self):
#         """Check if 'ALL PRODUCTS' page loaded"""
#         return self.is_visible(self.ALL_PRODUCTS_TITLE)
#
#     def verify_product_list_visible(self):
#         """Check if product list is displayed"""
#         return self.is_visible(self.PRODUCT_LIST)
#
#     def open_first_product(self):
#         """Click on 'View Product' for the first product"""
#         self.click(self.FIRST_VIEW_PRODUCT)
#         print("🔎 Clicked on 'View Product' of first product")
#
#     def verify_product_details(self):
#         """Verify that all product details are visible"""
#         details = {
#             "name": self.is_visible(self.PRODUCT_NAME),
#             "category": self.is_visible(self.PRODUCT_CATEGORY),
#             "price": self.is_visible(self.PRODUCT_PRICE),
#             "availability": self.is_visible(self.PRODUCT_AVAILABILITY),
#             "condition": self.is_visible(self.PRODUCT_CONDITION),
#             "brand": self.is_visible(self.PRODUCT_BRAND)
#         }
#
#         missing = [key for key, visible in details.items() if not visible]
#         if missing:
#             print(f"❌ Missing details: {missing}")
#             return False
#         print("✅ All product details (name, category, price, availability, condition, brand) are visible")
#         return True
