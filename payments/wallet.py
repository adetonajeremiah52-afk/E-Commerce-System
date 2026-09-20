from .payment import Payment

class WalletPayment(Payment):
    def __init__(self, customer):
        self.customer = customer

    def pay(self, amount):
        if self.customer.withdraw(amount):
            print(f"Paid N{amount:,.2f} using Wallet")
            print(f"Remaining Balance: N{self.customer.get_balance():,.2f}")
            return True
        return False