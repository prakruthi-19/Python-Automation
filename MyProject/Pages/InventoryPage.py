from Locators.Locators import Locators
from Pages.BasePage import BasePage


class InventoryPage(BasePage):

    item_name = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.items_price = Locators.items_price
        self.add_to_cart_path = Locators.add_to_cart
        self.items_name = Locators.items_name
        self.filter_low_high=Locators.filter_low_high
        self.shopping_cart_link=Locators.shopping_cart_link

    def select_item(self):
        self.click_element(self.filter_low_high)
        add_to_cart = self.driver.find_elements_by_xpath(self.add_to_cart_path)
        item_name_list = self.driver.find_elements_by_class_name(self.items_name)
        add_to_cart[0].click()
        InventoryPage.item_name = item_name_list[0].text

    def click_on_cart(self):
        self.click_element(self.shopping_cart_link)

    def get_title(self, by_locator):
        return self.get_text(by_locator)

