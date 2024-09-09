from .client import PaystackClient

class PaymentProcessor:
    def __init__(self):
        self.client = PaystackClient()

    def initialize_payment(self, email, amount, callback_url):
        """
        Initialize a transaction with Paystack.
        """
        payload = {
            "email": email,
            "amount": amount,
            "callback_url": callback_url
        }
        response = self.client.post("/transaction/initialize", payload)
        return response

    def verify_payment(self, reference):
        """
        Verify a transaction using the transaction reference.
        """
        response = self.client.get(f"/transaction/verify/{reference}")
        return response
