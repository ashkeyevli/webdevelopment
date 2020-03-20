
def caught_speeding(speed, is_birthday):
	limit = 5 if is_birthday else 0

	if speed >= (81 + limit):
		return 2
	elif speed >= (61 + limit):
		return 1
	else:
		return 0
