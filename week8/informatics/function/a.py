def min_in_four_numbers(a,b,c,d):
    return min([int(a),int(b), int(c),int(d)])


array = input().split()
print(min_in_four_numbers(int(array[0]),int(array[1]),int(array[2]),int(array[3])))