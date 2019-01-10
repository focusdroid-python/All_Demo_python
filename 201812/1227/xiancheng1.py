import threading
from time import sleep

def test1():
	for i in range(10000):
		print('---------test---------%d---'%i)

def test2():
	for i in range(10000):
		print('----111111111111111111111111111------%d----'%i)



def main():
	t1 = threading.Thread(target=test1)
	t2 = threading.Thread(target=test2)

	t1.start()
	t2.start()


if __name__ == "__main__":
	main()