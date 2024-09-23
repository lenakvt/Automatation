from selenium import webdriver
from form_page import FormPage


def test_user_form():
    chromDriver = webdriver.Chrome()

    # Создать экземпляр класса
    form = FormPage(chromDriver)

    # Зайти на сайт
    form.get_form()

    # Заполнить форму значениями
    form.setup_form()

    # Кликнуть на кнопку Submit
    form.submit()

    # Проверить assert, что поле zip code подсвечено красным цветом, и что
    # поля подсвечены зеленым цветом
    assert form.get_zipcode_id() == "zip-code", "Поле не подсвечено красным"
    assert form.check_sucsess_fields() is True, "Поля не подсвечено зеленым"

    chromDriver.quit()
