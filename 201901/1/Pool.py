from multiprocessing import Pool
import os, time


def worker(msg):
	# t_start = time.time()
	print(msg)


def main():
	po = Pool(3)
	for i in range(20):
		po.apply_async(worker, (1,))
	print('---------start---------')
	po.close()
	po.join()
	print('-------close-----')




if __name__ == '__main__':
	main()