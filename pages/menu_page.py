from appium.webdriver.common.appiumby import AppiumBy


class MenuPage:

    MENU_ICON = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    LOGIN_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        self.driver.find_element(*self.MENU_ICON).click()

    def go_to_login(self):
        self.open_menu()
        self.driver.find_element(*self.LOGIN_ITEM).click()