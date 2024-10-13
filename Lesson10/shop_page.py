from selenium.webdriver.common.by import By
import allure


class ShopPage:
    def __init__(self, seleniumDriver):
        self.driver = seleniumDriver

    @allure.step("получение сайта по url")
    def get_shop(self):
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("авторизация пользователя")
    def authorize_user(self, username: str, password: str):
        self.driver.find_element(
            By.ID, 'user-name').send_keys(username)
        self.driver.find_element(
            By.ID, 'password').send_keys(password)

    @allure.step("click по кнопке login")
    def login_click(self):
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("добавить в корзину")
    def add_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("click на корзине")
    def cart_click(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    @allure.step("click на получении заказа")
    def checkout_click(self):
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("заполнить поля формы")
    def fill_data(self, firstName: str, lastName: str, postalCode: str):
        self.driver.find_element(
            By.ID, "first-name").send_keys(firstName)
        self.driver.find_element(
            By.ID, "last-name").send_keys(lastName)
        self.driver.find_element(
            By.ID, "postal-code").send_keys(postalCode)

    @allure.step("click на кнопке продожить")
    def continue_click(self):
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("получить общую стоимость товаров")
    def read_total_cost(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "div.summary_total_label").text
