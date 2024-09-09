import unittest
from modules.processor import PaymentProcessor

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.payment_processor = PaymentProcessor()

    def test_initialize_payment(self):
        email = "test@example.com"
        amount = 5000
        callback_url = "http://your-site.com/callback"
        response = self.payment_processor.initialize_payment(email, amount, callback_url)
        self.assertIn('status', response)
        self.assertTrue(response['status'])

    def test_verify_payment(self):
        reference = "dummy_reference"
        response = self.payment_processor.verify_payment(reference)
        self.assertIn('status', response)
        self.assertTrue(response['status'])

if __name__ == '__main__':
    unittest.main()
