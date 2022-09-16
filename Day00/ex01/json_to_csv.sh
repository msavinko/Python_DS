#!/bin/sh

INFILE='../ex00/hh.json'
JQ="/Users/marlean/homebrew/bin/jq"

$JQ -rf filter.jq $INFILE > hh.csv

# -f filename
# -r raw-output. write directly to standard output