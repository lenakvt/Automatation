from authentication_api import AuthenticationApi
from company_api import CompanyApi
from employee_api import EmployeeApi

baseUrl = "https://x-clients-be.onrender.com"
token = ""
company_id = ""


# Создание новой компании
def test_create_company():
    authApi = AuthenticationApi(baseUrl)
    global token
    token = authApi.get_token()
    companyApi = CompanyApi(baseUrl)
    global company_id
    company_id = companyApi.create_company(
        token, "Lenas Company", "Comodities")
    companyApi = CompanyApi(baseUrl)
    company = companyApi.get_company(company_id)
    assert company["id"] == company_id


# Создание нового сотрудника
def test_create_employee():
    employeeApi = EmployeeApi(baseUrl)
    employee = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "middleName": "Petrovich",
        "companyId": company_id,
        "email": "ivan.ivanov@gmail.com",
        "url": "none",
        "phone": "+1333444555",
        "birthdate": "2000-09-28",
        "isActive": True
    }

    employee_id = employeeApi.create_employee(token, employee)
    assert type(employee_id) is int


# Получение данных сотрудника
def test_get_employee():
    employeeApi = EmployeeApi(baseUrl)
    employee = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "middleName": "Petrovich",
        "companyId": company_id,
        "email": "ivan.ivanov@gmail.com",
        "url": "none",
        "phone": "+1333444555",
        "birthdate": "2000-09-28",
        "isActive": True
    }

    employee_id = employeeApi.create_employee(token, employee)

    new_employee = employeeApi.get_employee(employee_id)

    assert new_employee["firstName"] == employee["firstName"]
    assert new_employee["lastName"] == employee["lastName"]
    assert new_employee["middleName"] == employee["middleName"]
    assert new_employee["companyId"] == employee["companyId"]
    assert new_employee["email"] == employee["email"]
    assert new_employee["avatar_url"] == employee["url"]
    assert new_employee["phone"] == employee["phone"]
    assert new_employee["birthdate"] == employee["birthdate"]
    assert new_employee["isActive"] == employee["isActive"]


# Изменение данных сотрудника
def test_update_employee():
    employeeApi = EmployeeApi(baseUrl)
    employee = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "middleName": "Petrovich",
        "companyId": company_id,
        "email": "ivan.ivanov@gmail.com",
        "url": "none",
        "phone": "+1333444555",
        "birthdate": "2000-09-28",
        "isActive": True
    }

    updated_employee = {
        "lastName": "Sidorov",
        "email": "sidorov@gmail.com",
        "url": "yandex.ru",
        "phone": "+44333444555",
        "isActive": False
    }

    employee_id = employeeApi.create_employee(token, employee)

    employeeApi.update_employee(token, employee_id, updated_employee)

    new_employee = employeeApi.get_employee(employee_id)

    assert new_employee["firstName"] == employee["firstName"]
    assert new_employee["lastName"] == updated_employee["lastName"]
    assert new_employee["middleName"] == employee["middleName"]
    assert new_employee["companyId"] == employee["companyId"]
    assert new_employee["email"] == updated_employee["email"]
    assert new_employee["avatar_url"] == updated_employee["url"]
    assert new_employee["phone"] == updated_employee["phone"]
    assert new_employee["birthdate"] == employee["birthdate"]
    assert new_employee["isActive"] == updated_employee["isActive"]


def test_check_required_fields():
    employeeApi = EmployeeApi(baseUrl)
    employee = {
        "firstName": "",
        "lastName": "",
        "middleName": "none",
        "companyId": "",
        "email": "ivan.ivanov@gmail.com",
        "url": "none",
        "phone": "",
        "birthdate": "",
        "isActive": "none"
    }

    employee_responce = employeeApi.create_employee(token, employee)
    assert employee_responce['statusCode'] == 400
    assert employee_responce['message'][0] == 'firstName should not be empty'
    assert employee_responce['message'][1] == 'lastName should not be empty'
    assert employee_responce['message'][2] == 'companyId must be an integer number'


def test_check_token():
    employeeApi = EmployeeApi(baseUrl)
    employee = {
        "firstName": "",
        "lastName": "",
        "middleName": "none",
        "companyId": "",
        "email": "ivan.ivanov@gmail.com",
        "url": "none",
        "phone": "",
        "birthdate": "",
        "isActive": "none"
    }

    employee_responce = employeeApi.create_employee("", employee)
    assert employee_responce['statusCode'] == 401


def test_check_body():
    employeeApi = EmployeeApi(baseUrl)
    employee = {

    }

    employee_responce = employeeApi.create_employee(token, employee)
    assert employee_responce['statusCode'] == 500

