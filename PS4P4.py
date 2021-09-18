# input
quantity = int(input("Enter number of concert tickets: "))

# process phase
if quantity >=25:
  ppt = 50
else: 
  if quantity >= 10 and quantity <= 24:
    ppt = 60
  else:
    if quantity >= 5 and quantity <= 9:
      ppt = 70
    else:
      ppt = 75

total_cost = quantity*ppt

# output
print("Number of tickets: ", quantity)
print("Price per ticket: $", ppt)
print("Total cost:       $", total_cost)