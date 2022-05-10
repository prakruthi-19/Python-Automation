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
        item_name = InventoryPage.item_name
        name = self.driver.find_elements(by=By.CLASS_NAME, value=self.items_name)[0].text
        if item_name == name:
            flag = 1
        else:
            flag = 0
        return flag

    def remove_item(self):
        self.click_element(Locators.remove_btn_path)

    def checkout(self):
        self.click_element(Locators.checkout_btn_path)

    def click_on_continue(self):
        self.click_element(Locators.continue_btn_path)