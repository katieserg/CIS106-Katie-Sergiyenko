def comp_nmsales(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    percent = 0.10
  elif month == "Apr" or month == "May" or month == "Jun":
    percent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    percent = 0.20
  else:
    percent = 0.25
  nmsales = sales*(1+percent)
  return nmsales

# main
print("Would you like to compute next month's sales? (Yes or No)")
response = input()

while response == "Yes":
  name = str(input("Enter last name: "))
  month = str(input("Enter month: "))
  sales = float(input("Enter sales: $"))

  comp_nmsales(month, sales)
  nmsales = comp_nmsales(month, sales)

  print(name)
  print("Next month's sales: $" + str(nmsales))

  print("Would you like to do this program again?")
  response = input()