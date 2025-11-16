import requests
from data import Url
import allure

class OrderMethods:
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER}', json=body)
    
      
    @staticmethod
    @allure.step("Получить список заказов")
    def get_order_list(parameters=None):
        # Получение списка заказов с возможными параметрами фильтрации
        if parameters is None:
            parameters = {}
        return requests.get(f'{Url.BASE_URL}{Url.LIST_ORDERS}', params=parameters)
    