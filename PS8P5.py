def comp_assessed_value(county, mvalue):
  if county == "Cook":
    avp = 0.90
  elif county == "DuPage":
    avp = 0.80
  elif county == "McHenry":
    avp = 0.75
  elif county == "Kane":
    avp = 0.60
  else:
    avp = 0.70
  assessed_value = mvalue*avp
  return assessed_value

# main
mvalue_sum = 0
assessed_value_sum = 0
print("Would you like to compute the assessed value of a home? (Yes or No)")
response = input()

while response == "Yes":
  county = str(input("Enter name of county: "))
  mvalue = float(input("Enter market value of home: $"))

  comp_assessed_value(county, mvalue)
  assessed_value = comp_assessed_value(county, mvalue)
  
  mvalue_sum = mvalue_sum + mvalue
  assessed_value_sum = assessed_value_sum + assessed_value

  print("Market value: $" + str(mvalue))
  print("Assessed value: $" + str(assessed_value))

  print("Would you like to do this program again? (Yes or No)")
  response = input()

print("Sum of all market values: $" + str(mvalue_sum))
print("Sum of all assessed values: $" + str(assessed_value_sum))