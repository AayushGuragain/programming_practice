'''
Here, we created a good __init__ method,
We know self references the instance.
So, the lines 11,12,13 inside __init__ are doing same thing done by line 16,17,18.
Line11 is self.name = "Phone" while
line16 is <instance_name>.name = "Phone"

'''
class Item:
    def __init__(self, name, price, quantity):
        self.name = name #line11
        self.price = price #line12
        self.quantity = quantity #line13

item1 = Item('Phone', 100, 5)
# item1.name = 'Phone' #line16
# item1.price = 100 #line17
# item1.quantity = 5 #line18

print(item1.name, item1.price, item1.quantity)
item2 = Item('Car', 20000, 1)
'''
So think about our item2 that is car. A car will always have a price
and we always want to know how many i.e. quantity.
But what if our item2 is a unique car that can go absoloutely driverless.
At present context, 2022, it would be a unique car.
And what if we want to have a boolean to store that data.
It wont be ideal to change __init__ for that weirdly specific thing.
So, what can be done? The following:
'''
item2.absoloutely_driverless = True
print(item2.absoloutely_driverless)
#print(item1.absoloutely_driverless) #should bre error
