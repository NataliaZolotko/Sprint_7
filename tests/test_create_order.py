import requests
import pytest
from data import DataCreateOrder, Url
from order_method import OrderMethods
import allure

class TestCreateOrder:
    @allure.title("Проверка, что создать заказ можно с разным набором цвета, тело ответа содержит track")
    @pytest.mark.parametrize("color_option", [
        ["BLACK"],
        ["GRAY"], 
        ["BLACK", "GRAY"],
        ['']
    ])
    def test_create_order_with_different_colors(self, color_option):
        order_data = DataCreateOrder.Create_Order_Body
        order_data["color"] = color_option
        response = OrderMethods.create_order(order_data)
        assert response.status_code == 201 and 'track' in response.json() 
        