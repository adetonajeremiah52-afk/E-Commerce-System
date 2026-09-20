class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            product.show_product()

    def search_product(self, name):
        result = []

        for product in self.products:
            if name.lower() in product.name.lower():
                result.append(product)

        return result

    def filter_by_category(self, category):
        result = []

        for product in self.products:
            if category.lower() in product.category.lower():
                result.append(product)

        return result

    def filter_by_price(self, max_price):
        result = []

        for product in self.products:
            if product.get_price() <= max_price:
                result.append(product)

        return result

    def show_results(self, products):
        for product in products:
            product.show_product()

    def get_product(self, index):
        if 0 <= index < len(self.products):
            return self.products[index]
        return None