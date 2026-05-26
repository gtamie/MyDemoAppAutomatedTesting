from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:

    TITLE_PAGE = (AppiumBy.ACCESSIBILITY_ID, "title")
    PRODUCT_PHOTO = (AppiumBy.ACCESSIBILITY_ID, "Product Image")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_product_photo(self, index=0):
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_PHOTO))
        self.driver.find_elements(*self.PRODUCT_PHOTO)[index].click()