import math

def area(d):
  return int(math.sqrt((10 * d)/3))

final = []
x = input().split(',')
for i in range(len(x)):
  final.append(str(area(int(x[i]))))

print(','.join(final))