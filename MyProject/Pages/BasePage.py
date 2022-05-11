import inspect

from selenium.webdriver.common.by import By
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_text(self,by_locator):
        return self.driver.find_element(by=By.XPATH, value=by_locator).text

    def get_element(self,by_locator):
        element = self.driver.find_element(by=By.XPATH, value=by_locator)
        return element

    def click_element(self, by_locator):
        self.driver.find_element(by=By.XPATH, value=by_locator).click()

    def get_url(self):
        return self.driver.current_url

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s %(message)s ")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
