# Restaurant Menu Ordering System Using Python Dictionaries
menu = {
    "Burger":350,
    "Chicken Burger":400,
    "Veg Burger":300,
    "French Fries":150,
    "Soft Drink":100,
    "Ice Cream":200,
    "Small-Pizza":500,
    "Medium-Pizza":700,
    "Large-Pizza":900,
    "Pasta":450,
    "Salad":250,
    "Sandwich":300,
    "Coffee":120,
    "Tea":80,
    "Juice":150,
    "Water":50,
    "Dessert":180,
    "Soup":220,
    "Steak":800,
    "Fish":750, 
    "Girlfriend Special": 1000,
    "Boyfriend Special": 1200,
}
print ("Welcome to Single Restaurant")
print ("Here is the Pure Single Menu;")
for item,price in menu.items():
    print (f"{item}:Rs{price}")

order_total=0
item_1=input("Enter the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
else:
    print(f"Sorry {item_1} is not available in this menu.")

another_order =input("Do You Want to order Another Item? (yes/no)")
if another_order == "yes":
    item_2=input("Enter the Item you want to order to Add in your single life = ")
    if item_2 in menu:
       order_total +=menu[item_2]
       print (f"item {item_2} in your single life")
    else:
        print(f"Sorry {item_2} is not available in this menu.")
print (f"Your total order amount is Rs{order_total}")