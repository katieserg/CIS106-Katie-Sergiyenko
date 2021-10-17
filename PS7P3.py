def comp_gas_cost(gallons):
  gas_cost = gallons*2.5
  return gas_cost

def comp_mpg(miles, gallons):
  mpg = miles/gallons
  return mpg

# main
destination = str(input("Enter destination city: "))
miles = float(input("Enter miles travelled: "))
gallons = float(input("Enter gallons used: "))

comp_mpg(miles, gallons)
mpg = comp_mpg(miles,gallons)

comp_gas_cost(gallons)
gas_cost = comp_gas_cost(gallons)

print(destination)
print("Miles travelled: " + str(miles))
print("Cost of gas: $" + str(gas_cost))