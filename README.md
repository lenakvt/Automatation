# Automatation
## Задачи курса автоматизации на Python

### Запуск тестов
```
pytest
```
***конфигурирование запуска тестов через pytest.ini***
***по умолчанию, для скорости, запускается только последний урок***

### Запуск тестов с отчетами allure
```
pytest --alluredir=./Lesson10/allure_report
```
### Установка сервера allure на windows
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install allure
```
***проверка версии allure***
```
allure --version
```