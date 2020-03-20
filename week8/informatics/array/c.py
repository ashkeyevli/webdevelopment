num=int(input(""))
array=[]
count=0
array=input().split()
for i in range(0,num):
    if int(array[i])>0:
       count+=1
print(count)