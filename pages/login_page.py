from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")
    USERNAME_ERROR_MESSAGE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV")
    PASSWORD_ERROR_MESSAGE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")

    LOCKED_USER_ERROR = "Sorry this user has been locked out."
    MANDATORY_USER_ERROR = "Username is required"
    MANDATORY_PASSWORD_ERROR = "Enter Password"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def tap_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username=None, password=None):
        if username:
            self.fill_username(username)
        if password:
            self.fill_password(password)
        self.tap_login_button()

    def get_username_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_ERROR_MESSAGE)
        ).text

    def get_password_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_ERROR_MESSAGE)
        ).text