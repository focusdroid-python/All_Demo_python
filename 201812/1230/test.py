import socket
import threading


def recv_msg(udp_socket,):
	while True:
		recv_data = udp_socket.recvfrom(1024)
		print(recv_data)

def send_msg(udp_socket, dest_ip, dest_port):
	while True:
		send_data = input('input data ... ')
		udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	udp_socket.bind(("", 7890))

	dest_ip = input('you ip is ')
	dest_port = int(input('you port: '))
	
	# create thread
	t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
	t2 = threading.Thread(target=send_msg, args=(udp_socket,))

	t1.start()
	t2.start()

if __name__ == '__main__':
	main()