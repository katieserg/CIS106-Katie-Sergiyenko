def comp_avg(score1, score2, score3, handicap):
  avg = (score1+score2+score3)/3
  avgh = (score1+score2+score3)/3 + handicap
  return avg, avgh

# main
name = str(input("Enter bowler's last name: "))
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
handicap = float(input("Enter handicap: "))

comp_avg(score1, score2, score3, handicap)
avg, avgh = comp_avg(score1, score2, score3, handicap)

print(name)
print("Average score: " + str(avg))
print("Average score with handicap: " + str(avgh))