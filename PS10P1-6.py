def dl1(mylist):
  n = int(input("Enter number of items in list: "))
  for n in range(0,n,1):
    s = int(input("Enter an integer: "))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)

#DL1
mylist = []
mylist = dl1(mylist)
print("DL1")
print(mylist)

#DL2
mylist.insert(0,99)
print("DL2")
print(mylist)

#DL3
mylist[0] = 100
print("DL3")
print(mylist)

#DL4
mylist2 = [500,600,700,800,900]
print("DL4")
print(mylist2)
mylist.extend(mylist2)
print(mylist)

#DL5
mylist.remove(800)
print("DL5")
print(mylist)

#DL6
mylist.pop(2)
print("DL6")
print(mylist)