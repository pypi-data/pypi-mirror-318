import requests
from .exceptions import APIError

class YoPhoneAPI:
    BASE_URL = "https://yoai.yophone.com/api/pub"

    def __init__(self, api_key):
        self.headers = {"X-YoAI-API-Key": api_key}

    def post(self, endpoint, data):
        response = requests.post(f"{self.BASE_URL}{endpoint}", headers=self.headers, json=data)
        return self._handle_response(response)

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.BASE_URL}{endpoint}", headers=self.headers, params=params)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(f"API Error {response.status_code}: {response.text}")

