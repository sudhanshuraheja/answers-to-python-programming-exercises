x = input().split(',')

final = []
for i in range(int(x[0])):
  internal = []
  for j in range(int(x[1])):
    internal.append(i * j)
  final.append(internal)

print(final)