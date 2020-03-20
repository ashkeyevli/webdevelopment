def make_bricks(small, big, goal):
	if big * 5 + small < goal:
	  return False
	elif goal * 5 <= small:
	  return False
	return True
#est' owibka v teste