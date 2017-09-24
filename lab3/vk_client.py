import requests
from base_client import *
from exception import *
from datetime import datetime


class GetVkID(BaseClient):
    v = 5.68

    def __init__(self, user_name):
        super().__init__('https://api.vk.com/method/', 'users.get', 'GET')
        self.user_id = user_name

    # Получение GET параметров запроса
    def get_params(self):
        return {'user_ids': self.user_id, 'v': self.v}

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(method), self.get_params())
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        try:
            response_dict = response.json()
            if response_dict.get('error') is not None:
                error = response_dict.get('error')
                error_msg = error.get("error_msg")
                raise APIException(error_msg)
            else:
                return response_dict.get('response')[0]
        except APIException as ex:
            print(ex.err)


class GetVkFriends(BaseClient):
    v = 5.68
    fields = 'bdate'

    def __init__(self, user_name):
        super().__init__('https://api.vk.com/method/', 'friends.get', 'GET')
        self.user_id = user_name

    # Получение GET параметров запроса
    def get_params(self):
        return {'user_id': self.user_id, 'v': self.v, 'fields': self.fields}


    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(method), self.get_params())
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        try:
            response_dict = response.json()
            if response_dict.get('error') is not None:
                error = response_dict.get('error')
                error_msg = error.get("error_msg")
                raise APIException(error_msg)
            else:
                return response_dict.get('response').get('items')
        except APIException as ex:
            print(ex.err)