import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')
    PAYSTACK_BASE_URL = os.getenv("PAYSTACK_BASE_URL")
