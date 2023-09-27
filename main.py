MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money_in_machine = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("☕️")

coffee_machine_is_on = True


def format_data():
    """Format account into printable format: name, description and country"""
    # Values from the Keys in the person_a
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    return f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_in_machine}\n"


def is_resources_enough(order_ingredients):
    """Returns True when order can be made, and False if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
            # print("Is not enough")
            return False
    return is_enough


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins")
    total_value_quarters_inserted = float(input("How many quarters?: ")) * 0.25
    total_value_dimes_inserted = float(input("How many dimes?: ")) * 0.10
    total_value_nickles_inserted = float(input("How many nickles?: ")) * 0.05
    total_value_pennies_inserted = float(input("How many pennies?: ")) * 0.01
    total_value_coins_inserted = (total_value_quarters_inserted + total_value_dimes_inserted
                                  + total_value_nickles_inserted + total_value_pennies_inserted)
    return total_value_coins_inserted


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money_in_machine
        money_in_machine += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


while coffee_machine_is_on:
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_coffee_choice == "off":
        coffee_machine_is_on = False
    elif user_coffee_choice == "report":
        print(format_data())
    else:
        drink = MENU[user_coffee_choice]
        if is_resources_enough(drink["ingredients"]):  # It calls the function to verify
            # if there is enough resources for the coffee.
            user_payment = process_coins()  # It calls the function to Return
            # the total calculated from coins inserted.
            if is_transaction_successful(user_payment, drink["cost"]):  # It calls the function
                # to verify if the money is enough to pay for the coffee
                make_coffee(user_coffee_choice, drink["ingredients"])
