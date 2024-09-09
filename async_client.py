import httpx
from .config import Config
from .exceptions import PaystackAPIError

class AsyncPaystackClient:
    def __init__(self):
        self.base_url = Config.PAYSTACK_BASE_URL
        self.secret_key = Config.PAYSTACK_SECRET_KEY
        self.headers = {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }

    async def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=data, headers=self.headers)
                response.raise_for_status()
            except httpx.RequestError as e:
                raise PaystackAPIError(f"Request failed: {e}")
            return response.json()

    async def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
            except httpx.RequestError as e:
                raise PaystackAPIError(f"Request failed: {e}")
            return response.json()
