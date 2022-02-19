'''
Concept of __init__.
Init runs the moment the class has been instantiated like in number 11 and 16.
So 'Init executing' should print twice.
'''
class Item:
    def __init__(self):
        print('Init executing')
    def calculate_total_price(self, x, y):
        return x * y
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
