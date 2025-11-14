import pytest
import requests
from faker import Faker
from courier_method import CreateCourierMethod
from generators import generator_create_courier_body


class TestCourierCreation:

    @pytest.fixture(autouse=False)
    def courier_data(self):
        """Фикстура подготовки и очистки данных курьера."""
        data = register_new_courier_and_return_login_password()
        yield data  
        # Постусловие: пытаемся удалить курьера после выполнения теста
        courier_id = get_courier_id(data["login"], data["password"])
        if courier_id:
            delete_courier(courier_id)
   
    @pytest.fixture
    def cleanup_courier(login, password):
        """Очистка: удаляет курьера если он существует"""
        courier_id = get_courier_id(login, password)
        if courier_id:
            delete_courier(courier_id)
        
                
    @pytest.fixture
    def unique_courier_data(self):
        """Фикстура для создания уникальных данных курьера."""
        data = generator_create_courier_body()
        yield data
        # Постусловие: удаляем созданного курьера
        cleanup_courier(data["login"], data["password"])


    