class Product:
    """Describing product"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_total(self, count: float):
        """Calculating total price for the product"""
        return round(self.price * count, 2)


class ShoppingCart:
    """Describing the shopping cart"""

    def __init__(self):
        self.products_list = {}

    def add(self, product: Product, count: float = 1):
        """Adding products to the cart"""

        if product.name in self.products_list:
            quantity = self.products_list.get(product.name, 0)["quantity"] + count
        else:
            quantity = count
        product_sum = product.get_total(quantity)
        price = product.price
        self.products_list[product.name] = {"quantity": quantity, "price": price, "product_sum": product_sum}

    def total_cart_sum(self):
        """Calculating the total cart sum"""

        product_list_sum = 0
        for product in self.products_list:
            product_list_sum += self.products_list[product]['product_sum']
        return product_list_sum


prod1 = Product('lemon', 15.10)
print(prod1.get_total(0.7))
prod2 = Product('strawberry', 150)
prod3 = Product('cucumber', 100)
cart1 = ShoppingCart()
cart1.add(prod1, 0.7)
cart1.add(prod2, 20)
cart1.add(prod3, 20)
cart1.add(prod1, 5)
print(cart1.products_list)
print(cart1.total_cart_sum())
