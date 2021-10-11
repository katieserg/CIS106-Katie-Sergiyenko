num1 = 1
num2 = 1
num3 = num1 + num2
print(num1)
print(num2)
for count in range (2, 20, 1):
  print(num3)
  num1 = num2
  num2 = num3
  num3 = num1 + num2