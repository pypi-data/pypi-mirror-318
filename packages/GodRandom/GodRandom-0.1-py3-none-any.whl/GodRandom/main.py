import requests
import json
url = "https://api.random.org/json-rpc/4/invoke" #url к рандому

class Random:
    def __init__(self):
        self.api_key = None  # Это атрибут, который будет хранить ваш API-ключ
    """Получение int с random.org"""
    def get_randint(api, min, max, amount, replacement=True):
        
        api_key = api  # API-ключ

        # Формирование запроса
        data = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": api_key,  # API-ключ
                "n": amount,  # Количество случайных чисел
                "min": min,  # Минимальное значение
                "max": max,  # Максимальное значение
                "replacement": replacement,  # Повторение значений
            },
            "id": 1,
        }

        # Отправка запроса
        response = requests.post(url=url, json=data)

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            return result["result"]["random"]["data"]
        else:
            return "Error"
    """Получение decimal с random.org"""
    def get_randdec(api, amount, decimalPlaces):
        api_key = api  # API-ключ

        # Формирование запроса
        # Формирование запроса
        data = {
            "jsonrpc": "2.0",
            "method": "generateDecimalFractions",
            "params": {
                "apiKey": api,
                "n": amount,
                "decimalPlaces": decimalPlaces
            },
            "id": 1
        }


        # Отправка запроса
        response = requests.post(url=url, json=data)

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            return result["result"]["random"]["data"]
        else:
            return "Error"
    """Получение string с random.org"""
    def get_randstring(api, amount, length, characters, replacement=False):
        api_key = api  # API-ключ

        # Формирование запроса
        data = {
            "jsonrpc": "2.0",
            "method": "generateStrings",
            "params": {
                "apiKey": api,
                "n": amount,
                "length": length,
                "characters": characters,
                "replacement": replacement,
            },
            "id": 42,
        }

        # Отправка запроса
        response = requests.post(url=url, json=data)

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            return result["result"]["random"]["data"]
        else:
            return "Error"
    """Получение uuid с random.org"""
    def get_randuuid(api, amount):

        api_key = api  # API-ключ

        # Формирование запроса
        # Формирование запроса
        data = {
            "jsonrpc": "2.0",
            "method": "generateUUIDs",
            "params": {"apiKey": api, "n": amount},
            "id": 15998,
        }

        # Отправка запроса
        response = requests.post(url=url, json=data)

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            return result["result"]["random"]["data"]
        else:
            return "Error"
    """Получение api info с random.org"""
    def get_api_info(api):
        api_key = api  # API-ключ

        # Формирование запроса
        # Формирование запроса
        data = {
            "jsonrpc": "2.0",
            "method": "getUsage",
            "params": {"apiKey": api},
            "id": 15998,
        }

        # Отправка запроса
        response = requests.post(url=url, json=data)

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return "Error"
    """Рофл функция BTW)"""
    def hello():
        print("Hello From GodRandom!")

if __name__ == "__main__":
    print("Hello From GodRandom!")
"""
Библа оч сырая, написана на коленке за пачку кириешек, по поводу говно кода не пишите, потом перепешу(наверно)
Написано одним русским //Специалистом// за два дня
Dron3915 on GitHub 2025
BUILD DATE 04.01.2025
"""