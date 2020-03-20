def sum13(nums):
    sum = 0
    skip = False

    for i in range(0, len(nums)):
        if not skip:
            if nums[i] == 13:
                skip = True
            else:
                sum += nums[i]
        else:
            skip = False
    return sum
