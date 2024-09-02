from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/add_remove_elements/')

add_element = browser.find_element(By.TAG_NAME, 'button')
for i in range(5):
    add_element.click()

list = browser.find_elements(By.CLASS_NAME, 'added-manually')

print(f'размер списка: {len(list)}')

sleep(5)
