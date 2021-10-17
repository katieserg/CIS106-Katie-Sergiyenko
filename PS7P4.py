def comp_grosspay(hours, payrate):
  grosspay = payrate*hours
  return grosspay

def comp_payrate(code):
  if code == "L":
    payrate = 25
  elif code == "A":
    payrate = 30
  elif code == "J":
    payrate = 50
  return payrate

# main
name = str(input("Enter last name: "))
code = str(input("Enter job code (L, A, J): "))
hours = float(input("Enter hours worked: "))

comp_payrate(code)
payrate = comp_payrate(code)
comp_grosspay(hours, payrate)
grosspay = comp_grosspay(hours, payrate)

if hours > 40:
  overtimehours = hours - 40
  overtimepay = payrate*1.5
  overtimegrosspay = overtimehours*overtimepay
  totalgross = grosspay + overtimegrosspay
else:
  totalgross = grosspay

print(name)
print("Gross pay: $" + str(totalgross))