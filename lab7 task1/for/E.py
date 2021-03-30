n = int(input())
cnt = 0
for x in range(0, len(str(n))) :
    cnt += n%10
    n //= 10
    
print(cnt)