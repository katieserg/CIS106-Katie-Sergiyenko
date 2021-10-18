def comp_sqft(length, width, height):
  sqft = (2*length*width) + (2*length*height) + (2*width*height)
  return sqft

# main
print("Would you like to compute gallons needed? (Yes or No")
response = input()

while response == "Yes":
  length = float(input("Enter length of room: "))
  width = float(input("Enter width of room: "))
  height = float(input("Enter height of room: "))

  comp_sqft(length, width, height)
  sqft = comp_sqft(length, width, height)

  gallons = sqft/50
  print("Gallons needed: " + str(gallons))
  
  print("Would you like to do this program again? (Yes or No)")
  response = input()