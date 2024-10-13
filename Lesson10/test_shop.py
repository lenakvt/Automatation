from selenium import webdriver
from shop_page import ShopPage
import allure
from allure_commons.types import Severity


@allure.title("Проверка магазина")
@allure.description("Покупка товара провека рассчета цены")
@allure.feature("Read")
@allure.severity(Severity.NORMAL)
def test_shop():
    driver = webdriver.Chrome()
    
    with allure.step("Создать экземпляр класса ShopPage"):
        shop = ShopPage(driver)

    with allure.step("Перейти на сайт"):
        shop.get_shop()

    with allure.step("Авторизоваться как пользователь standard_user"):
        shop.authorize_user("standard_user", "secret_sauce")

    with allure.step("Нажать на кнопку login"):
        shop.login_click()

    with allure.step("Добавить товары в корзину"):
        shop.add_to_cart()

    with allure.step("Перейти в корзину"):
        shop.cart_click()

    with allure.step("Нажать на кнопку Checkout"):
        shop.checkout_click()

    with allure.step("Заполнить форму своими данными"):
        shop.fill_data("Elena", "KIlovataya", "194223")

    with allure.step("Нажать кнопку Continue"):
        shop.continue_click()

    with allure.step("Прочитайте со страницы итоговую стоимость (Total)"):
        assert shop.read_total_cost() == "Total: $58.29"

    with allure.step("Закрыть сайт"):
        driver.quit()
