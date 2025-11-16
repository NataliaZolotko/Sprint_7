# Sprint_7

##  <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results



| Название файла          | Содержание файла                |
|-------------------------|-------------------------------- |
| Tests dir               | Директория с тестами            |
| test_create_courier.py  | Тесты на создание курьера       |
| test_create_order.py    | Тесты на создание заказа        |
| test_login_courier.py   | Тесты на логин курьера          |
| test_list_order.py      | Тесты, что возращается список   |
|                         | заказа                          |
| conftest.py             | Фикстуры                        |
| data.py                 | Файл с Url и телом запросов     |
| courier_method.py       | методы к странице теста курьера |
| order_method.py         | методы к странице теста заказа  |
| requirements.txt        | Файл с зависимостями            |
| allure_results.dir      | Папка с отчетами Allure         |
