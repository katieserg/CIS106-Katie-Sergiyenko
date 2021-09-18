# input
part = int(input("Enter a part number: "))
quantity = float(input("Enter the quantity: "))

# process phase
if part == 10 or part == 55:
  unit_cost = 1
elif part == 99:
  unit_cost = 2
elif part == 80 or part == 70:
  unit_cost = 3
else:
  unit_cost = 5
total_cost = quantity*unit_cost

# output
print("Part number:    ", part)
print("Cost per unit: $", unit_cost)
print("Total cost:    $", total_cost)