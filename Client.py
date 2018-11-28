import socket,sys
import SecurityModule

def beginClient(ip,port,fileName):
	socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketClient.connect((ip, port))
	while True:
		user = str(input("User:  "))
		password = str(input("Password: "))
		instruction  = str(input(">> "))
		message = "{} {} {}".format(user,password,instruction.upper())
		encryptMessage = SecurityModule.encryptMessage(message)
		socketClient.send(encryptMessage)
		received = socketClient.recv(2048)
		if received == "EXIT":
			break
		else:
			print(received.decode("utf-8"))
	socketClient.close()


if __name__ == '__main__':
	if len(sys.argv)<3:
		print("Rememeber following the format [Ip] [Port] [key]")
	else:
		beginClient(sys.argv[1],int(sys.argv[2]),sys.argv[3])