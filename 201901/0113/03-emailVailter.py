import re

def main():
	email = input("input on email : ")
	ret = re.match(r"^[a-zA-Z_0-9]{4,20}@[a-zA-Z0-9]{2,8}\.com$", email)
	if ret:
		print('------------ok-%s-------' % email)
	else:
		print('---err-----%s---' % email)





if __name__ == '__main__':
	main()