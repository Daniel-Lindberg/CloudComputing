import csv
import re

date = []
TMAX = []
TMIN = []
with open('daily.csv','rb') as csvfile:
	spamreader=csv.reader(csvfile,delimiter=' ',quotechar="|")
	for row in spamreader:	
		for column in row:
			splitStr = (column.split(","))
			date.append(splitStr[0])
			TMAX.append(splitStr[1])
			TMIN.append(splitStr[2])


del date[0]
del TMAX[0]
del TMIN[0]
print "Date:", date
print "Tmax:",TMAX
print "Tmin:",TMIN					
