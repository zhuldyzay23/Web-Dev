s=input()
cnt = 0
a=[int(s) for s in s.split()]
for i in a:
    if int(i)>0 :
       cnt+=1
print(cnt)
