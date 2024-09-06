from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)

# Перейти на сайт
driver.get('http://uitestingplayground.com/textinput')

# Указать в поле ввода текст SkyPro
name_button = driver.find_element(
    By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

# Получить текст кнопки и вывести в консоль
print(driver.find_element(By.ID, 'updatingButton').text)

driver.quit()
