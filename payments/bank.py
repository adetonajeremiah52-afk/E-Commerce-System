from .payment import Payment

class BankPayment(Payment):
    def pay(self, amount):
        print(f"Paid N{amount:,.2f} using Bank Transfer")
        return True