"""Lab4_15
App for food delivery
"""

orders = []


def add_dish(dish_name, dish_price):
    """Add dish to order
    parameters:
        dish_name: name of dish
        dish_price: price of dish"""
    orders.append((dish_name, dish_price))


def create_order():
    """Create order
    parameters:
        None"""
    amount = int(input("amount of dishes: "))
    for i in range(amount):
        name = input(f"dish {i+1}: ")
        price = float(input("dish price: "))
        add_dish(name, price)


def calculate_order_total():
    """Calculate order total
    parameters:
        None
    returns:
        total: total price of order"""
    total = 0
    for order in orders:
        total += order[1]
    return total


create_order()
print(calculate_order_total())
