def comp_ct(sales):
  if sales > 100000.00:
    commissionp = 0.10
  else:
    commissionp = 0.05
  commission = commissionp*sales
  target = sales + (sales*0.05)
  return commission, target

# main
name = str(input("Enter salesperson's last name: "))
sales = float(input("Enter number of sales: "))

comp_ct(sales)
commission, target = comp_ct(sales)

print(name)
print("Commission: $" + str(commission))
print("Next year's target: " + str(target))