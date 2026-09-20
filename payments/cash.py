from .payment import Payment

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid N{amount:,.2f} using Cash")
        return True