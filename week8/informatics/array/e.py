num=int(input(""))
check=False
array=[]
count=0
array=input().split()
for i in range(0,num-1):
    if int(array[i])>0 and int(array[i+1])>0 or int(array[i])<0 and int(array[i+1])<0 :
        check=True
if check==True:
    print("YES")
else:
    print("NO")
