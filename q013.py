x = input()
letters = 0
digits = 0
for i in x:
  if i.isdigit() == True:
    digits = digits + 1
  elif i.isalpha() == True:
    letters = letters + 1

print('LETTERS ', letters)
print('DIGITS ', digits)