from Crypto.PublicKey import RSA
def generateKeys():
	# Generate two pair keys
	key = RSA.generate(2048)

	# secretCode
	secretCode = "12345"

	# Export the private key
	privateKey = key.export_key(passphrase=secretCode)

	# Save on a file
	with open("private.pem", "wb") as file:
	    f.write(privateKey)

	# Export the public key
	publicKey = key.publickey().export_key()

	# Save on a file 
	with open("public.pem", "wb") as file:
	    file.write(publicKey)


def encryptMessage(message):
	bin_data = message.encode("utf-8")
	# Reading public key 
	with open("public.pem", "rb") as f:
	    recipient_key = f.read()

	# We load the public key
	key = RSA.importKey(recipient_key)

	# Encrypter
	cipher_rsa = PKCS1_OAEP.new(key)

	# We encrypt the message
	enc_data = cipher_rsa.encrypt(bin_data)
	return enc_data

def decryptMessage(message):
	with open("private.pem", "rb") as f:
    recipient_key = f.read()
	# We load the private key
	key = RSA.importKey(recipient_key, passphrase="12345")

	# Instancia del cifrador asimétrico
	cipher_rsa = PKCS1_OAEP.new(key)

	# we decrypt with the private key
	dec_data = cipher_rsa.decrypt(message)

	# Decode the string
	cadena = message.decode("utf-8")
	return cadena
