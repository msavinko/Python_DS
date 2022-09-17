def open_n_write():
	read_file = open('ds.csv', 'r')
	write_file = open('ds.tsv', 'w') #creates the file if does not exist
	write_file.write(read_file.read().replace('\",\"', '\"\t\"'))

if __name__ == '__main__':
	open_n_write()
