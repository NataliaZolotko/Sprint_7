import pytest
import requests
import random
from faker import Faker
from courier_method import CreateCourierMethod


@pytest.fixture()
def courier_data():
    """Фикстура подготовки и очистки данных курьера."""
    data = register_new_courier_and_return_login_password()
    yield data  
    # Постусловие: пытаемся удалить курьера после выполнения теста
    courier_id = get_courier_id(data["login"], data["password"])
    if courier_id:
        delete_courier(courier_id)
                     

@pytest.fixture
def temporary_courier():
    """Создаем временного курьера и автоматически удаляем после теста"""
    data = {
        "login": f"test_courier_{random.randint(1000, 9999)}",
        "password": "password123",
        "firstName": "TestCourier"
    }
    try:
        courier_id = get_courier_id(data["login"], data["password"])
        if courier_id:
            delete_courier(courier_id)
    except:
        pass
     
    yield data
     
    try:
        courier_id = get_courier_id(data["login"], data["password"])
        if courier_id:
            delete_courier(courier_id)
    except:
        pass
  

     
            