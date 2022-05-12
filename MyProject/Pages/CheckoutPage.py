from selenium.webdriver.common.by import By

from Locators.Locators import Locators
from Pages.BasePage import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.firstname_path = Locators.firstname_path
        self.lastname_path = Locators.lastname_path
        self.postal_code = Locators.postal_code
        self.finish_btn = Locators.finish_btn
        self.continue_btn = Locators.continue_btn
        self.message_heading = Locators.message_heading

    def checkout_details(self, firstname, lastname, zipcode):
        """
        This function enters checkout details in input fields
        :param: firstname, lastname, zipcode
        """
        log = self.get_logger()
        log.info("Entering firstname")
        self.driver.find_element(by=By.XPATH, value=self.firstname_path).send_keys(firstname)
        log.info("Entering lastname")
        self.driver.find_element(by=By.XPATH, value=self.lastname_path).send_keys(lastname)
        log.info("Entering Zipcode")
        self.driver.find_element(by=By.XPATH, value=self.postal_code).send_keys(zipcode)

    def click_on_continue(self):
        """
        This function clicks on continue button
        """
        log = self.get_logger()
        log.info("Clicking on continue button")
        self.click_element(self.continue_btn)

    def click_on_finish(self):
        """
        This function clicks on finish button
        """
        log = self.get_logger()
        log.info("Clicking on finish button")
        self.click_element(self.finish_btn)

    def get_success_msg(self):
        """
        This function returns success message text
        :return success message text
        """
        log = self.get_logger()
        log.info("Reading success message")
        return self.get_text(self.message_heading)

