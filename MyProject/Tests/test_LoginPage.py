import pytest
from dotenv import load_dotenv
import os
from Tests.BaseTest import BaseTest
from Pages.BasePage import BasePage
load_dotenv()


@pytest.mark.regression
class TestLogin(BaseTest):
    def test_login(self):
        log = BasePage.get_logger(self)
        log.info("Reading url from env file")
        self.loginPage.enter_url(os.getenv("url"))
        log.info("Reading username from env file")
        self.loginPage.enter_username(os.getenv("user"))
        log.info("Reading password from env file")
        self.loginPage.enter_password(os.getenv("pass"))
        self.loginPage.click_login()
        log.info("Login successful")

    def test_verify_url(self):
        log = BasePage.get_logger(self)
        current_url = self.loginPage.get_page_url()
        log.info("asserting the url value")
        assert current_url == "https://www.saucedemo.com/inventory.html"
        log.info("Verified the page url after login")

