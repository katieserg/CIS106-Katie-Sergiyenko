# input
principle = float(input("Enter principle amount of CD: $"))
ytm = float(input("Enter year to maturity of CD: $"))

# process phase
if principle > 100000 and ytm == 5:
  interest_rate = 0.06
else: 
  if principle >= 50000 and principle <= 100000 and ytm == 10:
    interest_rate = 0.05
  else: 
    if principle >= 50000 and principle <= 100000 and ytm ==5:
      interest_rate = 0.04
    else:
      interest_rate = 0.02

fyi = principle*interest_rate

# output
print("Principle:                      $", principle)
print("Interest rate:                   ", interest_rate)
print("Interest amount for first year: $", fyi)