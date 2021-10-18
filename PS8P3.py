def comp_total(msrp, make, model, code):
  if make == "Honda" and model == "Accord":
    percent_off = 0.10
  elif make == "Toyota" and model == "Rav4":
    percent_off = 0.15
  elif code == "Y":
    percent_off = 0.30
  else:
    percent_off = 0.05
  new_msrp = msrp - (msrp*percent_off)
  total = new_msrp + (new_msrp*0.07)
  return total

# main
msrp_sum = 0
sales_price_sum = 0
print("Would you like to compute the total price of your car? (Yes or No)")
response = input()

while response == "Yes":
  make = str(input("Enter make of car: "))
  model = str(input("Enter model of car: "))
  code = str(input("Is this an electric vehicle? (Y or N)"))
  msrp = float(input("Enter MSRP(sticker price): $"))

  comp_total(msrp, make, model, code)
  total = comp_total(msrp, make, model, code)

  msrp_sum = msrp_sum + msrp
  sales_price_sum = sales_price_sum + total

  print("Sales price: $" + str(total))

  print("Would you like to do this program again? (Yes or No)")
  response = input()

print("Sum of all MSRP's: $" + str(msrp_sum))
print("Sum of all sales prices: $" + str(sales_price_sum))