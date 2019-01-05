def isEven(n):
  return (int(n)%2 == 0)

output = []
for i in range(1000, 3001):
  j = str(i)
  if isEven(j[0]) and isEven(j[1]) and isEven(j[2]) and isEven(j[3]):
    output.append(j)

print(','.join(output))