from selenium import webdriver
from calc_page import CalcPage


def test_chek_calculator():
    driver = webdriver.Chrome()
    calc = CalcPage(driver)
    # Перейти на сайт
    calc.getCalc()

    # В поле ввода по локатору #delay ввести значение 45
    calc.setDelay("45")

    # Нажать на кнопки 7,+, 8,=
    calc.pressKey("7")
    calc.pressKey("+")
    calc.pressKey("8")
    calc.pressKey("=")

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    assert calc.getResult() == "15"

    # Закрыть сайт
    driver.quit()


test_chek_calculator()
