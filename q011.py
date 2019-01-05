x = input().split(',')
output = []
for i in x:
  if int(i, 2) % 5 == 0:
    output.append(i)

print(','.join(output))