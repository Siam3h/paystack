from unittest.mock import patch
import unittest
from modules.processor import PaymentProcessor

class TestPaymentProcessor(unittest.TestCase):

    @patch('modules.client.PaystackClient.post')
    def test_initialize_payment(self, mock_post):
        # Mock Paystack API response
        mock_post.return_value = {
            'status': True,
            'data': {
                'authorization_url': 'https://paystack.com/authorize'
            }
        }

        payment_processor = PaymentProcessor()
        response = payment_processor.initialize_payment('test@example.com', 5000, 'https://example.com/callback')

        self.assertIn('status', response)
        self.assertTrue(response['status'])

    @patch('modules.client.PaystackClient.get')
    def test_verify_payment(self, mock_get):
        # Mock  Paystack API response
        mock_get.return_value = {
            'status': True,
            'data': {
                'reference': 'nmug42lyfz',
                'status': 'success'
            }
        }

        payment_processor = PaymentProcessor()
        response = payment_processor.verify_payment('nmug42lyfz')

        self.assertIn('status', response)
        self.assertTrue(response['status'])

if __name__ == '__main__':
    unittest.main()
