import math

a = int(input(""))
count=0
m=math.floor(math.sqrt(a))
for i in range(1,m+1) :
    if (a % i == 0):
        if(a/i==i):
            count+=1
        else:
            count+=2
print(count)