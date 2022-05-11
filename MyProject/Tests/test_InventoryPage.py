import pytest

from Tests.BaseTest import BaseTest
from Locators.Locators import Locators
from Tests.test_LoginPage import TestLogin
from Pages.BasePage import BasePage


@pytest.mark.sanity
class TestInventory(BaseTest):

    def test_login(self):
        log = BasePage.get_logger(self)
        log.info("Logging in")
        TestLogin.test_login(self)
        TestLogin.test_verify_url(self)

    def test_verify_title(self):
        log = BasePage.get_logger(self)
        log.info("Verifying the page title")
        title = self.inventoryPage.get_title(Locators.inventory_page_title)
        assert title == "PRODUCTS"
        log.info("Verified the page title")

    def test_select_least_item(self):
        log = BasePage.get_logger(self)
        log.info("Selecting the least valued item...")
        self.inventoryPage.select_item()
        element = self.inventoryPage.get_element(Locators.shopping_cart_link)
        assert element.is_displayed() == True
        log.info("Clicking on cart button")
        self.inventoryPage.click_on_cart()
