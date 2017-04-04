#!/usr/bin/env python

import sys
import csv

isFirst = True

for row in csv.reader(iter(sys.stdin.readline, '')):
        if isFirst :
                isFirst = False
                continue
        else:
                if(row[24]):
                        print '%s\t%s' % (row[24].replace(',',''),1)
                if(row[25]):
                        print '%s\t%s' % (row[25].replace(',',''),1)
                if(row[26]):
                        print '%s\t%s' % (row[26].replace(',',''),1)
                if(row[27]):
                        print '%s\t%s' % (row[27].replace(',',''),1)
                if(row[28]):
                        print '%s\t%s' % (row[28].replace(',',''),1)
                                                          





