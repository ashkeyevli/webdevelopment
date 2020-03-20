def big_diff(nums):
    min = nums[0]
    max = nums[0]

    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num

    return max - min
