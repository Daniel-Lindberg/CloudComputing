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

#import random
#print random.randint(0,3)

date = '20150820'
input1 = open('daily3.csv','rb')
output = open('daily3.csv','wb')
writer=csv.writer(output)
for row in csv.reader(input1):
	if row[0] != date:
		writer.writerow(row)
		
"""
with open(r'daily3.csv','a') as csvfile:
	spamwriter=csv.writer(csvfile)
	spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
	for row in spamreader:
		print row
		if row[0] == date:
			print 'hello world'
	#spamwriter.writerow(['20170227','34','27'])
					
"""
