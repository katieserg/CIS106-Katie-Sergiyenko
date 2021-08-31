# input
itemcost = float(input("Enter cost of item: "))
tax = 0.07

# process phase
taxamount = itemcost*tax
total = itemcost+taxamount

# output
print("The total cost of this", itemcost) 
print("dollar item with a 7% tax of", taxamount)
print("dollars would be", total)
print("dollars.")