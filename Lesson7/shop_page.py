from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, seleniumDriver):
        self.driver = seleniumDriver

    def get_shop(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorize_user(self, username, password):
        self.driver.find_element(
            By.ID, 'user-name').send_keys(username)
        self.driver.find_element(
            By.ID, 'password').send_keys(password)

    def login_click(self):
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def cart_click(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def checkout_click(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_data(self, firstName, lastName, postalCode):
        self.driver.find_element(
            By.ID, "first-name").send_keys(firstName)
        self.driver.find_element(
            By.ID, "last-name").send_keys(lastName)
        self.driver.find_element(
            By.ID, "postal-code").send_keys(postalCode)

    def continue_click(self):
        self.driver.find_element(By.ID, "continue").click()

    def read_total_cost(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "div.summary_total_label").text
