from conftest import *
from endpoints.orders import *


class TestGetOrders:

    @allure.title('Проверка получения заказов авторизованного пользователя')
    @allure.description('Проверяем, что список заказов возвращается при авторизованном запрове')
    def test_get_orders_current_user(self, get_user):
        response = get_user.get_orders()
        assert (response.json()['success'] is True and
                response.json()['orders'] == [] and
                response.status_code == 200)

    @allure.title('Проверка получения заказов пользователя без авторизации')
    @allure.description('Проверяем, что для получения списка заказов пользователя требуется авторизация')
    def test_get_orders_without_authorisation(self):
        response = Orders().get_orders()
        assert (response.json()['success'] is False and
                response.json()['message'] == 'You should be authorised' and
                response.status_code == 401)
