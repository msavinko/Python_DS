import sys

def caesar(type, text, num):
	new_string = ''
	low_alpha = 'abcdefghijklmnopqrstuvwxyz'
	upp_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if type == 'decode':
		num *= -1
	for i in range(len(text)):
		if text[i] in low_alpha:
			letter = low_alpha.find(text[i])
			new_string += low_alpha[(num + letter) % len(low_alpha)]
		elif text[i] in upp_alpha:
			letter = upp_alpha.find(text[i])
			new_string += upp_alpha[(num + letter) % len(upp_alpha)]
		else:
			new_string += text[i]
	print(new_string)
if __name__ == '__main__':
	if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode') or (not sys.argv[2].isascii()) or (not sys.argv[3].isnumeric()):
		raise Exception('Wrong args')
	caesar(sys.argv[1],sys.argv[2],int(sys.argv[3]))
