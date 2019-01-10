def createNum():
	print('------start------')
	a,b = 0,1
	for i in range(10):
		print('----yeild---start-----')
		yield b
		a,b = b,a+b
		print('----yeild---end')
	print('------end------')


a = createNum()

