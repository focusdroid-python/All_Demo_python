import socket


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	udp_socket.sendto(b"hahahhahah",("192.168.2.2", 8080))

	udp_socket.close()





if __name__ == 'main':
	main()
