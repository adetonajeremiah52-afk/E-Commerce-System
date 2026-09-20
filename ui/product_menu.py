from e_commerce.utils import get_int_range, get_positive_int

def select_product(catalog, customer):

    number = get_positive_int("Enter a product number: ")
    index = number - 1
    product = catalog.get_product(index)
    if product is None:
        print("Product not found")
        return

    quantity = get_positive_int("Enter the quantity needed: ")

    success = customer.add_to_cart(product, quantity)
    if success:
        print(f"Successfully added {quantity} quantity of {product.name} to cart.")


def product_menu(catalog, customer):
    while True:
        print("\n--- Product Catalog Menu ---")
        print("1. Show All Product")
        print("2. Search Product")
        print("3. Filter by Category")
        print("4. Filter by Price")
        print("5. Select Product")
        print("6. Back")

        choice = get_int_range("Enter your choice: ", 1, 6)

        if choice == 1:
            print("\n --- All Product ---")
            catalog.show_products()

        elif choice == 2:
            name = input("\nEnter product name: ")
            results = catalog.search_product(name)
            if results:
                print("\n--- Search Results ---")
                catalog.show_results(results)
            else:
                print("No product found")

        elif choice == 3:
            category = input("\nEnter Category: ")
            results = catalog.filter_by_category(category)
            if results:
                print("\n--- Category Results ---")
                catalog.show_results(results)
            else:
                print("No product found in the category.")

        elif choice == 4:
            try:
                max_price = float(input("\nEnter maximum price: "))
                results = catalog.filter_by_price(max_price)
            except ValueError:
                print("Enter price in figure format")
                continue

            if results:
                print("\n--- Price Results ---")
                catalog.show_results(results)
            else:
                print("No product found")

        elif choice == 5:
            select_product(catalog, customer)

        elif choice == 6:
            print("Exiting catalog menu...")
            break

        else:
            return None