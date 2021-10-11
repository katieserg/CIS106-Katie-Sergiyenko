print("Would you like to compute your beginning balance, ending balance, and accumulated interest earned?")
yn = input()

while yn == "Yes":
  principle = float(input("Enter principle amount:"))
  rate = float(input("Enter interest rate:"))
  print("Year  " + "Beginning Balance  " + "Ending Balance")
  total_interest = 0
  for year in range(1, 5 + 1, 1):
    interest = principle * rate
    total_interest = total_interest + interest
    ebalance = principle + interest
    print(str(year) + "  $" + str(principle) + "  $" + str(ebalance))
    principle = ebalance
  print("Total interest earned: $" + str(total_interest))
  print("Would you like to do this again? (Yes or No)")
  yn = input()