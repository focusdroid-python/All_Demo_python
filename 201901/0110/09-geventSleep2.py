import gevent
import time
from gevent import monkey

monkey.patch_all()

def test1(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)
		# gevent.sleep(0.5)

def test2(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)
		# gevent.sleep(1)

def test3(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)
		# gevent.sleep(0.5)


gevent.joinall([
	gevent.spawn(test1, 5),
	gevent.spawn(test2, 5),
	gevent.spawn(test3, 5)
])


"""print('----1----')
g1 = gevent.spawn(test1, 5)
print('----2----')
g2 = gevent.spawn(test2, 5)
print('----3----')
g3 = gevent.spawn(test3, 5)
print('----4----')

g1.join()
g2.join()
g3.join()"""

