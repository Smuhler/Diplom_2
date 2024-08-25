from conftest import *
from endpoints.ingredients import *
from endpoints.orders import *


class TestOrderCreate:

    @allure.title('Проверка создания заказа авторизованным пользователем')
    @allure.description('Создается зарегистрированный пользователь и проверяем, что заказ создается')
    def test_order_create_with_authorise(self, get_user):
        ingredients = Ingredients()
        response = get_user.create_order([ingredients.get_ingredients_id_list()[0]])
        assert (response.json()['order']['number'] and
                response.json()['order']['owner'] and
                response.status_code == 200)

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Проверяем, что заказ создается')
    def test_order_create_without_authorise(self):
        ingredients = Ingredients()
        orders = Orders()
        response = orders.create_order([ingredients.get_ingredients_id_list()[1]])
        assert (response.json()['order']['number'] and
                response.status_code == 200)

    @allure.title('Проверка создания заказа со всеми ингредиентами')
    @allure.description('Проверяем, что заказ создается')
    def test_order_create_correct_list(self):
        ingredients = Ingredients()
        orders = Orders()
        response = orders.create_order(ingredients.get_ingredients_id_list())
        assert (response.json()['order']['number'] and
                response.status_code == 200)

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Проверяем, что для заказа требуется указать ингредиент')
    def test_order_create_empty_list(self):
        orders = Orders()
        response = orders.create_order([])
        assert (response.json()['success'] is False and
                response.json()['message'] == 'Ingredient ids must be provided' and
                response.status_code == 400)

    @allure.title('Проверка создания заказа с несуществующим ингредиентом')
    @allure.description('Проверяем, что для заказа требуется указать ингредиент добавленный в базу')
    def test_order_create_incorrect_ingredient(self):
        orders = Orders()
        response = orders.create_order(['71c0c5a71d1f82001bdaaa6d'])
        assert (response.json()['success'] is False and
                response.json()['message'] == 'One or more ids provided are incorrect' and
                response.status_code == 400)

    @allure.title('Проверка создания заказа с неверным хешем ингредиента')
    @allure.description('Проверяем, что для заказа требуется указать ингредиент добавленный в базу с корректным хешем')
    def test_order_create_incorrect_hash(self):
        orders = Orders()
        response = orders.create_order(['d1f82001bdaaa6d'])
        assert ('Internal Server Error' in response.text and
                response.status_code == 500)
