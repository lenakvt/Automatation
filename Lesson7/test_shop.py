from selenium import webdriver
from shop_page import ShopPage


def test_shop():
    driver = webdriver.Chrome()
# Создать экземпляр класса
    shop = ShopPage(driver)

    # Перейти на сайт
    shop.get_shop()

    # Авторизоваться как пользователь standard_user
    shop.authorize_user("standard_user", "secret_sauce")

    # Нажать на кнопку login
    shop.login_click()

    # Добавить товары в корзину
    shop.add_to_cart()

    # Перейти в корзину
    shop.cart_click()

    # Нажать на кнопку Checkout
    shop.checkout_click()

    # Заполнить форму своими данными
    shop.fill_data("Elena", "KIlovataya", "194223")

    # Нажать кнопку Continue
    shop.continue_click()

    # Прочитайте со страницы итоговую стоимость (Total)
    assert shop.read_total_cost() == "Total: $58.29"

    # Закрыть сайт
    driver.quit()
