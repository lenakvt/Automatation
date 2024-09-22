from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, seleniumDriver):
        self.driver = seleniumDriver

    def getShop(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorizeUser(self, username, password):
        self.driver.find_element(
            By.ID, 'user-name').send_keys(username)
        self.driver.find_element(
            By.ID, 'password').send_keys(password)

    def loginClick(self):
        self.driver.find_element(By.ID, "login-button").click()

    def addToCart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def cartClick(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def checkoutClick(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fillData(self, firstName, lastName, postalCode):
        self.driver.find_element(
            By.ID, "first-name").send_keys(firstName)
        self.driver.find_element(
            By.ID, "last-name").send_keys(lastName)
        self.driver.find_element(
            By.ID, "postal-code").send_keys(postalCode)

    def continueClick(self):
        self.driver.find_element(By.ID, "continue").click()

    def readTotalCost(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "div.summary_total_label").text
