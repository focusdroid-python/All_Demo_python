import re


def main():
	names = ["age", "_age", "1age", "age1", "a_age", "age_1", "age!", "a#123", "------"]

	for name in names:
		ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
		if ret:
			print('---%s----ok--%s' % (name, ret.group()))
		else:
			print('----%s---err' % name)


if __name__ == '__main__':
	main()