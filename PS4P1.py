# input
quantity = int(input("Enter quantity of widgets: "))

# process phase
if quantity > 10000:
  price = 10
else:
  if quantity < 5000:
    price = 30
  else:
    price = 20
extended_price = quantity*price
tax_amount = extended_price*0.07
total = extended_price + tax_amount

# output
print("Extended price: $" + str(extended_price))
print("Tax amount: $" + str(tax_amount))
print("Total: $" + str(total))