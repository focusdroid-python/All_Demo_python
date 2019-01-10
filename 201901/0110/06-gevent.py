import gevent

def test(n):
	for i in range(n):
		print(gevent.getcurrent(), i)


