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

	# We read the file with the public key
	with open("public.pem", "rb") as f:
	    recipient_key = f.read()

	# We load the public key (RSA class instance)
	key = RSA.importKey(recipient_key)

	# Instance of asymmetric encryption
	cipher_rsa = PKCS1_OAEP.new(key)

	# We encrypt the string using the public key
	enc_data = cipher_rsa.encrypt(bin_data)
	return enc_data

def decryptMessage(enc_data):
	# We read the file with the private key
	with open("private.pem", "rb") as f:
	    recipient_key = f.read()

	# We load the private key (RSA class instance)
	key = RSA.importKey(recipient_key, passphrase="12345")

	# Instance of asymmetric encryption
	cipher_rsa = PKCS1_OAEP.new(key)

	# We decrypt the chain using the private key
	dec_data = cipher_rsa.decrypt(enc_data)

	# Decode the string
	cadena = dec_data.decode("utf-8")

	return cadenas