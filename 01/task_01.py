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
            quantity = \
                self.products_list.get(
                    product.name, 0
                )["quantity"] + count
        else:
            quantity = count
        self.products_list[product.name] = {"product": product, "quantity": quantity}

    def total_cart_sum(self):
        """Calculating the total cart sum"""

        product_list_sum = 0
        for item in self.products_list:
            product = self.products_list[item]['product']
            quantity = self.products_list[item]["quantity"]
            product_list_sum += product.get_total(quantity)
        return product_list_sum


prod1 = Product('lemon', 10.59)
print(prod1.get_total(0.7))
prod2 = Product('strawberry', 36.55)
prod3 = Product('cucumber', 100)
cart1 = ShoppingCart()
cart1.add(prod1, 0.7)
cart1.add(prod2, 4)
cart1.add(prod3, 20)
cart1.add(prod1, 5)
print(cart1.products_list)
print(cart1.total_cart_sum())
