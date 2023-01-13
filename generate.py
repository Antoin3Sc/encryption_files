import main

key = Fernet.generate_key()
with open('.key', 'wb') as filekey:
	filekey.write(key)