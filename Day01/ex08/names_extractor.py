import sys

def extract():
	with open('employees.tsv', 'a') as write_file: #now we open a new doc and write into in
		write_file.write('Name\tSurname\tEmail\n') #header
		with open(sys.argv[1], 'r') as read_file:
			line = read_file.readlines() #we read all file wiht \n delimeter
			for line_num in range(len(line)):
				name = line[line_num].split('@')[0].split('.')[0]
				surname = line[line_num].split('@')[0].split('.')[1]
				write_file.write(f'{name.capitalize()}\t{surname.capitalize()}\t{line[line_num]}')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise Exception('Wrong args')
	extract()