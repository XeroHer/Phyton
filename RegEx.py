import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

y = re.findall("ai", txt)
Z = re.findall("Portugal", txt)
A = re.search("\s", txt)
b= re.split("\s", txt)
c = re.split("\s", txt, 1)
print(c)
print(b)
print("The first white-space character is located in position:", A.start()) 
print(Z)
print(y)

d = re.sub("\s", "9", txt)
# replace all whitespace with 9
print(d)

