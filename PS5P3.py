# input
counter = 0
print("Do you want to compute your average exam score? (Yes or No)")
response = input()

# process phase
while response == "Yes":
  counter = counter + 1
  name = str(input("Enter student last name: "))
  score1 = float(input("Enter exam score 1: "))
  score2 = float(input("Enter exam score 2: "))
  
  average = (score1 + score2)/2

  print(name + " has an average exam score of " + str(average))
  
  print("Do you want to compute another average exam score? (Yes or No)")
  response = input()

# output
print("Total number of students: ",counter)