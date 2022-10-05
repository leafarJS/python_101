# jorge wants to open a pizza 🍕 shop and need to write a program for accepting orders

#Tips - Always visualize first, then start coding

# variable declaration 
customer: str = 'jorge'
pizza_base: str =  'thin'
pizza_size: int = 12
topping: str = 'Olives'
extra_cheese: bool = True
price: float = 99.99

#alternative 1 - Using print function 

print(f"Received order from: {customer}")
print(f"Pizza Base: {pizza_base}, size: {pizza_size} inches, Topping: {topping}")
print(f"you need to cheese in your order: {extra_cheese}")
print(f"Bill amount: {price}")

#alternative 2 - Using fromatted String

order_detail: str = f"""
Received order from: {customer}
Pizza Base: {pizza_base}, size: {pizza_size} inches, Topping: {topping}
you need to cheese in your order: {extra_cheese}
Bill amount: {price}
"""
print(order_detail)

#alternative 3 Using fromatted String in print


print(f"""
Received order from: {customer}
Pizza Base: {pizza_base}, size: {pizza_size} inches, Topping: {topping}
you need to cheese in your order: {extra_cheese}
Bill amount: {price}
""")