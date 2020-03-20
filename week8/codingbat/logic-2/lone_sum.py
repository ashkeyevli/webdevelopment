def lone_sum(a, b, c):
	if a == b:
		if b == c:
			return 0
		return c
	elif a == c:
		return b
	elif b == c:
		return a
	return a + b + c
