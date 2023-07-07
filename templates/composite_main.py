from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount()

item2 = Item("MyItem", 750)
item2.name = "OtherItem"

# Getting an Attribute
print(item1.name)
print(item1.price)

print(item2.name)
print(item2.price)