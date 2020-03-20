def xor(x,y):
    if(x!=y):
        return 1
    else:
        return 0
array = input().split()
print(xor(float(array[0]),float(array[1])))