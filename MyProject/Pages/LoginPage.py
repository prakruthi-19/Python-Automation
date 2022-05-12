from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_path = Locators.username_xpath
        self.password_path = Locators.password_xpath
        self.login_btn = Locators.login_btn_xpath

    def enter_url(self, url):
        """
        This function is used to launch the website
        :param url: website url
        """
        log = self.get_logger()
        log.info("Entering url")
        self.driver.get(url)
        log.info("maximizing window")
        self.driver.maximize_window()

    def enter_username(self, username):
        """
        This function enters username value in the input field
        :param: username
        """
        log = self.get_logger()
        log.info("Entering username")
        self.driver.find_element(by=By.XPATH, value=self.username_path).send_keys(username)

    def enter_password(self, password):
        """
        This function enters username value in the input field
        :param password:
        """
        log = self.get_logger()
        log.info("Entering Password")
        self.driver.find_element(by=By.XPATH, value=self.password_path).send_keys(password)

    def click_login(self):
        """This function clicks on login button"""
        log = self.get_logger()
        log.info("Clicking on login button")
        self.click_element(self.login_btn)

    def get_page_url(self):
        """
        This function returns the page url
        :return: url
        """
        log = self.get_logger()
        log.info("getting page url value")
        return self.get_url()
