from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5
def generateKeys():
	# Generate two pair keys
	key = RSA.generate(5120)

	# secretCode
	secretCode = "12345"

	# Export the private key
	privateKey = key.exportKey(passphrase=secretCode)

	# Save on a file
	with open("private.pem", "wb") as file:
	    file.write(privateKey)

	# Export the public key
	publicKey = key.publickey().exportKey()

	# Save on a file 
	with open("public.pem", "wb") as file:
	    file.write(publicKey)


def encryptMessage(message):
	bin_data = message.encode("utf-8")

	# Leemos el archivo con la clave publica
	with open("public.pem", "rb") as f:
	    recipient_key = f.read()

	# Cargamos la clave pública (instancia de clase RSA)
	key = RSA.importKey(recipient_key)

	# Instancia del cifrador asimétrico
	cipher_rsa = PKCS1_OAEP.new(key)

	# Encriptamos la cadena usando la clave pública
	enc_data = cipher_rsa.encrypt(bin_data)
	return enc_data

def decryptMessage(enc_data):
	# Leemos el archivo con la clave privada
	with open("private.pem", "rb") as f:
	    recipient_key = f.read()

	# Cargamos la clave privada (instancia de clase RSA)
	key = RSA.importKey(recipient_key, passphrase="12345")

	# Instancia del cifrador asimétrico
	cipher_rsa = PKCS1_OAEP.new(key)

	# Desencriptamos la cadena usando la clave privada
	dec_data = cipher_rsa.decrypt(enc_data)

	# Decodificamos la cadena
	cadena = dec_data.decode("utf-8")

	return cadena