import pytest
import os
from dotenv import load_dotenv
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class TestLogin:

    @pytest.mark.MDA1C1
    def test_login_valid_credentials(self, driver):
        menu_page = MenuPage(driver)
        login_page = LoginPage(driver)
        catalog_page = CatalogPage(driver)

        username = os.getenv("LOGIN_USERNAME")
        password = os.getenv("LOGIN_PASSWORD")

        menu_page.go_to_login()
        login_page.login(username, password)

        assert catalog_page.wait.until(
            EC.visibility_of_element_located(catalog_page.TITLE_PAGE)
        ), "Catalog page should be displayed after login"

        menu_page.open_menu()

        assert menu_page.wait.until(
            EC.visibility_of_element_located(menu_page.LOGOUT_ITEM)
        ), "Logout item should be visible in menu after login"

    @pytest.mark.MDA1C2
    def test_login_blocked_user(self, driver):
        menu_page = MenuPage(driver)
        login_page = LoginPage(driver)

        username = os.getenv("LOCKED_USERNAME")
        password = os.getenv("LOCKED_PASSWORD")

        menu_page.go_to_login()
        login_page.login(username, password)

        assert login_page.get_password_error_message() == LoginPage.LOCKED_USER_ERROR, \
            "Blocked user should see a locked out error message"

    @pytest.mark.MDA1C3
    def test_login_mandatory_fields(self, driver):
        menu_page = MenuPage(driver)
        login_page = LoginPage(driver)

        menu_page.go_to_login()
        login_page.login()

        assert login_page.get_username_error_message() == LoginPage.MANDATORY_USER_ERROR, \
            "Username field should show a mandatory field error message"
        assert login_page.get_password_error_message() == LoginPage.MANDATORY_PASSWORD_ERROR, \
            "Password field should show a mandatory field error message"