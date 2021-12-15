line = input("Enter a line of comma-separated-values: ")

line_items = line.split(",")

for item in line_items:
  print(item.strip())