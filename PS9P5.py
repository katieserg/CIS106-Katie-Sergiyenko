def comp_total(quantity, price):
  global total
  total = quantity*price
  global tax
  tax = total*0.07

# main
quantity = float(input("Enter quantity of item: "))
price = float(input("Enter unit price of item: $"))

comp_total(quantity, price)

print("Total: $" + str(total))
print("Tax: $" + str(tax))