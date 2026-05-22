import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv

load_dotenv()


def dismiss_compatibility_alert(driver):
    try:
        wait = WebDriverWait(driver, 10)
        ok_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, "//android.widget.Button[@text=\"Don't Show Again\"]")
        ))
        ok_button.click()
    except Exception:
        pass


@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.saucelabs.mydemoapp.android"
    options.app_activity = ".view.activities.SplashActivity"
    options.device_name = "emulator-5554"
    options.app = os.getenv("APK_PATH")

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    dismiss_compatibility_alert(driver)
    yield driver
    driver.quit()