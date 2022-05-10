import pytest
from Tests.BaseTest import BaseTest
from Tests.test_LoginPage import TestLogin


class TestCartPage(BaseTest):

    def test_login(self):
        TestLogin.test_login(self)
        TestLogin.test_verify_url(self)

    def test_add_item(self):
        self.inventoryPage.select_item()
        self.inventoryPage.click_on_cart()

    @pytest.mark.sanity
    def test_cart_page(self):
        value = self.cartPage.verify_item()
        assert value == 1
        self.cartPage.remove_item()
        self.cartPage.click_on_continue()
        self.inventoryPage.select_item()
        self.inventoryPage.click_on_cart()
        self.cartPage.checkout()
