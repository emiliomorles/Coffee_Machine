# Coffee Machine 👀

A Coffee Machine simulator

## Developer: https://github.com/emiliomorles

## Year: 2023

✅ I learned:

    🟢 How to call for a Key in a dictionary  ✔️
    🟢 That the parameter is created when the function is being called. And, when I I formulating the funtion, I can change the name of the parameter. e.g.:
    def make_coffee(drink_name, order_ingredients): # >>>>>>>>>>>>>drink_name<<<<<<<<<<<<<<<< 👈
        """Deduct the required ingredients from resources"""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕")

    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")        
    drink = MENU[user_coffee_choice] # There is a dictionary MENU with all the ingredients data.
    
    make_coffee(user_coffee_choice, drink["ingredients"]) # >>>>>>>>>>>>>drink["ingredients"]<<<<<<<<<<<<<<<< 👈

    🟢 Creating a new parameter for a function in order to compare values in a dictionary with an input from the user.
    🟢 To use a Global Variable





