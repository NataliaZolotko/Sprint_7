from faker import Faker
import random

fake = Faker()


def generator_create_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

def generator_auth_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password()
    }