import requests


class EmployeeApi:
    # Инициализация
    def __init__(self, url):
        self.url = url

    # Получить сотрудника по ID
    def get_employee(self, id, params_to_add=None):
        resp = requests.get(self.url + '/employee/' +
                            str(id), params=params_to_add)
        return resp.json()

    # Добавить сотрудника:
    def create_employee(self, token, employee):
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=my_headers)
        return resp.json()["id"]

    def update_employee(self, token, id, employee):
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.patch(self.url + '/employee/'+str(id),
                              data=employee, headers=my_headers)
        return resp.json()
