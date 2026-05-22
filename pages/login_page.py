from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:

    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")

    def __init__(self, driver):
        self.driver = driver

    def fill_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def tap_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.tap_login_button()