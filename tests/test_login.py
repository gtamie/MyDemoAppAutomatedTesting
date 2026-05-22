import pytest
import os
from dotenv import load_dotenv
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class TestLogin:

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