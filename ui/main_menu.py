from .product_menu import product_menu
from .cart_menu import cart_menu
from .order_menu import order_menu
from ..utils import get_int_range

def run_menu(customer, catalog):
    while True:
        print("=== E-Commerce System ===")
        print("1. Products")
        print("2. Cart")
        print("3. Orders")
        print("4. Exit")

        choice = get_int_range("Enter choice: ", 1, 4)

        if choice == 1:
            product_menu(catalog, customer)
        elif choice == 2:
            cart_menu(customer)
        elif choice == 3:
            order_menu(customer)
        elif choice == 4:
            print("Exiting E-Commerce System menu...")
            break
        else:
            return None