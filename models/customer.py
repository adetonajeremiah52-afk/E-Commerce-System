class Customer:
    def __init__ (self, name, email, balance):
        self.name = name
        self.email = email
        self.__balance = balance
        self.cart = []
        self.orders = []

    def get_balance(self):
         return self.__balance

    def add_to_cart (self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero")
            return False

        for item in self.cart:
            if item["product"] == product:
                current_quantity = item["quantity"]
                new_quantity = current_quantity + quantity

                if new_quantity > product.get_stock():
                    print("Not enough stock available")
                    return False

                item["quantity"] = new_quantity
                return True

        if quantity > product.get_stock():
            print(f"Not enough stock available. Only {product.get_stock()} left")
            return False

        cart_item = {"product": product, "quantity": quantity}
        self.cart.append(cart_item)
        return True

    def remove_from_cart(self, product):
        for item in self.cart:
            if item["product"] == product:
                self.cart.remove(item)
                print(f"{product.name} has been removed from cart")
                return True
        print("Product is not in the cart")
        return False

    def show_cart(self):
        print("--- Shopping Cart ---")
        if not self.cart:
            print("Your cart is empty.")
            return
        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product.name} - N{product.get_price():,.2f} x {quantity}")

    def cart_total(self):
        total = 0
        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]
            total += product.get_price() * quantity
        return total

    def clear_cart(self):
        self.cart = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return False
        else:
            self.__balance += amount
            print(f"Amount to deposit: N{amount:,.2f}")
            print("Deposit successful")
            print(f"New Balance: N{self.__balance:,.2f}")
            return  True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self.__balance:
            print("Insufficient Balance")
            return False

        self.__balance -= amount
        return True

    def show_orders(self):
        if not self.orders:
            print("No orders found")
            return

        print("--- Order History ---")
        for order in self.orders:
            order_id = order.order_id
            status = order.status
            total = order.calculate_total()
            print(f"Order ID: {order_id}")
            print(f"Status: {status}")
            print(f"Total: N{total:,.2f}\n")