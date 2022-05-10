from Tests.BaseTest import BaseTest
from Locators.Locators import Locators
from Tests.test_LoginPage import TestLogin


class TestInventory(BaseTest):

    def test_login(self):
        TestLogin.test_login(self)
        TestLogin.test_verify_url(self)

    def test_verify_title(self):
        title = self.inventoryPage.get_title(Locators.inventory_page_title)
        assert title == "PRODUCTS"

    def test_select_least_item(self):
        self.inventoryPage.select_item()
        element = self.inventoryPage.get_element(Locators.shopping_cart_link)
        assert element.is_displayed() == True
        self.inventoryPage.click_on_cart()
