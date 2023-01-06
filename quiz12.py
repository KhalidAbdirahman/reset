class Item:
    count = 0
    def __init__(self, size):
        Item.count += 1
        self.size = size
    def __repr__(self):
        return f'Item size: {self.size}'
    def __lt__(self, other):
        return self.size < other.size

class NamedItem(Item):
        def __init__(self, size, name):
            self.size = size
            self.name = name
        def __repr__(self):
            return f'Item size: {self.size} Item name: {self.name}'
        def __lt__(self, other_size, other_name = None):
            if self.size != other_size.size:
                return self.size < other_size.size
            else:
                return self.name < other_name.name



print(Item(3))
x = Item(4)
print(x < Item(3))
print(x < Item(19))
print(NamedItem(11, 'ABC'))
y = NamedItem(11, 'ABC')
print(x<y)
print(y<x)
z = NamedItem(11, 'BCD')
print(y<z)
print(z<y)


#___________________________________________________________________________________________________________________________________________________________________
class Warehouse():
    def __init__(self, address, item = []):
        self.address = address
        self.item = item
    def normilize(self):
        return self.item
    def __add__(self, other_warehouse):
        self.other_warehouse = other_warehouse
        self.item.append(self.other_warehouse)
        self.item.append(self.item)
        return self.item
    def add_item(self, an_item):
        self.item.append(an_item)
        return self.item

# x = Item(4)
# y = NamedItem(11, "ABC")
# z = NamedItem(11, "BCD")
# Warehouse("address one", [x, y, z])
# # w1 = Warehouse("address one", [x, y, z])
# # w2 = Warehouse("address two")
# # w2

# # w1.add_item(Item(-3))
# # w1
# # w1 + w2
 





