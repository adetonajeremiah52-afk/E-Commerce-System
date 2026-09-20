from e_commerce.models import Order
from e_commerce.payments import CardPayment, BankPayment, CashPayment, WalletPayment
from e_commerce.utils import get_int_range, get_non_negative_float

def choose_payment_method(customer):
    print("\n--- Payment Method ---")
    print("1. Card")
    print("2. Bank")
    print("3. Cash")
    print("4. Wallet")

    payment_choice = get_int_range("Choose payment method: ", 1, 4)

    if payment_choice == 1:
        card_balance = get_non_negative_float("Enter your card balance: ")
        return CardPayment(card_balance)

    elif payment_choice == 2:
        return BankPayment()

    elif payment_choice == 3:
        return CashPayment()

    elif payment_choice == 4:
        return WalletPayment(customer)

    else:
        return None


def cart_menu(customer):
    while True:
        print("\n--- Shopping Cart Menu---")
        print("1. View Cart")
        print("2. Remove Product")
        print("3. View Cart Total")
        print("4. Checkout")
        print("5. Back")

        option = get_int_range("Enter your choice: ", 1, 5)

        if option == 1:
            customer.show_cart()

        elif option == 2:
            try:
                number = int(input("Enter product number to remove: "))
                if number <= 0:
                    print("Product number must be greater than zero")
                    continue
                index = number - 1
                cart_item = customer.cart[index]
                product_to_remove  = cart_item["product"]
                customer.remove_from_cart(product_to_remove)
            except (ValueError, IndexError):
                print("Please enter a valid product number.")

        elif option == 3:
            total = customer.cart_total()
            print("--- Cart Total ---")
            print(f"Total: N{total:,.2f}")

        elif option == 4:
            if not customer.cart:
                print("Your cart is empty. Add products before checkout.")
                continue
            print("Proceeding to checkout...")
            order = Order(customer, customer.cart)
            payment = choose_payment_method(customer)
            if payment:
                order.checkout(payment)

        elif option == 5:
            print("Exiting cart menu...")
            break

        else:
            return None