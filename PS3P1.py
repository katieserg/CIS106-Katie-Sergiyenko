# input
quantity = int(input("Enter quantity of item: "))
taxPercent = 0.07

# process phase
if quantity >= 1000:
  unitPrice = 3
else: 
  unitPrice = 5
extendedPrice = quantity*unitPrice
tax = extendedPrice*taxPercent
total = extendedPrice+tax

# output
print("Quantity of item:         ",quantity)
print("Unit price of item:      $",unitPrice)
print("Extended price of item:  $",extendedPrice,)
print("Tax:                     $",tax,)
print("Total:                   $",total)