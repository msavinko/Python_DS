#!/bin/sh

OUTFILE='concatenator.csv'

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $OUTFILE
cat 2022*.csv | sed -En '/^"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"$/!p' >> $OUTFILE
