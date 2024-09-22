from selenium import webdriver
from shop_page import ShopPage


def test_shop():
    driver = webdriver.Chrome()
# Создать экземпляр класса
    shop = ShopPage(driver)

    # Перейти на сайт
    shop.getShop()

    # Авторизоваться как пользователь standard_user
    shop.authorizeUser("standard_user", "secret_sauce")

    # Нажать на кнопку login
    shop.loginClick()

    # Добавить товары в корзину
    shop.addToCart()

    # Перейти в корзину
    shop.cartClick()

    # Нажать на кнопку Checkout
    shop.checkoutClick()

    # Заполнить форму своими данными
    shop.fillData("Elena", "KIlovataya", "194223")

    # Нажать кнопку Continue
    shop.continueClick()

    # Прочитайте со страницы итоговую стоимость (Total)
    assert shop.readTotalCost() == "Total: $58.29"

    # Закрыть сайт
    driver.quit()


test_shop()
