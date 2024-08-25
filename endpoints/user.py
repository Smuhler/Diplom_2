from endpoints.orders import *
from urls import *
import requests
import allure
import json


class User(Orders):

    def __init__(self, user):
        super().__init__()
        self.email = user[0]
        self.password = user[1]
        self.name = user[2]
        self.refreshToken = None

    @allure.step('Регистрируемся')
    def register(self):
        payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = requests.post(register_url, data=payload)
        if response.status_code == 200:
            self.accessToken = response.json()['accessToken']
            self.refreshToken = response.json()['refreshToken']
        return response

    @allure.step('Авторизуемся')
    def login(self):
        payload = {
            "email": self.email,
            "password": self.password
        }
        response = requests.post(login_url, data=payload)
        if response.status_code == 200:
            self.accessToken = response.json()['accessToken']
            self.refreshToken = response.json()['refreshToken']
        return response

    @allure.step('Удаляем пользователя')
    def delete(self):
        if self.accessToken is None:
            return 'nothing to delete'
        else:
            return requests.delete(f'{user_url}')

    @allure.step('Редактируем данные пользователя')
    def change_user_data(self, new_email, new_name):
        headers = {
            'Content-Type': 'application/json'
        }
        if self.accessToken:
            headers['authorization'] = self.accessToken

        payload = {}
        if new_email:
            payload['email'] = new_email
        if new_name:
            payload['name'] = new_name

        response = requests.patch(user_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200 and response.json()['success']:
            self.email = response.json()['user']['email']
            self.name = response.json()['user']['name']
        return response
