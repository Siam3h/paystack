import logging

def log_transaction(transaction):
    logging.info(f"Transaction: {transaction}")

def to_kobo(naira_amount):
    """
    Convert Naira amount to Kobo (smallest currency unit).
    """
    return int(naira_amount * 100)
