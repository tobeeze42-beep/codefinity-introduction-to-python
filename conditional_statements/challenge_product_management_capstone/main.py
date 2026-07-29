# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"# Can be "Perishable" or "Non-Perishable"

#Series of coonditional statements to determine the discount for a prdduct based on its type, days until expiration, and stock level

if days_until_expiration <= 3 and stock_level > 50:
    print("30% discount applied")

if 4 <= days_until_expiration <= 6 and stock_level > 50:
      print("20% discount applied")

if days_until_expiration > 6 and stock_level <= 50:
     print("10% discount applied")

if product_type != "Perishable":
    print("No discount available for non-perishable items.")