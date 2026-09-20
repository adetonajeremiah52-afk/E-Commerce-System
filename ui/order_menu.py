from e_commerce.utils import get_int_range, get_positive_int

def order_menu(customer):
    while True:
        print("\n--- Orders ---")
        print("1. View Orders")
        print("2. View Order Details")
        print("3. Exit")

        order_choice = get_int_range("Enter your choice: ",1, 3)

        if order_choice == 1:
            customer.show_orders()

        elif order_choice == 2:
            if not customer.orders:
                print("No orders found.")
                continue
            print("\n--- Your Orders ---")
            for index, order in enumerate(customer.orders, start=1):
                print(f"{index}. {order.order_id}")
            order_number = get_positive_int("Enter order number: ")
            index = order_number - 1
            order = customer.orders[index]
            order.show_order()

        elif order_choice == 3:
            print("Exiting order menu...")
            break

        else:
            return None