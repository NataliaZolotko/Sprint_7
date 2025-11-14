from faker import Faker
import random

fake = Faker()

def generators_create_order_body():
    return {
    "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 10),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 10),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": fake.text(max_nb_chars=50),
        "color": [random.choice(["BLACK", "GRAY"])]
    }

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