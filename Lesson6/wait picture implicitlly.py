from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Перейти на сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Дождаться загрузки всех картинок
driver.implicitly_wait(20)

# Получить значение атрибута src 3-й картинки и вывести в консоль
pictures = driver.find_element(By.ID, "image-container")
src = pictures.find_element(By.ID, "award").get_attribute("src")

print(src)
driver.quit()
