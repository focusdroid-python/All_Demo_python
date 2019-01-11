import gevent
import time
from gevent import monkey

monkey.patch_all()

def test1(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.1)

def test2(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

def test3(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.6)

gevent.joinall([
	gevent.spawn(test1, 5),
	gevent.spawn(test2, 5),
	gevent.spawn(test3, 5)
])

