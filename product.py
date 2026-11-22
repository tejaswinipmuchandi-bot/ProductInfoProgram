
def product_info(product_id, name, quantity, price):
    return (f"Product ID: {product_id}\n"
            f"Product Name: {name}\n"
            f"Quantity: {quantity}\n"
            f"Price: {price}")


print(product_info(101, "Laptop", 2, 45000))