import socket


def beginClient(ip,port,fileName):
	socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketClient.connect((ip, port))
	while True:
			user = str(input(">> "))
			password = str(input(">> "))
	        instruction  = str(input(">> "))
	        message = "{} {} {}".format(user,password,message)
	        socketClient.send(message.encode('utf-8'))
	        received = socketClient.recv(1024)
	        print("received", received)
	socketClient.close()


if __name__ == '__main__':
	if len(sys.argv)<3:
		print("Rememeber following the format [Ip] [Port] [key]")
	else:
		eginClient(sys.argv[1],int(sys.argv[2]),sys.argv[3])