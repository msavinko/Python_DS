import sys

class Research:
	def __init__(self, file_name):
		self.file_name = file_name

	def file_reader(self):
		# try:
		with open(self.file_name, 'r') as file:
			# if not file:
			# 	raise Exception()
			return(file.read())
		# except:
			# return('Unable to open the file')

def check_arg(file_name):
	try:
		file = Research.file_reader(file_name)
		if not file:
			raise Exception('Unable to open the file')
		if len(file) < 2 or len(file[0].split(',')) !=2:
			print('1')
			raise Exception()
		for i in range(1, len(file) - 1):
			if file[i] != '0,1\n' and file[i] != '1,0\n':
				print('2')
				raise Exception()
	except:
		# print(error)
		print('Wrong data in the file')
	

if __name__ == '__main__':
	if len (sys.argv) != 2:
		raise Exception('Wrong num of arg')
	try:
		if check_arg(sys.argv[1]):
			print(Research(sys.argv[1]).file_reader())
	except:
		print('ERROR')
	