from collections import defaultdict

class Product:
    """Describing product"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_total(self, count: float):
        """Calculating total price for the product"""
        return self.price * count


class ShoppingCart:
    """Describing shopping cart"""

    def __init__(self):
        self.products = defaultdict(int)
        self.total = 0

    def add(self, product: Product, count: int = 1):
        """Adding products and calculating total sum"""

        self.products[product] += count
        self.total += product.price * count


prod1 = Product('lemon', 50)
print(prod1.get_total(10))
prod2 = Product('strawberry', 150)
print(prod2.get_total(20))
prod3 = Product('cucumber', 100)
print(prod2.get_total(20))
cart1 = ShoppingCart()
cart1.add(prod1, 5)
cart1.add(prod2, 10)
cart1.add(prod3, 20)
cart1.add(prod1, 5)
print(cart1.total)
