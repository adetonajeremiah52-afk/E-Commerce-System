class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.__price = price
        self.__stock = stock
        self.category = category

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def set_price(self, price):
        if price > 0:
            self.__price = price
            return True
        else:
            print("Price must be greater than zero")
            return False

    def reduce_stock(self, quantity):
        if 0 < quantity <= self.__stock:
            self.__stock -= quantity
            return True
        else:
            return False

    def show_product(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.get_price():,.2f}")
        print(f"Stock: {self.get_stock()}")
        print(f"Category: {self.category}\n")