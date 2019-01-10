from socket import *

def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	udp_socket.close()
	print('---run---')

if __name__ == "__main__":
	main()