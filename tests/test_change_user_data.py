from conftest import *
from endpoints.user import *


class TestDataChange:

    @allure.title('Проверка изменения данных пользователя')
    @allure.description('Проверяем, что данные пользователя корректно изменяются')
    @pytest.mark.parametrize('new_email, new_name', [['', ''], ['@new_email.new_email', ''],
                                                     ['', 'new_name'], ['@new_email.new_email', 'new_name']])
    def test_login_data_change(self, get_user, new_email, new_name):
        response = get_user.change_user_data(get_user.email.replace('@volkov.10', new_email) if new_email else None,
                                             new_name if new_name else None)
        assert (new_email in response.json()['user']['email'] and
                new_name in response.json()['user']['name'] and
                response.status_code == 200)

    @allure.title('Проверка изменения данных пользователя без авторизации')
    @allure.description('Проверяем, что для операции изменения данных требуется авторизация при изменении любого поля')
    @pytest.mark.parametrize('new_email, new_name', [['', ''], ['@new_email.new_email', ''],
                                                     ['', 'new_name'], ['@new_email.new_email', 'new_name']])
    def test_data_change_without_login(self, get_user_data, new_email, new_name):
        user = User(get_user_data)
        response = user.change_user_data(user.email.replace('@volkov.10', new_email) if new_email else None,
                                         new_name if new_name else None)
        assert (response.json()['success'] is False and
                response.json()['message'] == 'You should be authorised' and
                response.status_code == 401)
