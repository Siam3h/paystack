class PaystackAPIError(Exception):
    """Raised when there is an error with the Paystack API request."""
    pass

class PaymentVerificationError(Exception):
    """Raised when payment verification fails."""
    pass
