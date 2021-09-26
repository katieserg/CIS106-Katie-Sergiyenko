# input
dacounter = 0
print("Would you like to compute the total cost for an item? (Yes or No)")
response = input()

# process phase
while response == "Yes":
  quantity = int(input("Enter quantity of item: "))
  price = float(input("Enter price of item: $"))

  extended_price = quantity*price

  if extended_price > 10000.00:
    discount_percent = 0.25
  else:
    discount_percent = 0.10
  
  discount = extended_price*discount_percent
  total = extended_price - discount
  
  print("Extended price: $" + str(extended_price))
  print("Discount amount: $" + str(discount))
  print("Total: $" + str(total))

  dacounter = dacounter + discount

  print("Would you like to compute the total cost for another item? (Yes or No)")
  response = input()

# output
print("Sum of all discounts: $" + str(dacounter))