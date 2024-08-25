import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def create_data_for_user_register():
    return [f'{generate_random_string(10)}@volkov.10', generate_random_string(10), generate_random_string(10)]
