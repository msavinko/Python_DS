#!/bin/sh

FILE='../ex03/hh_positions.csv'

echo "\"name\"","\"count\"" > hh_uniq_positions.csv
(tail -n +2 $FILE | \
awk 'BEGIN { FS = OFS = "," }
    {
        if (index($3, "Junior"))
            JUN++
        if (index($3, "Middle"))
            MID++
        if (index($3, "Senior"))
            SEN++
    }
    END { print "\"Junior\"", 
                JUN "\n\"Middle\"", 
                MID "\n\"Senior\"", SEN }
    ') | \
    sort -t',' -nk2\
    >>  hh_uniq_positions.csv