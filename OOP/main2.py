'''
Concept of Self.
'''
class Item:
    def calculate_total_price(self, x, y):
        return x * y
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
total = item1.calculate_total_price(item1.price, item1.quantity)
#here, the instance i.e. item1 is being passed to self
#and x, y = item1.price, item1.quantity
print(total)

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
total = item1.calculate_total_price(item2.price, item2.quantity)
#here, the instance i.e. item2 is being passed to self
#and x, y = item2.price, item2.quantity
#Here in line 17, try total = item1.calculate_total_price(item2.price, item2.quantity)
#because item1 is just an instance of Item() just like item2. It makes no difference at this moment.

print(total)
