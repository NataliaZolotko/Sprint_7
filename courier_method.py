import requests
from data import Url, DataCreateCourier

class CreateCourierMethod:
    @staticmethod
    def createcourier(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=body)
        
    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER}/{courier_id}')
    
       
    @staticmethod
    def auth_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=body)
    
    