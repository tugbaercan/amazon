from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.amazon.com/")

time.sleep(2)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'nav-link-accountList'))).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'ap_email'))).send_keys("vusewop@hostguru.info")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'ap_password'))).send_keys("123456tt")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "a-button-input"))).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))).send_keys("Samsung")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'nav-input'))).click()


text = browser.find_element_by_class_name('a-color-state').text
assert "Samsung" in text

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'a-normal'))).click()

second_page = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'a-selected'))).text
assert second_page, '2'

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-index="2"] h2 a'))).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'wishlistButtonStack'))).click()

time.sleep(1)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.a-icon.a-icon-close'))).click()
wish_list = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'productTitle'))).text

add = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'nav-link-accountList')))
Hover = ActionChains(browser).move_to_element(add)
Hover.perform()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Wish List'))).click()

assert wish_list, browser.find_element_by_css_selector('h3').text


WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'a-autoid-7'))).click()

clear = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.a-alert-inline-success .a-alert-content'))).text
assert clear, 'Deleted'

time.sleep(2)
browser.close()