import requests
from data import Url

class OrderMethods:
    @staticmethod
    def create_order(body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER}', json=body)
    
      
    @staticmethod
    def get_order_list(parameters=None):
        # Получение списка заказов с возможными параметрами фильтрации
        if parameters is None:
            parameters = {}
        return requests.get(f'{Url.BASE_URL}{Url.LIST_ORDERS}', params=parameters)
    