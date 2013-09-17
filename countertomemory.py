# countertomemory


def add_to_mem():
	num_holder = {}
	for counter in range (0,10):
		num_holder[counter] = 100 - counter
	
	return num_holder

print add_to_mem()