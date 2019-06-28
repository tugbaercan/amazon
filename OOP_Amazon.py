from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait


class BaseFunction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    TEXT = ""

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def input(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(value)

    def get_text(self, locator):
        self.TEXT == self.driver.find_element_by_css_selector(locator).text

    def Assert(self, value1, value2):
        assert value1, value2

    def hover(self, locator):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 10)
                                                  .until(EC.element_to_be_clickable(locator))).perform()


class AmazonTest(BaseFunction):

    def __init__(self):

        self.driver.get("https://www.amazon.com/")

        self.click((By.ID, 'nav-link-accountList'))
        self.input((By.ID, 'ap_email'), "umut.yasin.colak@hotmail.com")
        self.input((By.ID, 'ap_password'), "Umut0127-")
        self.click((By.CLASS_NAME, "a-button-input"))

        self.input((By.ID, 'twotabsearchtextbox'), "Samsung")
        self.click((By.CLASS_NAME, 'nav-input'))

        self.get_text('.a-color-state')
        self.Assert("Samsung", self.TEXT)

        self.click((By.CLASS_NAME, 'a-normal'))
        self.get_text('.a-selected')
        self.Assert("2", self.TEXT)

        self.click((By.CSS_SELECTOR, 'div[data-index="2"] h2 a'))

        self.click((By.ID, 'wishlistButtonStack'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, '.a-icon.a-icon-close'))
        self.get_text('#productTitle')

        self.hover((By.ID, 'nav-link-accountList'))

        self.click((By.LINK_TEXT, 'Wish List'))
        a = self.driver.find_element_by_css_selector('h3').text
        self.Assert(a, self.TEXT)

        self.click((By.ID, 'a-autoid-7'))
        time.sleep(2)
        self.get_text('.a-alert-inline-success')

        self.Assert('Deleted', self.TEXT)
        self.driver.close()

AmazonTest()
