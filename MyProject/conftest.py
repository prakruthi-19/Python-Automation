import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.ie.service import Service
import os
from Pages.LoginPage import LoginPage
from Pages.InventoryPage import InventoryPage
from Pages.CheckoutPage import CheckoutPage
from Pages.CartPage import CartPage


driver = None
@pytest.fixture(scope="class")
def init_driver(request):
    global driver
    browser = os.getenv("browser")
    if browser.casefold() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser.casefold() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser.casefold() == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
    elif browser.casefold() == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = driver
    request.cls.loginPage = LoginPage(driver)
    request.cls.inventoryPage = InventoryPage(driver)
    request.cls.checkoutPage = CheckoutPage(driver)
    request.cls.cartPage = CartPage(driver)
    yield
    driver.close()
    driver.quit()
