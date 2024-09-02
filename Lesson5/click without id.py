from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

browser = webdriver.Chrome()
browser.get('http://uitestingplayground.com/dynamicid')


button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))


button.click()

sleep(5)
