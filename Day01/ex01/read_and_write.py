def open_n_write():
	read_file = open('ds.csv', 'r')
	write_file = open('ds.tsv', 'w') #creates the file if does not exist
	write_file.write(read_file.read()
	.replace('\",\"', '\"\t\"')
	.replace(',false', '\tfalse')
	.replace(',true', '\ttrue')
	.replace(',\"', '\t\"')
	)

	read_file.close()
	write_file.close()

if __name__ == '__main__':
	open_n_write()