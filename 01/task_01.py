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
        self.total_cart = []
        self.total_count = 0

    def add(self, product: Product, count: float = 1):
        """Adding products to the cart, count products"""

        total_product_price = product.get_total(count)
        self.total_cart.append(total_product_price)
        self.total_count += count

    def total_cart_sum(self):
        """Calculating the total cart sum"""

        return sum(self.total_cart)


prod1 = Product('lemon', 15.10)
print(prod1.get_total(0.7))
prod2 = Product('strawberry', 150)
prod3 = Product('cucumber', 100)
cart1 = ShoppingCart()
cart1.add(prod1, 0.7)
cart1.add(prod2, 20)
cart1.add(prod3, 20)
cart1.add(prod1, 5)
print(cart1.total_cart_sum())
print(cart1.total_count)
