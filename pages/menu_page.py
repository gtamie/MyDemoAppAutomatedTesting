from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    MENU_ICON = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    LOGIN_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    LOGOUT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_ICON)).click()

    def go_to_login(self):
        self.open_menu()
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_ITEM)).click()