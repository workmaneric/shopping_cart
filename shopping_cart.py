class ShoppingCart:
    def __init__(self):
        self.products = []

    def calculate_cart_total(self):
        final_total = 0
        for product in self.products:
            final_total += product.price

        return final_total

    def add_product_to_cart(self, product):
        self.products.append(product)
        print(f'Your product {product.name} was added to your cart')

    def empty_products(self):
        self.products.clear()
        print("Your shopping cart is now empty")
