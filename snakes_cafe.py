def main():

   print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")

   def menu():
       print("""

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
Unicorn Tears""")


   menu_options = {
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

    def costumer_order():
        print("""
    ***********************************
    ** What would you like to order? **
    ***********************************""")
       order = input("> ")

    while order != "quit":
        if order in menu_options:
            menu_options[order] += 1
            print(f"""You have ordered {menu_options[order]}. Would you like to add any additional items to your order?""")

        elif order != menu_options:
            print("Sorry, that is not an item in our menu")
            order = input("> ")



if __name__ == "__main__":
    main()

