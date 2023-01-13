import main, os

def crypt(file, encrypted: bool) -> None:
	fernet = main.get_key()
	file_infos = main.get_file_infos(file)

	if encrypted:
		content = fernet.encrypt(file_infos["content"])
		file_name = fernet.encrypt(file_infos["name"].encode())
	else:
		content = fernet.decrypt(file_infos["content"])
		file_name = fernet.decrypt(file_infos["name"].encode())

	file_path = file_infos["path"] + '/' + file_name.decode()

	with open(file_path, 'wb') as encrypted_file:
		encrypted_file.write(content)

	os.remove(os.path.join(file_infos["path"], file_infos["name"]))
