def round_sum(a, b, c):
	return round10(a) + round10(b) + round10(c)

def round10(num):
	rem = num % 10
	out = num - rem
	return out + 10 if rem >= 5 else out
