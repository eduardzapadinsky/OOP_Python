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
        self.products_list = []
        self.products_count = []

    def add_product(self, product: Product, count: float = 1):
        """Adding products to the cart"""

        if product in self.products_list:
            self.products_count[
                self.products_list.index(product)] += count
        else:
            self.products_list.append(product)
            self.products_count.append(count)

    def total_cart_sum(self):
        """Calculating the total cart sum"""

        product_list_sum = 0
        for product, count in zip(self.products_list, self.products_count):
            product_list_sum += product.get_total(count)
        return round(product_list_sum, 2)


# prod1 = Product('lemon', 10.59)
# print(prod1.get_total(0.7))
# prod2 = Product('strawberry', 36.55)
# prod3 = Product('cucumber', 100)
# cart1 = ShoppingCart()
# cart1.add_product(prod1, 0.7)
# cart1.add_product(prod2, 4)
# cart1.add_product(prod3, 20)
# cart1.add_product(prod1, 5)
# print(cart1.products_list)
# print(cart1.total_cart_sum())

product_1 = Product("foo", 10.59)
product_2 = Product("bar", 36.55)
print(product_1.get_total(0.7))
print(product_2.get_total(4))
cart = ShoppingCart()
cart.add_product(product_1, 0.7)
cart.add_product(product_2, 4)
print(cart.total_cart_sum())
