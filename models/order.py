class Order:
    next_id = 1001
    def __init__(self, customer, items):
        self.order_id = f"ORD-{Order.next_id}"
        Order.next_id += 1
        self.customer = customer
        self.items = items.copy()
        self.status = "Pending"

    @classmethod
    def get_next_id(cls):
        return cls.next_id

    @staticmethod
    def generate_reference():
        return "ORDER-SYSTEM"

    @staticmethod
    def format_price(amount):
        return f"N{amount:,.2f}"

    def calculate_total(self):
        total = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.get_price() * quantity
        return total

    def checkout(self, payment_method):
        total = self.calculate_total()

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]

            if product.get_stock() < quantity:
                print("Checkout failed: Not enough stock.")
                self.status = "Failed"
                return

        if not payment_method.pay(total):
            self.status = "Failed"
            return

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            product.reduce_stock(quantity)
        print("Order Successful")
        self.customer.clear_cart()
        self.status = "Completed"
        self.customer.orders.append(self)

    def show_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print("-- Items --")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product.name} - N{product.get_price():,.2f} x {quantity}")
        print(f"Total: N{self.calculate_total():,.2f}")