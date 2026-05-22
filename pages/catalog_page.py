from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:

    TITLE_PAGE = (AppiumBy.ACCESSIBILITY_ID, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)