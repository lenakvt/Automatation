from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

# Перейти на сайт
driver.get('https://www.saucedemo.com/')

# Авторизоваться как пользователь standard_user
input_username = driver.find_element(
    By.ID, 'user-name').send_keys("standard_user")
input_password = driver.find_element(
    By.ID, 'password').send_keys("secret_sauce")

# Нажать на кнопку login
driver.find_element(By.ID, "login-button").click()

# Добавить товары в корзину
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# Перейти в корзину
driver.find_element(By.ID, "shopping_cart_container").click()

# Нажать на кнопку Checkout
driver.find_element(By.ID, "checkout").click()

# Заполнить форму своими данными
first_name = driver.find_element(
    By.ID, "first-name").send_keys("Елена")
last_name = driver.find_element(
    By.ID, "last-name").send_keys("Киловатая")
portal_code = driver.find_element(
    By.ID, "postal-code").send_keys("194223")

# Нажать кнопку Continue
driver.find_element(By.ID, "continue").click()

# Прочитайте со страницы итоговую стоимость (Total)
total_cost = driver.find_element(
    By.CSS_SELECTOR, "div.summary_total_label").text

# Закрыть сайт
driver.quit()

# Проверить, что итоговая сумма равна $58.29
assert total_cost == "Total: $58.29"
