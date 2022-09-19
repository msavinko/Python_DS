class Research:
	def file_reader():
		with open('data.csv', 'r') as read_file:
			return(read_file.read())

if __name__ == '__main__':
	print(Research.file_reader())
