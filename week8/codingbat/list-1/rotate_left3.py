

def rotate_left3(nums):
	l = 1 % len(nums)
	return nums[l:] + nums[:l]

