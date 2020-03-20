a=int(input(""))
b=int(input(""))
for i in range(a,b+1):
    c=i**(1/2)
    if(c%1==0):
        print(int(c*c))