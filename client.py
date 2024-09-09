import requests
from .config import Config
from .exceptions import PaystackAPIError

class PaystackClient:
    def __init__(self):
        self.base_url = Config.PAYSTACK_BASE_URL
        self.secret_key = Config.PAYSTACK_SECRET_KEY
        self.headers = {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PaystackAPIError(f"Request failed: {e}")
        return response.json()

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PaystackAPIError(f"Request failed: {e}")
        return response.json()
