my_current_order = {}

snakes_menu = {
    "wings": 0,
    "cookies": 0,
    "spring rolls": 0,
    "salmon": 0,
    "steak": 0,
    "meat tornado": 0,
    "a literal garden": 0,
    "ice cream": 0,
    "cake": 0,
    "pie": 0,
    "coffee": 0,
    "tea": 0,
    "unicorn tears": 0,
}


def welcome():
    print('''
    *************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************''')


def menu():
    print('''
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears''')


def order_invitation():
    print('''
    ***********************************
    ** What would you like to order? **
    ***********************************''')

    while True:
        users_order = input("> ").lower()

        if users_order == "quit":
            break
        elif users_order == "that is all":
            print('''
            Your order is coming right up. Thank you for eating at Snakes Cafe!''')
            break
        elif users_order not in snakes_menu:
            print(f'''
            Your {users_order} is not on the menu, but we can make an exception.''')

        if users_order in my_current_order:
            my_current_order[users_order] += 1
        else:
            my_current_order[users_order] = 1

        print(f'''
        1 order of {users_order} has been added to your meal''')

        print('''
        What else can I prepare for you today?
        Type "quit" to quit, "that is all" to confirm your order, or enter another item.''')

    print(f'''
    Your meal consists of: {my_current_order}''')


welcome()
menu()
order_invitation()
