import multiprocessing


def down_from_web():
	data = [11,22,33,44]

	for temp in data:
		q.put(temp)
	print('download over--------!!!!')

def analysis_data():

	watting_data = list()
	while True:
		data = q.get()
		watting_data.append(data)
		if q.empty():
			break




def main():

	q = multiprocessing.Queue()
	p1 = multiprocessing.Process(taregt=down_from_web, args=(q,))
	p2 = multiprocessing.Process(taregt=analysis_data)

	p1.start()
	p2.start()


if __name__ == '__main__':
	main()