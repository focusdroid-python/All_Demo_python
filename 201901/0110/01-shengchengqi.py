def create_num(all_num):
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		# print(a)
		yield a
		a, b = b, a+b
		current_num+=1
	return 'success'


obj = create_num(10)
print(obj)

"""for num in obj:
	print(num)"""


while True:
	try:
		ret = next(obj)
		print(ret)
	except Exception as ret:
		print(ret.value)
		break