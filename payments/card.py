from .payment import Payment

class CardPayment(Payment):
    def __init__(self, card_balance):
        self.card_balance = card_balance

    def  pay(self, amount):
        if amount > self.card_balance:
            print("Card Payment failed: Insufficient funds")
            return False
        self.card_balance -= amount
        print(f"Paid N{amount:,.2f} using Card")
        return True