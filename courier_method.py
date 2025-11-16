import requests
import allure
from data import Url, DataCreateCourier
import random
import string
        
class CreateCourierMethod:
    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=body)
        
    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER}/{courier_id}')
    
       
    @staticmethod
    @allure.step("Авторизация курьера")
    def auth_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=body)
    
   
    @staticmethod
    @allure.step("Сгенерировать данные для создания курьера")
    def create_courier_body(): 
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return {
            "login": f"test_courier_{random_suffix}",
            "password": "password123",
            "firstName": "TestCourier"
        } 