import os, \
	yaml
from cryptography.fernet import Fernet
from yaml.loader import SafeLoader

def get_exluded_files() -> list:
	data = get_config()
	return data["excluded_files"]

def get_dir_path() -> str:
	data = get_config()
	return data["dir_path"]

def get_config() -> list:
	with open('config.yaml') as f:
		return yaml.load(f, Loader=SafeLoader)

def files_list() -> list:
	files = []
	dir_path = get_dir_path()

	for path in os.listdir(dir_path):
		# Test if path is not excluded
		exclude_files = get_exluded_files()
		if path not in exclude_files:
			file_name = os.path.join(dir_path, path)
			if os.path.isfile(file_name):
				files.append(file_name)
	return files

def get_key() -> str:
	with open('./.key', 'rb') as filekey:
		key = filekey.read()
		return Fernet(key)

def get_file_infos(file) -> dict:
	file_object = open(file, 'rb')
	content = file_object.read()
	file_path = os.path.realpath(file)
	file_name = os.path.basename(file)
	path = os.path.dirname(file_path)

	return {
		'name': file_name,
		'content': content,
		'path': path,
	}