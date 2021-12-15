import re

def get_input():
  txt = input("Enter a line of text: ")
  return txt

def duplicate(txt):
  txt2 = txt.strip()
  txt3 = re.sub(' +', ' ',txt2)
  txt4 = txt3 [::-1]
  return txt4

def text(txt):
  print(txt)

original_text = get_input()
print("Original Text: ")
text(original_text)

print("New Text: ")
updated_text = duplicate(original_text)
text(updated_text)