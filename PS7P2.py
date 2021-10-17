def comp_batting_avg(hits, at_bats):
  batting_avg = hits/at_bats
  return batting_avg

# main
name = str(input("Enter player last name: "))
hits = float(input("Enter number of hits: "))
at_bats = float(input("Enter number of at-bats: "))

comp_batting_avg(hits, at_bats)
batting_avg = comp_batting_avg(hits, at_bats)

print(name)
print("Batting average: " + str(batting_avg))