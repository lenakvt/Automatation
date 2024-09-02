from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('http://the-internet.herokuapp.com/inputs')

input_element = browser.find_element(By.TAG_NAME, 'input')
input_element.send_keys("1000")
sleep(2)

input_element.clear()
input_element.send_keys("999")
sleep(2)
