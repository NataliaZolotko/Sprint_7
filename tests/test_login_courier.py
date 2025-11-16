import requests
import pytest
import random
from faker import Faker
fake = Faker()
from data import DataAuthCourier, DataCreatNewCourier, Url
from courier_method import CreateCourierMethod
from generators import generator_auth_courier_body

import allure

class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    @allure.description("Авторизация по шаблонному логину и паролю, проверка статуса ответа и тела ответа") 
    def test_auth_courier(self):
        data = DataAuthCourier.Auth_Courier_Body
        response = CreateCourierMethod.auth_courier(data)
        assert response.status_code == 200 and response.json() == {id: 12345}
    
    @allure.title("Успешная авторизация курьера")
    @allure.description("Авторизация по логину и паролю, проверка статуса ответа") 
    def test_auth_new_courier(self):
        courier_data = DataCreatNewCourier.CreatNewCourier
        response = CreateCourierMethod.createcourier(courier_data)
        data = {
            "login": "testqwert",
            "password": "12345"
        }
        response = CreateCourierMethod.auth_courier(data)
        assert response.status_code == 200 
    

    @allure.title("Проверка:система вернёт ошибку, если неправильно указать логин или пароль")
    def test_auth_courier_with_incorrect_login_or_password(self):
        incorrect_password = {
            "login": "testqwert",  
            "password": fake.password()     
        }
        response = CreateCourierMethod.auth_courier(incorrect_password)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
        incorrect_login = {
            "login": fake.user_name(),  
            "password": "12345"     
        }
        response = CreateCourierMethod.auth_courier(incorrect_login)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
        
    @allure.title("Проверка:если какого-то поля нет, запрос возвращает ошибку")
    def test_auth_courier_with_not_login_or_password(self):
        not_password = {
            "login": "testqwert",  
            "password": ""    
        }
        response = CreateCourierMethod.auth_courier(not_password)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"
        not_login = {
            "login": "",  
            "password": "12345"     
        }
        response = CreateCourierMethod.auth_courier(not_login)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"
        
    @allure.title("Проверка:если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_auth_non_existent_user(self):
        non_existent_user = generator_auth_courier_body()
        response = CreateCourierMethod.auth_courier(non_existent_user)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
    
    @allure.title("Проверка: успешный запрос возвращает {id}")
    def test_return_id(self):
        data = {
            "login": "testqwert",
            "password": "12345"
        }
        response = CreateCourierMethod.auth_courier(data)
        assert response.json()["id"]