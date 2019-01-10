import threading
import time



class MyThread(threading.Thread):
	def run(self):
		for i in range(2000):
			time.sleep(1)
			msg = "I'm"+self.name+' @ '+str(i)
			print(msg)
			print(self.name)




if __name__ == '__main__':
	t1 = MyThread()
	t2 = MyThread()
	t1.start()
	t2.start()