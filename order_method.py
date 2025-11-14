import requests
from data import Url

class OrderMethods:
    @staticmethod
    def create_order(body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER}', json=body)
    
    @staticmethod
    def cancel_order(track_id):
        # ID заказа передается как параметр в строке запроса
        params = {
            "track": track_id
        }
        return requests.put(f'{Url.BASE_URL}{Url.ORDER}/cancel', params=params)
    
    @staticmethod
    def get_order_list(parameters=None):
        # Получение списка заказов с возможными параметрами фильтрации
        if parameters is None:
            parameters = {}
        return requests.get(f'{Url.BASE_URL}{Url.LIST_ORDERS}', params=parameters)
    
    @staticmethod
    def get_order_by_track(track_id):
        # Получение заказа по track номеру
        params = {
            "t": track_id
        }
        return requests.get(f'{Url.BASE_URL}{Url.ORDER}/track', params=params)