# input
name = str(input("Enter last name: "))
hours = int(input("Enter hours: "))
payRate = float(input("Enter pay rate: "))

# process phase
grossPay = hours*payRate

# output
print("The gross pay for " + name + " is " + str(grossPay) + " dollars.")