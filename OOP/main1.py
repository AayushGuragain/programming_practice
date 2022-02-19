class Item:
    pass
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
item1.price_total = item1.price * item1.quantity

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
print(type(item1.price_total))

random_string = 'OOP' #here, instance of an string was grabbed and named random_string
print(random_string.upper()) #the method of that string class named upper was executed.
