def comp_price(miles):
  if miles >= 30:
    price = 12
  elif miles < 30 and miles >= 20:
    price = 10
  elif miles < 20 and miles >= 10:
    price = 8
  else:
    price = 5
  return price

# main
ticket_sum = 0
print("Would you like to compute your ticket price? (Yes or No)")
response = input()

while response == "Yes":
  name = str(input("Enter last name: "))
  miles = float(input("Enter miles from downtown Chicago: "))

  comp_price(miles)
  price = comp_price(miles)

  ticket_sum = ticket_sum + price
  print(name)
  print("Ticket price: $" + str(price))

  print("Would you like to do this program again? (Yes or No)")
  response = input()

print("Sum of all tickets: $" + str(ticket_sum))