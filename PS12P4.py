def repeat_shift(line):
  characters = int(input("Enter number of characters to print in each line: "))
  lines = int(input("Enter number of lines to print: "))
  scroll = input("Enter scroll direction of lines (r or l): ")
  
  shift = ""
  if scroll == "r":
   shift = ""
  elif scroll == "l":
   shift = " " * (lines - 1)
    
  counter = 0

  for i in range(lines):
   print(shift, end='')
   
   if scroll == "r":
     shift += " "
   elif scroll == "l":
     shift = shift[:-1]
     
   for j in range(characters):
      print(line[counter], end='')
      
      counter = (counter + 1) % len(line)
      
   print()

#main
if __name__ == '__main__':
  line = input("Enter the line of text: ")
  
  repeat_shift(line)