# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = discounted or lowStock
promotion = not discounted and not lowStock

print(f"is the item eligible for promotion? {promotion}")