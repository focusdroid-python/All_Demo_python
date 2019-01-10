import socket


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	udp_socket.bind(("", 7890))

	


if __name__ == '__main__':
	main()