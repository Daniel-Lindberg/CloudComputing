##############################################################
# 
# fnoc.py
#
# calculates a Fibonacci sequence using a web service
# takes a single integer on the URL and reports the 
# series as JSON so people might actually use it
#
#    a call URL http://domain.com/fibonacci?n=10
#
#    should return the following JSON document:
#
#    { "Fibonacci": [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ] }
#
#
##############################################################
from flask import Flask, jsonify, request

app = Flask(__name__)

app.config.from_envvar('FNOC_SETTINGS', silent=True)
import sys
import random
import csv
import os
import re
import json

def readCSV():
	dates = []
	TMAXs = []
	TMINs = []
	with open('daily.csv','rb') as csvfile:
        	spamreader=csv.reader(csvfile,delimiter=' ',quotechar="|")
       		for row in spamreader:
                	for column in row:
                        	splitStr = (column.split(","))
                       		dates.append(splitStr[0])
                       		TMAXs.append(splitStr[1])
                       		TMINs.append(splitStr[2])
	return dates,TMAXs,TMINs

@app.route("/historical/")
# five test cases: n=10, n=-1, no parameter, malformed parameters
def historical():
	dates,TMAXs,TMINs = readCSV()	
	json_list = []
	for date in dates:
		json_list.append({'DATE':date})
	return jsonify(json_list)
	
@app.route('/historical/<date_id>',methods=['GET'])
def get_date(date_id):
	dates,TMAXs,TMINs = readCSV()
	try:
		value = dates.index(date_id)
		return jsonify({'DATE':dates[value],'TMAX':float(TMAXs[value]),'TMIN':float(TMINs[value])})
	except:
		error_message = 'HTTP Error code 404'
		return (jsonify({'error': error_message}),404)

@app.route('/historical/',methods=['POST'])
def post_date():
	data= request.get_json()
	date_value = data['DATE']
	tmax_value = data['TMAX']
	tmin_value = data['TMIN']
	with open(r'daily.csv','a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([])
                spamwriter.writerow([str(date_value),str(tmax_value),str(tmin_value)])	
	return (jsonify({'DATE':(date_value),'TMAX':int(tmax_value),'TMIN':int(tmin_value)}),201)

@app.route('/historical/<data_id>',methods=['DELETE'])
def delete_date(data_id):
	dates,TMAXs,TMINs = readCSV()
	deleted = False
	csvfile=open('daily2.csv','wt')
	try:
		writer = csv.writer(csvfile)
		value = dates.index(data_id)
		del dates[value]
		del TMAXs[value]
		del TMINs[value]
		deleted = True
		for index in range(0 ,len(dates)):
			writer.writerow(([dates[index],TMAXs[index],TMINs[index]]))
		csvfile.close();	
		os.system('cp daily2.csv daily.csv')
		return jsonify({'Deleted Result': deleted})		
	except Exception as inst:
		return jsonify({'Error':'Value does not exit'})
	


@app.route('/forecast/<date_id>',methods=['GET'])
def get_forecast(date_id):
	dates,TMAXs,TMINs = readCSV()
	try:
		value = dates.index(date_id)
		new_days = []
		t_max = TMAXs[value]
		t_min = TMINs[value]
		forecast = []
		date_return = []
		tmax_return = []
		tmin_return = []
		date_return.append(str(dates[value]))
		tmax_return.append(str(t_max))
		tmin_return.append(str(t_min))
		for x in range(1,8):	
			new_days.append(int(dates[value])+x)
		for x in new_days:
			new_tmax = float(t_max)+random.randint(-3,3)
			new_tmin = float(t_min)+random.randint(-3,3)
			date_return.append(str(x))
			tmax_return.append(float(new_tmax))
			tmin_return.append(float(new_tmin))
		return jsonify({'DATE':date_return[0], 'TMAX':tmax_return[0],'TMIN':tmin_return[0],'DATE':date_return[1], 'TMAX':tmax_return[1],'TMIN':tmin_return[1],'DATE':date_return[2], 'TMAX':tmax_return[2],'TMIN':tmin_return[2],'DATE':date_return[3], 'TMAX':tmax_return[3],'TMIN':tmin_return[3],'DATE':date_return[4], 'TMAX':tmax_return[4],'TMIN':tmin_return[4],'DATE':date_return[5], 'TMAX':tmax_return[5],'TMIN':tmin_return[5],'DATE':date_return[6], 'TMAX':tmax_return[6],'TMIN':tmin_return[6],'DATE':date_return[7], 'TMAX':tmax_return[7],'TMIN':tmin_return[7]})
	except:
		error_message = 'HTTP Error code 404'
		return jsonify({'error':error_message},404)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
