from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

# Перейти на сайт
driver.get('http://uitestingplayground.com/ajax')

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получить текст из зеленой плашки
divcontent = driver.find_element(By.CSS_SELECTOR, "#content")
txt = divcontent.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Вывести текст в консоль
print(txt)

driver.quit()
