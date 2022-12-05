from copy import deepcopy


class Product:
    """Describing product"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product {self.name} - price {self.price}'

    def __float__(self):
        return self.price

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def get_total(self, count: float):
        """Calculating total price for the product"""
        return round(self.price * count, 2)


class ShoppingCart:
    """Describing the shopping cart"""

    def __init__(self):
        self.products_list = []
        self.products_count = []

    def __repr__(self):
        cheque = ''
        for i in range(len(self.products_list)):
            cheque += f"" \
                      f"product - {self.products_list[i].name}, " \
                      f"price - {self.products_list[i].price}, " \
                      f"count - {self.products_count[i]}\n"
        cheque += f"total sum - {self.total_cart_sum()}"
        return cheque

    def __float__(self):
        return self.total_cart_sum()

    def __add__(self, other):
        added_cart = deepcopy(self)
        if isinstance(other, Product):
            added_cart.add_product(other, 1)
        elif isinstance(other, ShoppingCart):
            for product, count in zip(other.products_list, other.products_count):
                added_cart.add_product(product, count)
        return added_cart

    def add_product(self, product: Product, count: float = 1):
        """Adding products to the cart"""

        if product in self.products_list:
            common_index = self.products_list.index(product)
            self.products_count[common_index] += count
        else:
            self.products_list.append(product)
            self.products_count.append(count)

    def total_cart_sum(self):
        """Calculating the total cart sum"""

        product_list_sum = 0
        for product, count in zip(self.products_list, self.products_count):
            product_list_sum += product.get_total(count)
        return round(product_list_sum, 2)


prod1 = Product('lemon', 10.59)
print(prod1.get_total(0.7))
prod2 = Product('strawberry', 36.55)
prod3 = Product('cucumber', 100)
prod4 = Product('cucumber', 100)
cart1 = ShoppingCart()
cart1.add_product(prod1, 0.7)
cart1.add_product(prod2, 4)
cart1.add_product(prod3, 20)
cart1.add_product(prod1, 5)
print(cart1.products_list)
print(cart1.total_cart_sum())
print(prod1)
print("___________")
print(f"{cart1=}")
print("___________")
print(float(prod1))
print(str(prod1))
print(float(cart1))
cart2 = ShoppingCart()
cart2.add_product(prod1, 2)
cart2.add_product(prod2, 3)
print(prod4 == prod3)
print("___________")
print(f"{cart2=}")
cart3 = cart1 + prod1
print("___________")
print(f"{cart3=}")
cart4 = cart1 + cart2
print("___________")
print(f'{cart1=}')
print("___________")
print(f'{cart4=}')

# product_1 = Product("foo", 10.59)
# product_2 = Product("bar", 36.55)
# print(product_1.get_total(0.7))
# print(product_2.get_total(4))
# cart = ShoppingCart()
# cart.add_product(product_1, 0.7)
# cart.add_product(product_2, 4)
# print(cart.total_cart_sum())
