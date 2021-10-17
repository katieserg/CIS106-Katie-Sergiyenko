def comp_total(quantity, price):
  total = quantity*price
  if total > 10000.00:
    total = total*0.9
  else:
    total = total
  return total

# main
quantity = float(input("Enter quantity: "))
price = float(input("Enter price: "))

comp_total(quantity, price)
total = comp_total(quantity, price)

print("Quantity: " + str(quantity))
print("Price: $" + str(price))
print("Total: $" + str(total))