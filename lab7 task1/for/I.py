#a = int(input())
#cnt = 0
#b = int(input())
#for x in range(1, a+1):
 #   if a%x == 0 :
#       cnt += 1

#print(cnt)
x = int(input())
d = 0
if x == 1:
    d = 1
else:
    for i in range(2, int((x/2) )):
        if x % i == 0:
            d += 1

print(d)
