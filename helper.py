from data import DataCreateOrder
from data import DataCreateCourier


def modify_create_order(key,value):
    body = DataCreateOrder.Create_Order_Body.copy()
    body[key] = value
    return body

def modify_create_courier(key,value):
    body = DataCreateCourier.Create_Courier_Body.copy()
    body[key]=value
    return body