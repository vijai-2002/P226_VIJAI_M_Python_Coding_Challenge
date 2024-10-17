# entity/payment.py

from entity.client import Client  # Ensure you import the Client class

class Payment:
    def __init__(self, payment_id: int, payment_date: str, payment_amount: float, client: Client):
        self.payment_id = payment_id
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.client = client


    # You can add additional methods or properties here if needed
