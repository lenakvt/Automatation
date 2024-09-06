from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Перейти на сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Дождаться загрузки всех картинок
pictures = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[id=landscape]")))

# Получить значение атрибута src 3-й картинки и вывести в консольF
src = driver.find_element(By.ID, "award").get_attribute("src")

print(src)
driver.quit()
