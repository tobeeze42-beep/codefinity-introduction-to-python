grocery_inventory = {"Milk" : ("Dairy", 3.50, 8), "Eggs" : ("Dairy", 5.50 , 30) , "Bread" : ("Bakery", 2.99 , 15 ) , "Apples" : ("Produce", 1.50, 50)}
category, price, stock = grocery_inventory["Eggs"]

if price > 5:
    grocery_inventory["Eggs"] = (category, price - 1, stock)
    print("Eggs are too expensive, reducing the price by $1.")

else:
     print("The price of Eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

milk_stock = grocery_inventory["Milk"][2]

if milk_stock <10:
   yo, zo, xo = grocery_inventory["Milk"]
   grocery_inventory["Milk"] = (yo, zo, xo + 20)
   print("milk needs to be restocked. increasing stock by 20 units.")

else:
     print("Milk has sufficient stock.")
    
apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    
print("Updated inventory:",  grocery_inventory)