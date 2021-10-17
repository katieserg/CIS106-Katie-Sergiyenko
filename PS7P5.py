def comp_tuition(credits, code):
  if code == "I":
    tuition = credits*250
  else:
    tuition = credits*550
  return tuition

# main
name = str(input("Enter student last name: "))
credits = float(input("Enter credit hours: "))
code = str(input("Enter district code: (I or O): "))

comp_tuition(credits, code)
tuition = comp_tuition(credits, code)

print(name)
print("Tuition owed: $" + str(tuition))