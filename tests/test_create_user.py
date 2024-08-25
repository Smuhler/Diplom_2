from conftest import *
from endpoints.user import *


class TestRegister:

    @allure.title('Проверка регистрации пользователя')
    @allure.description('Проверяем, что пользователь с корректными данными регистрируется успешно')
    def test_register(self, get_user_data):
        user = User(get_user_data)
        response = user.register()
        assert (response.status_code == 200 and
                response.json()['success'] is True)

    @allure.title('Проверка регистрации существующего пользователя')
    @allure.description('Проверяем, что при регистрации существующего пользователя возвращается корректная ошибка')
    def test_register_already_registered_user(self, get_user):
        response = get_user.register()
        assert (response.status_code == 403 and
                response.json()['message'] == 'User already exists')

    @allure.title('Проверка регистрации пользователя без заполнения обязательных полей')
    @allure.description('Проверяем, что при регистрации пользователя без заполнения обязательных полей возвращается корректная ошибка')
    def test_register_without_data(self):
        user = User([None, None, None])
        response = user.register()
        assert (response.status_code == 403 and
                response.json()['message'] == 'Email, password and name are required fields')
