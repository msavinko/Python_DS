#!/bin/sh

FILE='../ex02/hh_sorted.csv'

head -n 1 $FILE > hh_positions.csv
tail -n +2 $FILE | \
awk 'BEGIN { FS = OFS = "," } 
	{
		STR = ""
		if (index(tolower($3), "junior"))
			STR = STR"Junior/"
		if (index(tolower($3), "middle"))
			STR = STR"Middle/"
		if (index(tolower($3), "senior"))
			STR = STR"Senior"
		if (STR == "")
			STR = "-"
		gsub(/[\/ ]*$/, "", STR)
		
		$3 = "\""STR"\""
		print
	}' \
	>> hh_positions.csv
# FS: field separator, Разделитель полей, используемый при чтении файла
# OFS: Output Filed Separator:
# gsub - метод подстановки