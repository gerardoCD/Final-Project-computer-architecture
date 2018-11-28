class Usuario:
	dineroTotal = 0 
	def __init__(self, user, password):
		self.user = user
		self.password = password
def loggin(listUser,user, password):
	for llave,valor in listUser.items():
		if valor.user == user and valor.password == password:
			return True
			break
	return False 