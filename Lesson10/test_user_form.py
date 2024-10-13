from selenium import webdriver
from form_page import FormPage
import allure
from allure_commons.types import Severity


@allure.title("Проверка веб формы")
@allure.description("Заполнение всех поле веб формы")
@allure.feature("Read")
@allure.severity(Severity.NORMAL)
def test_user_form():
    chromDriver = webdriver.Chrome()

    with allure.step("Создать экземпляр класса"):
        form = FormPage(chromDriver)

    with allure.step("Зайти на сайт"):
        form.get_form()

    with allure.step("Заполнить форму значениями"):
        form.setup_form()

    with allure.step("Кликнуть на кнопку Submit"):
        form.submit()

    with allure.step("""Проверить assert, что поле zip code подсвечено
                     красным цветом, и что поля подсвечены зеленым цветом"""):

        assert form.get_zipcode_id() == "zip-code", """Поле не подсвечено
        красным"""
        assert form.check_sucsess_fields() is True, """Поля не подсвечено 
        зеленым"""

    with allure.step("Закрыть сайт"):
        chromDriver.quit()
