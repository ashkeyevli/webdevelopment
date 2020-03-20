
def sum67(nums):
	sum = 0
	skip = False

	for i in range(0, len(nums)):
		if not skip:
			if nums[i] == 6:
				skip = True
			else:
				sum += nums[i]
		else:
			if nums[i] == 7:
				skip = False
	return sum