def checkPrime(n):
    flag=1;
    for j in range(2,int(n/2)):
        if n%j==0:
            flag=0
            break
    return flag



array = input().split()
for i in range(int(array[0])+1,int(array[1])):
    galf=checkPrime(i)
    if galf==1:
        print(i,end=" ")
