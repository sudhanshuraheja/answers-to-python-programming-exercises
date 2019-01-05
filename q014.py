x = input()
upper = 0
lower = 0
for i in x:
  if i.isupper() == True:
    upper = upper + 1
  elif i.isalpha() == True:
    lower = lower + 1

print("UPPER ", upper)
print("LOWER ", lower)