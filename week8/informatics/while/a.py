a=int(input(""))
i=1
while i<=a:
    c=i**(1/2)
    if(c%1==0):
        print(int(c*c))
    i+=1