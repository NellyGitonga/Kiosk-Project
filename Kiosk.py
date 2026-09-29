# 1. WELCOME & SETUP

Owners_name = input("What is your name? ").strip().title()
kiosks_name = input("What is the Kiosk's name? ").strip().title()


def print_divider():
    print("=" * 30)


print_divider()
print(f"Welcome to {kiosks_name} Manager, run by {Owners_name}")
print_divider()


# 2. INVENTORY

stock = {
    'Bread': {'price': 65, 'quantity': 20},
    'Milk': {'price': 50, 'quantity': 50},
    'Sugar': {'price': 120, 'quantity': 60},
    'Salt': {'price': 30, 'quantity': 100},
    'Flour': {'price': 130, 'quantity': 100}
}

sales_log = []
products_sold = set()


# 3. FUNCTIONS


# View inventory
def full_inventory():
    print(f"{'Item':<15}{'Price':>10}{'Quantity':>12}")
    print("-" * 40)

    for item, details in stock.items():
        print(f"{item:<15}{details['price']:>10}{details['quantity']:>12}")


# Add or restock product
def restock_product():
    item = input("Enter item: ").strip().title()
    quantity = int(input("Enter quantity: "))

    if item in stock:
        stock[item]['quantity'] += quantity
        print(f"{item} has been restocked.")

    else:
        price = (input("Enter price: "))

        stock[item] = {
            'price': price,
            'quantity': quantity
        }

        print(f"{item} has been added to the inventory.")


# Sell product
def sell_product():
    item = input("Enter item: ").strip().title()
    quantity = int(input("Enter quantity: "))

    if item not in stock:
        print("Sorry, that item is not in stock.")
        return

    if quantity > stock[item]['quantity']:
        print("Sorry, there is not enough stock.")
        return

    total = stock[item]['price'] * quantity

    stock[item]['quantity'] -= quantity

    sales_log.append((item, quantity, total))
    products_sold.add(item)

    print("Sale successful!")
    print(f"Total price: {total}")


# Sales report
def sales_report():
    print("\n========== SALES REPORT ==========")

    total_revenue = 0

    for sale in sales_log:
        item, quantity, total = sale

        print(f"{item:<15}{quantity:>10}{total:>12}")

        total_revenue += total

    print("-" * 40)
    print(f"{'TOTAL REVENUE':<25}{total_revenue:>15}")

    print(f"Unique products sold: {len(products_sold)}")

    if sales_log:
        best_selling = sales_log[0]

        for sale in sales_log:
            if sale[1] > best_selling[1]:
                best_selling = sale

        print(f"Best-selling product: {best_selling[0]}")

    else:
        print("No sales have been made yet.")


# Search products
def search_products():
    search = input("Enter product name to search: ").lower()

    found = False

    for item, details in stock.items():

        if search in item.lower():
            print(
                f"{item:<15}"
                f"{details['price']:>10}"
                f"{details['quantity']:>12}"
            )

            found = True

    if not found:
        print("No matches found.")

#Restock product
def restock_product():
    item = input("Enter item: ").title()
    quantity = int(input("Enter quantity: "))

    if item in stock:
        stock[item]['quantity'] += quantity
        print(f"{item} has been restocked.")

    else:
        price = input("Enter price: ")

        stock[item] = {
            'price': price,
            'quantity': quantity
        }

        print(f"{item} has been added to the inventory.")




# Save inventory
def save_inventory():
    with open("inventory.txt", "w") as file:

        for item, details in stock.items():
            file.write(
                f"{item},{details['price']},{details['quantity']}\n"
            )

    print("Inventory saved successfully.")


# Save sales
def save_sales():
    with open("sales.txt", "a") as file:

        for sale in sales_log:
            item, quantity, total = sale

            file.write(f"{item},{quantity},{total}\n")

    print("Sales saved successfully.")



# 4. MAIN MENU

Menu = (
    "View Stock",
    "Add/Restock a Product",
    "Sell a Product",
    "View Sales Report",
    "Search Products"
)


while True:

    print("\n=========== Kiosk Menu ===========")

    for number, item in enumerate(Menu, start=1):
        print(f"{number}) {item}")

    print("6) Exit")

    choice = input("Choose a number: ").strip()

    if not choice.isdigit():
        print("Please enter a number from 1 to 6.")
        continue

    option = int(choice)

    if option == 1:
        full_inventory()

    elif option == 2:
        restock_product()

    elif option == 3:
        sell_product()

    elif option == 4:
        sales_report()

    elif option == 5:
        search_products()

    elif option == 6:
        save_inventory()
        save_sales()

        print("Goodbye!")
        break

    else:
        print("Please choose a number from 1 to 6.")