n=int(input())
sum = 0
p = 1

for x in range(0, len(str(n))) :
    
    sum += (n%10)*p
    p *=2
    n //=10
    
print(sum)