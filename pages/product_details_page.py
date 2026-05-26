from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage:

    INCREASE_ITEM_QUANTITY_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Increase item quantity")
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
    CART_ICON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def tap_increase_item_quantity_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.INCREASE_ITEM_QUANTITY_BUTTON)
        ).click()

    def tap_add_to_cart_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()


