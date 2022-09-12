#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
	if os.getenv("VIRTUAL_ENV") is None:
		print('You are not in the Virtual Environment')
	else:
		print('Virtual Environment is OK')
		# USE ANY OF THESE

		subprocess.call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "PyTest"])
		subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=open("requirements.txt", "w"))
		subprocess.run(["cat", "requirements.txt"])

		# OR
		# os.system('pip3 install -r requirements.txt')
		# os.system("pip3 freeze > requirements.txt")
		# os.system("cat requirements.txt")

if __name__ == '__main__':
	main()