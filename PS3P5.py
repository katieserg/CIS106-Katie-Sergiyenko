# input
name = str(input("Enter last name: "))
dependents = int(input("Enter the number of dependents: "))
grossIncome = float(input("Enter gross income: $"))
agi = grossIncome-dependents*12000

# process phase
if agi > 50000:
  itr = 0.20
else:
  itr = 0.10
incomeTax = agi*itr
if incomeTax < 0:
  incomeTax = 100

# output
print(name)
print("Gross income:          $", grossIncome)
print("Number of dependents:   ", dependents)
print("Adjusted gross income: $", agi)
print("Income tax:             ", incomeTax)