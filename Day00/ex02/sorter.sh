#!/bin/sh

INFILE='../ex01/hh.csv'
OUTFILE='hh_sorted.csv'

head -n 1 $INFILE > $OUTFILE;
tail -n +2 $INFILE | sort -t, -k2 -k1 >> $OUTFILE;


# -n num of lines
# -n +2 start from line 2, included
# -t separator
# -k key KEYDEF gives location