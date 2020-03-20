a=int(input(""))
check= False
i=1
while i<a:
    i=i*2
    if(i==a or a==1):
        check=True
if(check==True or a==1):
    print("YES")
else:
    print("NO")