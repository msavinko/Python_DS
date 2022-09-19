import sys
import os

class Research:
	def __init__(self, file_name):
		self.file_name = file_name

	def file_reader(self, has_header = True):
		with open(self.file_name, 'r') as file:
			line = file.readlines()
			if line[0] == '0,1\n' or line[0] == '1,0\n':
				has_header = False # does not have header
			start_line = 0
			if has_header == True: #has header
				start_line = 1
			list_lists = []
			for i in range(start_line, len(line)):
				list_i = [int(line[i][0])]
				list_i.append(int(line[i][2]))
				list_lists.append(list_i)
			return(list_lists)

	class Calculations:
		def counts(list_lists):
			heads = 0
			tails = 0
			for i in range(len(list_lists)):
				if list_lists[i][0] == 1:
					heads += 1
				else: 
					tails += 1
			return (heads, tails)

		def fractions(list_counts):
			sum = list_counts[0] + list_counts[1]
			return (list_counts[0] / sum, list_counts[1] / sum)


def check_arg(file_name):
	try:
		with open(file_name, 'r') as filename:
			line = filename.readlines()
	except Exception as e:
		raise Exception("Unable to open this file")
	else: 
		if not line:
			raise Exception("File is empty")
		if len(line) < 2 or len(line[0].split(',')) !=2:
			raise Exception("Wrong header")
		for i in range(1, len(line)):
			if line[i][0:4] != '0,1\n' and line[i][0:4] != '1,0\n' and line[i][0:4] != '1,0' and line[i][0:4] != '1,0':
				raise Exception("Wrong data")

if __name__ == '__main__':
	try:
		if len(sys.argv) != 2:
			print("Wrong num of args")
		check_arg(sys.argv[1])
	except Exception as e: 
		print(e)
	else:
		list_lists = Research(sys.argv[1]).file_reader()
		print(list_lists)
		list_counts = Research.Calculations.counts(list_lists)
		print(list_counts[0], list_counts[1])
		list_fractions = Research.Calculations.fractions(list_counts)
		print(list_fractions[0], list_fractions[1])