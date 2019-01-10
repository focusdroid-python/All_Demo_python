from greenlet import greenlet
import time

def test1():
	while True:
		print('----A----')
		gr2.switch()
		time.sleep(0.2)


def test2():
	while True:
		print('-------------B----')
		gr1.switch()
		time.sleep(0.2)

def main():
	gr1 = greenlet(test1)
	gr2 = greenlet(test2)
	print('********************************')
	gr1.switch()

if __name__ == '__main__':
	main()
