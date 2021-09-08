# input
name = str(input("Enter name of appliance: "))
applianceCost = float(input("What is the cost of the appliance? $"))

# process phase
if applianceCost > 1000:
  warranty = 0.10*applianceCost
else:
  warranty = 0.05*applianceCost
total = applianceCost+warranty

# output
print("Name of appliance:  ", name)
print("Cost of appliance: $", applianceCost)
print("Cost of warranty:  $", warranty)
print("Total cost:        $", total)