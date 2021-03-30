import math
a = int(input())
b = int(input())
for x in range(a, b+1):
    m = int(math.sqrt(x))
    if m*m == x :
        print(x) 
