from Pages.BasePage import BasePage
from Tests.BaseTest import BaseTest
from Tests.test_LoginPage import TestLogin
import os
import pytest


class TestCheckoutPage(BaseTest):

    @pytest.mark.sanity
    def test_login(self):
        """This function logs into the application"""
        log = BasePage.get_logger(self)
        log.info("Logging in")
        TestLogin.test_login(self)
        TestLogin.test_verify_url(self)

    def test_add_item(self):
        """This function selects least priced item"""
        log = BasePage.get_logger(self)
        log.info("Selecting least price item")
        self.inventoryPage.select_item()
        self.inventoryPage.click_on_cart()

    def test_place_order(self):
        """This function is used to place order for the selected applicaiton"""
        log = BasePage.get_logger(self)
        log.info("Checking out")
        self.cartPage.checkout()
        log.info("Entering details")
        self.checkoutPage.checkout_details(os.getenv("firstname"), os.getenv("lastname"), os.getenv("zipcode"))
        self.checkoutPage.click_on_continue()
        self.checkoutPage.click_on_finish()
        log.info("Verify success message")
        success_msg = self.checkoutPage.get_success_msg()
        assert success_msg == "THANK YOU FOR YOUR ORDER"
