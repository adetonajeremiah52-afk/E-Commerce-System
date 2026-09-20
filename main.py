from e_commerce.models import Product, Customer, ProductCatalog
from e_commerce.ui import run_menu

laptop = Product("Laptop", 500_000, 5, "Electronics")
phone = Product("Phone", 300_000, 10, "Electronics")
headphones = Product("Headphones", 50_000, 15, "Accessories")
t_shirt = Product("T-Shirt", 25_000, 20, "Clothing")
sneakers = Product("Sneakers", 80_000, 8, "Clothing")
backpack = Product("Backpack", 40_000, 15, "Accessories")

customer = Customer("Jeremiah", "adetonajeremiah52@gmail.com", 3_000_000)

catalog = ProductCatalog()

run_menu(customer, catalog)
