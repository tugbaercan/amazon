from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.amazon.com/")
wait = WebDriverWait(browser, 10)

#step one
wait.until(EC.element_to_be_clickable((By.ID, 'nav-link-accountList'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'ap_email'))).send_keys("duvorowu@greentech5.com")
wait.until(EC.element_to_be_clickable((By.ID, 'ap_password'))).send_keys("test0123")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "a-button-input"))).click()

#step two
wait.until(EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))).send_keys("Samsung")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'nav-input'))).click()

#step three
text = browser.find_element_by_class_name('a-color-state').text
assert "Samsung" in text

#step four
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'a-normal'))).click()
second_page = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'a-selected'))).text
assert second_page, '2'

#step five
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-index="2"] h2 a'))).click()

#steep six
wait.until(EC.element_to_be_clickable((By.ID, 'wishlistButtonStack'))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.a-icon.a-icon-close'))).click()
wish_list = wait.until(EC.element_to_be_clickable((By.ID, 'productTitle'))).text

#step seven
add = wait.until(EC.element_to_be_clickable((By.ID, 'nav-link-accountList')))
Hover = ActionChains(browser).move_to_element(add)
Hover.perform()

#step eight
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Wish List'))).click()
assert wish_list, browser.find_element_by_css_selector('h3').text

#step nine
wait.until(EC.element_to_be_clickable((By.ID, 'a-autoid-7'))).click()

#step ten
clear = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.a-alert-inline-success .a-alert-content'))).text
assert clear, 'Deleted'

time.sleep(2)
browser.close()
