# input
name = str(input("Enter last name: "))
salary = float(input("Enter salary: $"))
job_level = int(input("Enter job level: "))

# process phase
if job_level >= 10:
  bonus_rate = 0.25
else:
  if job_level >= 5 and job_level <= 9:
    bonus_rate = 0.2
  else:
    bonus_rate = 0.1

bonus = salary*bonus_rate

# output
print(name)
print("Bonus: $",bonus)