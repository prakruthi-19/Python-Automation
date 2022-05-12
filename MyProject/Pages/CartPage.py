from selenium.webdriver.common.by import By

from Locators.Locators import Locators
from Pages.InventoryPage import InventoryPage
from Pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.items_name = Locators.items_name
        self.remove_btn_path = Locators.remove_btn_path
        self.checkout_btn_path = Locators.checkout_btn_path

    def verify_item(self):
        """
        This function verifies the item name added to the cart
        :return: returns 1 if the name matches
        """
        log = self.get_logger()
        item_name = InventoryPage.item_name
        log.info("Getting the item name")
        name = self.driver.find_elements(by=By.CLASS_NAME, value=self.items_name)[0].text
        if item_name == name:
            flag = 1
        else:
            flag = 0
        return flag

    def remove_item(self):
        """
        This function clicks on remove button
        """
        log = self.get_logger()
        log.info("Clicking on remove button")
        self.click_element(Locators.remove_btn_path)
        log.info("Clicked on button")

    def checkout(self):
        """
        This function clicks on checkout button
        """
        log = self.get_logger()
        log.info("Clicking on checkout button")
        self.click_element(Locators.checkout_btn_path)
        log.info("Clicked on checkout button")

    def click_on_continue(self):
        """
        This function clicks on continue button
        """
        log = self.get_logger()
        log.info("Clicking on continue button")
        self.click_element(Locators.continue_btn_path)
        log.info("Clicked on continue button")
