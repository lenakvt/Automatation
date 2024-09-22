from selenium import webdriver
from form_page import FormPage


def test_user_form():
    chromDriver = webdriver.Chrome()

    # Создать экземпляр класса
    form = FormPage(chromDriver)

    # Зайти на сайт
    form.getForm()

    # Заполнить форму значениями
    form.setupForm()

    # Кликнуть на кнопку Submit
    form.submit()

    # Проверить assert, что поле zip code подсвечено красным цветом, и что
    # поля подсвечены зеленым цветом
    assert form.getZipCodeId() == "zip-code", "Поле не подсвечено красным"
    assert form.checkSucsessFields() is True, "Поля не подсвечено зеленым"
    
    chromDriver.quit()


test_user_form()
