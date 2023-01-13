import main, cryptograph

files = main.files_list()
for file in files:
	cryptograph.crypt(file, encrypted = False)
print("%s files has been decrypted" %len(files))