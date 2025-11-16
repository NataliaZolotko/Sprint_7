class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    ORDER = '/api/v1/orders'
    LIST_ORDERS = '/api/v1/orders'
    

class DataCreateOrder:
    Create_Order_Body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

class DataCreateCourier:
    Create_Courier_Body = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

class DataAuthCourier:
    Auth_Courier_Body = {
    "login": "ninja",
    "password": "1234"
}

class DataCreatNewCourier:
    CreatNewCourier = {
    "login": "testqwert",
    "password": "12345",
    "firstName": "Test1"

}


