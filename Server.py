import socket, sys
import SecurityModule
import ModelData
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
			if ModelData.loggin(listUsers,receivedDecryptArray[0], receivedDecryptArray[1]):
				if (receivedDecryptArray[2] == "CONSULTA"):
					for llave,valor in listUsers.items():
						if valor.user  == receivedDecryptArray[0] and valor.password == receivedDecryptArray[1]:
							stringSend = "Your total account is:  " + str(valor.dineroTotal)
							sc.send(stringSend.encode("utf-8"))
				elif receivedDecryptArray[2] == "DEPOSITAR":
					print(len(receivedDecryptArray))
					if len(receivedDecryptArray) > 3:
						for llave,valor in listUsers.items():
							if valor.user  == receivedDecryptArray[0] and valor.password == receivedDecryptArray[1]:
								valor.dineroTotal += int(receivedDecryptArray[3])
								stringSend = "Your deposit was successful  "
								sc.send(stringSend.encode("utf-8"))
					else:
						stringSend = "Your nedd put the next format: DEPOSITAR [CANTIDAD A DEPOSITAR]"
						sc.send(stringSend.encode("utf-8"))	
				elif receivedDecryptArray[2] == "RETIRAR":
					print(len(receivedDecryptArray))
					if len(receivedDecryptArray) > 3:
						for llave,valor in listUsers.items():
							if valor.user  == receivedDecryptArray[0] and valor.password == receivedDecryptArray[1]:
								if valor.dineroTotal >= int(receivedDecryptArray[3]):
									valor.dineroTotal -= int(receivedDecryptArray[3])
									stringSend = "Your total account is:  " + str(valor.dineroTotal)
									sc.send(stringSend.encode("utf-8"))
								else:
									stringSend = "Your dont have so much  money" 
									sc.send(stringSend.encode("utf-8"))
					else:
						stringSend = "Your nedd put the next format: RETIRAR [CANTIDAD A RETIRAR]"
						sc.send(stringSend.encode("utf-8"))	
				elif receivedDecryptArray[2] == "EXIT":
					sc.send("EXIT".encode("utf-8"))			
					break		
				else:
					stringSend = "This option is not correct " 
					sc.send(stringSend.encode("utf-8"))
			else:
				sc.send("Wrong, user and password are incorrect".encode("utf-8"))
	sc.close()
	s.close()
if __name__ == '__main__':
	if len(sys.argv)<3:
		print("Rememeber following the format [Ip] [Port]")
	else:
		SecurityModule.generateKeys()
		beginConnection(sys.argv[1],int(sys.argv[2]))