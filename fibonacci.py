# Sarah Smith
# fibonacci number program

def calc_fib(index):
	if index == 0:
		return 0
	if index == 1:
		return 1
	else:
		return calc_fib(index-1) + calc_fib(index-2)


for i in range(0,11):
	print calc_fib(i)


