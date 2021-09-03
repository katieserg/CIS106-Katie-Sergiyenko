# input
itemPrice = float(input("Enter item price: "))
discountPercent = float(input("Enter discount percentage as a decimal: "))

# process phase
discountAmount = discountPercent*itemPrice
price = itemPrice-discountAmount

# output
print("The discount amount is " + str(discountAmount) + " dollars, and the discounted price of the item is " + str(price) + " dollars.")