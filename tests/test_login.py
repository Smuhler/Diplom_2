from conftest import *
from endpoints.user import *


class TestLogin:

    @allure.title('Проверка авторизации зарегистрированным пользователем')
    @allure.description('Проверяем, что авторизация происходит корректно')
    def test_login(self, get_user):
        response = get_user.login()
        assert (response.status_code == 200 and
                response.json()['success'] is True)

    @allure.title('Проверка авторизации несуществующим пользователем')
    @allure.description('Проверяем, что ошибка авторизации возвращается корректно')
    def test_login_incorrect_data(self, get_user_data):
        user = User(get_user_data)
        response = user.login()
        assert (response.status_code == 401 and
                response.json()['message'] == 'email or password are incorrect')
