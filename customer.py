from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()
    def add_item_to_cart(self, product):
        self.cart.add_product_to_cart(product)
        print(f'{self.name} added {product.name} to their cart')

    def see_items_in_cart(self):
        for product in self.cart.products:
            print(product.name)
            