import socket, sys
import SecurityModule
from ModelData import Usuario
listUsers = {"Gerardo": Usuario("Gerardo","1234"),"Ricardo": Usuario("Ricardo","1234")}
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
			print(receivedDecrypt)
			receivedDecryptArray = receivedDecrypt.split(" ")
			print(receivedDecryptArray)
			if (receivedDecryptArray[2] == "CONSULTA"):
				for llave,valor in listUsers.items():
					if valor.user == receivedDecryptArray[0] and valor.password == receivedDecryptArray[1]:
						stringSend = "Your total account is:  " + str(valor.dineroTotal)
						sc.send(stringSend.encode("utf-8"))
					else:
						sc.send("Wrong in user and password".encode("utf-8"))

			elif receivedDecryptArray[2] == "DEPOSITAR":
				for llave,valor in listUsers.items():
					if valor.user == receivedDecryptArray[0] and valor.password == receivedDecryptArray[1]:
						valor.dineroTotal += int(receivedDecryptArray[3])
						stringSend = "Your total account is:  " + str(valor.dineroTotal)
						sc.send(stringSend.encode("utf-8"))
					else:
						sc.send("Wrong in user and password".encode("utf-8"))
				
			elif receivedDecryptArray[2] == "RETIRAR":
				for llave,valor in listUsers.items():
					if valor.user == receivedDecryptArray[0] and valor.password == receivedDecryptArray[1]:
						if valor.dineroTotal >= int(receivedDecryptArray[3]):
							valor.dineroTotal -= int(receivedDecryptArray[3])
							stringSend = "Your total account is:  " + str(valor.dineroTotal)
							sc.send(stringSend.encode("utf-8"))
						else:
							stringSend = "Your dont have so much  money" 
							sc.send(stringSend.encode("utf-8"))
					else:
						sc.send("Wrong in user and password".encode("utf-8"))
			elif receivedDecryptArray[2] == "EXIT":
				sc.send("EXIT".encode("utf-8"))
			else:
				sc.send("EXIT".encode("utf-8"))
	sc.close()
	s.close()
if __name__ == '__main__':
	if len(sys.argv)<3:
		print("Rememeber following the format [Ip] [Port]")
	else:
		SecurityModule.generateKeys()
		beginConnection(sys.argv[1],int(sys.argv[2]))