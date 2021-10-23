def comp_total(quantity, price2, rate):
  disc_amt = price2*rate
  disc_price = price2 - disc_amt
  return disc_amt, disc_price

# main
quantity = float(input("Enter quantity of item: "))
price = float(input("Enter price of item: $"))
rate = float(input("Enter discount rate: "))
price2 = quantity*price

comp_total(quantity,price2,rate)
disc_amt, disc_price = comp_total(quantity,price2,rate)

print("Discount amount: $" + str(disc_amt))
print("Discounted price: $" + str(disc_price))
print("Quantity: " + str(quantity))
print("Original price for all quantities: $" + str(price2))