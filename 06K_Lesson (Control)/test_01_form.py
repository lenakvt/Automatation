from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Перейти на сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

# Заполнить форму значениями
first_name = driver.find_element(
    By.CSS_SELECTOR, "[name=first-name]").send_keys("Иван")
last_name = driver.find_element(
    By.CSS_SELECTOR, "[name=last-name]").send_keys("Петров")
address = driver.find_element(
    By.CSS_SELECTOR, "[name=address]").send_keys("Ленина, 55-3")
email = driver.find_element(
    By.CSS_SELECTOR, "[name=e-mail]").send_keys("test@skypro.com")
phone_number = driver.find_element(
    By.CSS_SELECTOR, "[name=phone]").send_keys("+7985899998787")
city = driver.find_element(
    By.CSS_SELECTOR, "[name=city]").send_keys("Москва")
country = driver.find_element(
    By.CSS_SELECTOR, "[name=country]").send_keys("Россия")
job_position = driver.find_element(
    By.CSS_SELECTOR, "[name=job-position]").send_keys("QA")
company = driver.find_element(
    By.CSS_SELECTOR, "[name=company]").send_keys("SkyPro")

# Кликнуть на кнопку Submit
button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")))

button_submit.click()

# Проверить assert, что поле zip code подсвечено красным цветом
alert_danger = driver.find_element(
    By.CSS_SELECTOR, "#zip-code.alert.py-2.alert-danger")

assert alert_danger.get_attribute(
    "id") == "zip-code", "Поле не подсвечено красным"

# Проверьте assert, что остальные поля подсвечены зеленым
assert len(driver.find_elements(By.CLASS_NAME, "alert-success")
           ) == 9, "Количество полей, подсвеченных зеленым отличается"

# Закрыть сайт
driver.quit()
