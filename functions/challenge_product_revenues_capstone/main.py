# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, quantity in zip(prices, quantities_sold):
        revenue.append(price * quantity)
    return revenue

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))

def formatted_output(revenues):
    sorted_revenues = sorted(revenues, key=lambda x: x[0])
    for product_name, rev in sorted_revenues:
        print(f"{product_name} has total revenue of ${rev}")

formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")