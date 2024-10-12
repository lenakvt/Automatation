from selenium import webdriver
from calc_page import CalcPage
import allure
from allure_commons.types import Severity

delay = "45"

@allure.title("Проверка калькулятора")
@allure.description("Сложение цифр")
@allure.feature("Read")
@allure.severity(Severity.NORMAL)
def test_chek_calculator():
    driver = webdriver.Chrome()
    calc = CalcPage(driver)

    with allure.step("Получить сайт калькулятор"):
        calc.get_calc()

    with allure.step("В поле ввода по локатору #delay ввести значение 45"):
        calc.set_delay(delay)

    with allure.step("Нажать на кнопки 7,+, 8,="):
        calc.press_key("7")
        calc.press_key("+")
        calc.press_key("8")
        calc.press_key("=")

    with allure.step("Проверьте (assert), что в окне отобразится результат"
                     "\\15 через 45 секунд"):
        assert calc.get_result() == "15"

    with allure.step("Закрыть сайт"):
        driver.quit()
