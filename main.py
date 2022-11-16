from product import Product
from customer import Customer

my_customer = Customer("Eric")

print(f'The customers name is {my_customer.name} ')

apple = Product("apple", "fruit", 3)
bannana = Product("bannana", "fruit", 4)
bacon = Product("bacon", "meat", 12)

my_customer.add_item_to_cart(apple)
my_customer.add_item_to_cart(bannana)
my_customer.add_item_to_cart(bacon)

total = my_customer.cart.calculate_cart_total()
print(f"The total for {my_customer.name}'s shopping cart is {total}")

my_customer.cart.empty_products()
my_customer.see_items_in_cart()

