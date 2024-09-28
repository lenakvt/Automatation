import requests


class CompanyApi:
    # Инициализация
    def __init__(self, url):
        self.url = url

    # Получить список компаний
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    # Добавить компанию:
    def create_company(self, token, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = token
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()["id"]

    def get_company(self, id):
        resp = requests.get(self.url + '/company/'+str(id))
        return resp.json()
