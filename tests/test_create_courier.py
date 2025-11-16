import requests
import pytest
import random
import string
from faker import Faker
from data import DataCreateCourier, Url, DataCreatNewCourier
from courier_method import CreateCourierMethod
from generators import generator_create_courier_body
import allure

fake = Faker()

class TestCreateCourier:
    @allure.title("Создание курьера")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа и тела ответа") 
    def test_create_courier_success(self, temporary_courier):
        data = temporary_courier
        response = CreateCourierMethod.create_courier(data)
        assert response.status_code == 201 and response.json() == {"ok": True}
 

    @allure.title("Проверка, что нельзя создать двух одинаковых курьеров")  
    def test_create_duplicate_courier_fails(self, temporary_courier):
        data = temporary_courier
        first_response = CreateCourierMethod.create_courier(data)
        duplicate_response = CreateCourierMethod.create_courier(data)
        assert duplicate_response.status_code == 409 and duplicate_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
        

    @allure.title("Проверка: чтобы создать курьера, нужно передать в ручку все обязательные поля (логин и пароль)")
    def test_create_courier_with_only_login_password_success(self):
        courier_data = generator_create_courier_body()
        del courier_data["firstName"]
        response = CreateCourierMethod.create_courier(courier_data)
        assert response.status_code == 201 and response.json() == {"ok": True}
    
    @allure.title("Запрос возвращает правильный код ответа при успехе")
    def test_create_courier_returns_correct_status_code(self):
        data = generator_create_courier_body()
        response = CreateCourierMethod.create_courier(data)
        assert response.status_code == 201

    @allure.title("Проверим, что успешный запрос возвращает ok: True") 
    def test_successful_request(self):
        data = generator_create_courier_body()
        response = CreateCourierMethod.create_courier(data)
        assert response.json() == {"ok": True}
    
           
    @allure.title("Проверка, что если одного из полей нет, запрос возвращает ошибку")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field(self, missing_field):
        data = generator_create_courier_body()
        del data[missing_field]
        response = CreateCourierMethod.create_courier(data)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_courier_with_existing_login_fails(self):
        duplicate_data = {
            "login": "ninja",  
            "password": fake.password(),         
            "firstName": fake.first_name()      
        }
        response = CreateCourierMethod.create_courier(duplicate_data)
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется. Попробуйте другой."