from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
browser.get('http://the-internet.herokuapp.com/login')

input_username = browser.find_element(By.ID, 'username').send_keys("tomsmith")

input_password = browser.find_element(By.ID, 'password').send_keys("SuperSecretPassword!")

sleep(2)
button_submit = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.TAG_NAME, "button")))

button_submit.click()
