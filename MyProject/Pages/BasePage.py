from selenium.webdriver.common.by import By


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