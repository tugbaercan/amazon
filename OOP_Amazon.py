from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait


class BaseFunctions:
    driver = webdriver.Chrome()
    driver.maximize_window()

    def wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_element(locator).click()

    def input(self, locator, value):
        self.wait_element(locator).send_keys(value)

    def get_text(self, locator):
        return self.wait_element(locator).text

    def hover(self, locator):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))).perform()


class AmazonTest(BaseFunctions):

    def __init__(self):

        self.driver.get("https://www.amazon.com/")

        self.click((By.ID, 'nav-link-accountList'))
        self.input((By.ID, 'ap_email'), "test0321@outlook.com.tr")
        self.input((By.ID, 'ap_password'), "testinsider")
        self.click((By.CLASS_NAME, "a-button-input"))

        self.input((By.ID, 'twotabsearchtextbox'), "Samsung")
        self.click((By.CLASS_NAME, 'nav-input'))

        search_text = self.get_text((By.CSS_SELECTOR, '.a-color-state'))
        assert "Samsung", search_text

        self.click((By.CLASS_NAME, 'a-normal'))
        page_number = self.get_text((By.CSS_SELECTOR, '.a-selected'))
        assert "2" == page_number

        self.click((By.CSS_SELECTOR, 'div[data-index="2"] h2 a'))
        wish_list = self.driver.find_element_by_css_selector('#productTitle').text

        self.click((By.ID, 'wishlistButtonStack'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, '.a-icon.a-icon-close'))

        self.get_text((By.CSS_SELECTOR,'#productTitle'))

        self.hover((By.ID, 'nav-link-accountList'))
        time.sleep(2)
        self.click((By.LINK_TEXT, 'Wish List'))
        wish_list_add = self.driver.find_element_by_css_selector('h3').text
        assert wish_list == wish_list_add

        self.click((By.CSS_SELECTOR, '#content-right .a-button-stack .a-link-normal'))
        time.sleep(2)
        product_deleted = self.get_text((By.CSS_SELECTOR, '.a-alert-inline-success'))

        assert 'Deleted' == product_deleted
        self.driver.close()


AmazonTest()
