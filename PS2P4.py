# input
name = str(input("Enter last name: "))
credits = int(input("Enter credits: "))

# process phase
tuition = 250
labFee = 100
totalTuition = (credits*tuition) + labFee

# output
print("The total tuition fee for " + str(name) + " is " + str(totalTuition) + " dollars.")