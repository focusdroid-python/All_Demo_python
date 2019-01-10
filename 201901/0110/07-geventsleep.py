import gevent

def test1(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		gevent.sleep(0.5)

def test2(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		gevent.sleep(1)

def test3(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		gevent.sleep(0.5)

print('----1----')
g1 = gevent.spawn(test1, 5)
print('----2----')
g2 = gevent.spawn(test2, 5)
print('----3----')
g3 = gevent.spawn(test3, 5)
print('----4----')

g1.join()
g2.join()
g3.join()

