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
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_username(self, username):
        self.driver.find_element(by=By.XPATH, value=self.username_path).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by=By.XPATH, value=self.password_path).send_keys(password)

    def click_login(self):
        self.click_element(self.login_btn)

    def get_page_url(self):
        return self.get_url()
