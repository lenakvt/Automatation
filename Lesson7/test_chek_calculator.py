from selenium import webdriver
from calc_page import CalcPage


def test_chek_calculator():
    driver = webdriver.Chrome()
    calc = CalcPage(driver)
    # Перейти на сайт
    calc.get_calc()

    # В поле ввода по локатору #delay ввести значение 45
    calc.set_delay("45")

    # Нажать на кнопки 7,+, 8,=
    calc.press_key("7")
    calc.press_key("+")
    calc.press_key("8")
    calc.press_key("=")

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    assert calc.get_result() == "15"

    # Закрыть сайт
    driver.quit()
