import threading
import socket
import time
import multiprocessing

def test1():
	while True:
		print('---test11111111111111---------')
		time.sleep(1)

def test2():
	while True:
		print('---test222-----------')
		time.sleep(1)



def main():
	t1 = multiprocessing.Process(target=test1)
	t2 = multiprocessing.Process(target=test2)

	t1.start()
	t2.start()



if __name__ == '__main__':
	main()