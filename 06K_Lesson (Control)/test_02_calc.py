from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Перейти на сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

# Вполе ввода удалить значение 5
delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()

# В поле ввода по локатору #delay ввести значение 45
delay_input.send_keys("45")

# Нажать на кнопки 7,+, 8,=
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
result = WebDriverWait(driver, 46).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

result_text = driver.find_element(By.CLASS_NAME, "screen").text
assert result_text == "15"

# Закрыть сайт
driver.quit()
