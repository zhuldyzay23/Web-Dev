max = 0
index_of_max = -1
s = input().split(' ')
len = 0
for i in s:
   i = int(i)
   if i > max:
       max = i
       index_of_max = len
   len += 1
print(max, index_of_max)