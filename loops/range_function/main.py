# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for days in range(5):
    product = daily_promotions[days]
    week = weekdays[days]
    print(f"{week}: promotion on {product}")