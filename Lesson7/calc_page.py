from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CalcPage:

    def __init__(self, seleniumDriver):
        self.driver = seleniumDriver

    def get_calc(self):
        self.driver.get(
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, time):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(time)

    def press_key(self, key):
        self.driver.find_element(By.XPATH, f'//span[text()="{key}"]').click()

    def get_result(self):
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        return self.driver.find_element(By.CLASS_NAME, "screen").text
