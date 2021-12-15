def getname():
    name = input("Enter full name: ")
    return name

def display_name(name):
  name_list = name.strip().split()
  
  if len(name_list) != 2:
    print("Invalid input")
  else:
    last_name = name_list[1]
    name_initial = name_list[0][0]
    print(f"{last_name}, {name_initial}.")

def main():
    name = getname()
    display_name(name)
main()