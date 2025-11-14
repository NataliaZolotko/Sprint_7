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
    def get_courier_id(login,password):
        params = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', params=params)   
        if response.status_code == 200:
            return response.json()["id"]
        else:
            return None
    
    @staticmethod
    def auth_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=body)
    
    