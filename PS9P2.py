def comp_total (score1, score2, score3):
  avg = (score1+score2+score3)/3
  total = score1 + score2 + score3
  return avg, total

# main
name = str(input("Enter student's last name: "))
score1 = float(input("Enter first exam score: "))
score2 = float(input("Enter second exam score: "))
score3 = float(input("Enter third exam score: "))

comp_total(score1, score2, score3)
avg, total = comp_total(score1, score2, score3)

print(name)
print("Total points: " + str(total))
print("Average exam score: " + str(avg))