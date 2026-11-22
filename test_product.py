from product import product_info

def test_product_info():

    result = product_info(101, "Laptop", 2, 45000)

    expected = ("Product ID: 101\n"
                "Product Name: Laptop\n"
                "Quantity: 2\n"
                "Price: 45000")

    assert result == expected