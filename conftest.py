import pytest
from helpers import *
from endpoints.user import *


@pytest.fixture(scope="function")
def get_user_data():
    user_data = create_data_for_user_register()
    yield user_data
    user_to_delete = User(user_data)
    if user_to_delete.login().status_code == 200:
        user_to_delete.delete()


@pytest.fixture(scope="function")
def get_user():
    user = User(create_data_for_user_register())
    user.register()
    yield user
    user.delete()
