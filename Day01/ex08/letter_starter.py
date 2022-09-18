import sys

def letter_starter():
	with open('employees.tsv', 'r') as f_read:
		line = f_read.readlines()
		name = ''					#if email does not exist
		for i in range(len(line)):
			if line[i].split('\t')[2] == sys.argv[1] + '\n':
				name = line[i].split('\t')[0]
		if name == '':
			print('Error email')
			return
		print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That\'s a precondition for the professionals that our company hires.')

if __name__ == '__main__':
	if len (sys.argv) != 2:
		raise Exception("Error argument")
	letter_starter()
