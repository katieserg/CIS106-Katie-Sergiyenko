# input
item = str(input("Enter an item (A or B): "))
quantity = int(input("Enter the quantity of this item: "))

# process phase
if item == "A":
  unitPrice = 10
else: 
  unitPrice = 20
extendedPrice = quantity*unitPrice

# output
print("Item name:       ", item)
print("Unit price:     $", unitPrice)
print("Extended price: $", extendedPrice)