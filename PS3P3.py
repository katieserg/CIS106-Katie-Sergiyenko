# input
books = int(input("How many books would you like to order? "))
bookCost = float(input("What is the cost per book? $"))
orderTotal = bookCost*books

# process phase
if orderTotal <= 50:
  shipping = 25
else:
  shipping = 0

# output
print("The order total is: $", orderTotal)
print("Shipping costs:     $", shipping)