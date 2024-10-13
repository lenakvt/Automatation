from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class CalcPage:
    def __init__(self, seleniumDriver):
        self.driver = seleniumDriver

    @allure.step("получение сайта по url")
    def get_calc(self):
        self.driver.get(
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("установка задержки")
    def set_delay(self, time: str):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(time)

    @allure.step("нажатие кнопки")
    def press_key(self, key: str):
        self.driver.find_element(By.XPATH, f'//span[text()="{key}"]').click()

    @allure.step("получить результат")
    def get_result(self) -> str:
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        return self.driver.find_element(By.CLASS_NAME, "screen").text
