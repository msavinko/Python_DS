class Must_read:
	with open('data.csv', 'r') as read_file:
		print(read_file.read())

if __name__ == '__main__':
	Must_read()