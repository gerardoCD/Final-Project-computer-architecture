import socket
import SecurityModule
def beginConnection(ip,port):
	#Build my socket
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Add our ip and port 
	mySocket.bind((ip, port))
	#We can listen uo to 5
	mySocket.listen(5)
	print("Welcome")

	while True:
		print("Wating conection")
		#Accept the conection, The sc is Client's socket  
		sc, addr = mySocket.accept()
		print("Client connected from: ", addr)
		while True:
			received = sc.recv(2048)
			receivedDecrypt = SecurityModule.decryptMessage(received)
			if received == "CONSULTA":
				pass
			elif received == "DEPOSITAR":
				pass
			elif received == "RETIRAR":
				pass
			elif received == "EXIT":
				break
	sc.close()
	s.close()
if __name__ == '__main__':
	if len(sys.argv)<3:
		print("Rememeber following the format [Ip] [Port]")
	else:
		SecurityModule.generateKeys()
		beginConnection(sys.argv[1],int(sys.argv[2]))