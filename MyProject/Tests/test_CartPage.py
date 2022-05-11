import pytest

from Pages.BasePage import BasePage
from Tests.BaseTest import BaseTest
from Tests.test_LoginPage import TestLogin

@pytest.mark.sanity
class TestCartPage(BaseTest):

    def test_login(self):
        log = BasePage.get_logger(self)
        log.info("Logging in")
        TestLogin.test_login(self)
        TestLogin.test_verify_url(self)

    def test_add_item(self):
        log = BasePage.get_logger(self)
        log.info("Selecting least price item")
        self.inventoryPage.select_item()
        self.inventoryPage.click_on_cart()

    def test_cart_page(self):
        log = BasePage.get_logger(self)
        log.info("Verifying the selected item in the cart")
        value = self.cartPage.verify_item()
        assert value == 1
        log.info("Removing the item")
        self.cartPage.remove_item()
        self.cartPage.click_on_continue()
        log.info("Selecting least price item")
        self.inventoryPage.select_item()
        self.inventoryPage.click_on_cart()
        log.info("Checking out")
        self.cartPage.checkout()
