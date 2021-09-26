# input
counter = 0
gross_pay_sum = 0
print("Would you like to compute your gross pay? (Yes or No)")
response = input()

# process phase
while response == "Yes":
  counter = counter + 1
  name = str(input("Enter employee last name: "))
  hours = float(input("Enter hours worked: "))
  pay_rate = float(input("Enter rate of pay: $"))

  gross_pay = hours*pay_rate
  
  if hours > 40:
    overtime_hours = hours-40
    overtime_pay = pay_rate*1.5
    overtime_gross_pay = overtime_hours*overtime_pay
    total_gross = gross_pay + overtime_gross_pay
  else:
    total_gross = gross_pay

  print("The gross pay for " + str(name) + " is $" + str(total_gross))
  gross_pay_sum = gross_pay_sum + total_gross

  print("Would you like to compute another gross pay? (Yes or No)")
  response = input()

# output
print("Sum of all gross pays: $" + str(gross_pay_sum))
print("Number of employees entered: " + str(counter))
average_pay = gross_pay_sum/counter
print("Average pay: $" + str(average_pay))