import requests


class AuthenticationApi:
    # Инициализация
    def __init__(self, url):
        self.url = url

    # Получение токена
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
