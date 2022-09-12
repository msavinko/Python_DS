# pip3 install virtualenv
# mkdir virtual
# python3 -m venv marlean
# cd bin
# source activate
# cd ../include
# python3 venv.py
# deactivate

import os

if __name__ == '__main__':
	print("Your current virtual env is: " + os.getcwd())