import requests
import pytest
from data import Url
from order_method import OrderMethods
import allure

class TestListOrder:
    @allure.title("Проверка, что в тело ответа возвращается список заказов.")
    def test_list_order(self):
        response = OrderMethods.get_order_list()
        assert response.status_code == 200 and 'orders' in response.json() 
        orders_list = response.json()["orders"]
        assert isinstance(orders_list, list)
        