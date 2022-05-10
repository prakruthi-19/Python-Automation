import pytest
from dotenv import load_dotenv
import os
from Tests.BaseTest import BaseTest
load_dotenv()


@pytest.mark.regression
class TestLogin(BaseTest):
    def test_login(self):
        self.loginPage.enter_url(os.getenv("url"))
        self.loginPage.enter_username(os.getenv("user"))
        self.loginPage.enter_password(os.getenv("pass"))
        self.loginPage.click_login()

    def test_verify_url(self):
        current_url = self.loginPage.get_page_url()
        assert current_url == "https://www.saucedemo.com/inventory.html"

