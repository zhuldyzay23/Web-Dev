n = int(input())
d = int(input())
cnt = 0
for x in range(0, len(str(n))) :
    if(n%10 == d):
        cnt += 1
    n //= 10
    
print(cnt)