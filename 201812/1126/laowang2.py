class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.gun = None
		self.hp = 100
	def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
		dan_jia_temp.baocun_zidan(zi_dan_temp)
	def anzhuang_danjia(self,gun_temp, dan_jia_temp):
		gun_temp.baocun_danjia(dan_jia_temp)
	def naqiang(self, gun_temp):
		self.gun = gun_temp
	def __str__(self):
		if self.gun:
			return "%sxueliang :%d, tayouqiang"%(self.name, self.hp)
		else:
			return "%sxueliang :%d, meiqiang"%(self.name, self.hp)

class Gun(object):
	"""docstring for Gun"""
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name
		self.danjia = None
	def baocun_danjia(self, dan_jia_temp):
		self.danjia = dan_jia_temp
	def __str__(self):
		return 'qiang is:%s'%(self.name)

class Danjia(object):
	"""docstring for Danjia"""
	def __init__(self, max_num):
		super(Danjia, self).__init__()
		self.max_num = max_num
		self.zidan_list = []

	def baocun_zidan(self, zi_dan_temp):
		self.zidan_list.append(zi_dan_temp)
	def __str__(self):
		return "danjia:%d/%d"%(len(self.zidan_list), self.max_num)
		
class Zidan(object):
	"""docstring for Zidan"""
	def __init__(self, sha_shang_li):
		super(Zidan, self).__init__()
		self.sha_shang_li = sha_shang_li
			
def main():
	pass
	#1.create obj
	laowang = Person('focus')

	#2.qiang
	ak47 = Gun('AK47')

	#3.danjia
	dan_jia = Danjia(20)

	#4.zidan
	zi_dan = Zidan(10)

	#5.diren

	#6.zidan---danjia
	laowang.anzhuang_zidan(dan_jia, zi_dan)

	#7.danjia---qiang
	laowang.anzhuang_danjia(ak47, dan_jia)

	print(dan_jia)
	print(ak47)
	#8.naqiang
	laowang.naqiang(ak47)
	print(laowang)

	#9.dadiren 



if __name__ == '__main__':
	main()