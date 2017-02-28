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
import json
import random
import csv
import os
import re

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

del dates[0]
del TMAXs[0]
del TMINs[0]

@app.route("/historical")
# five test cases: n=10, n=-1, no parameter, malformed parameters
def historical():	
	json_list = []
	for date in dates:
		json_list.append({'Date':date})
	return json.dumps(json_list)
	
@app.route('/historical/<date_id>',methods=['GET'])
def get_date(date_id):
	try:
		json_list = []
		value = dates.index(date_id)
		json_list.append({"Date":dates[value]})
		json_list.append({"TMAX":TMAXs[value]})
		json_list.append({"TMIN":TMINs[value]})
		return json.dumps(json_list)
	except:
		error_message = "HTTP Error code 404"
		return (jsonify({'error': error_message}))

@app.route('/historical/<data_info>',methods=['POST'])
def post_date(data_info):
	date, temp_tmax, temp_tmin= request.get_data().split(',')
	date_value = re.findall(r'\d+', date)
	tmax_value = re.findall(r'\d+',temp_tmax)
	tmin_value = re.findall(r'\d+',temp_tmin)
	date_value = date_value[0]
	tmax_value = tmax_value[0]
	tmin_value = tmin_value[0]
	with open(r'daily.csv','a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([])
                spamwriter.writerow([str(date_value),str(tmax_value),str(tmin_value)])	
	return (jsonify({'Post':'Response'}))

@app.route('/historical/<data_id>',methods=['DELETE'])
def delete_date(data_id):
	inputCSV=open('daily.csv','rb')
	outputCSV=open('daily2.csv','wb')
	writer=csv.writer(outputCSV)
	deleted = False
	for row in csv.reader(inputCSV):
		if row[0]!='DATE':
			if row[0] != data_id:
				writer.writerow(row)
			else:
				value = dates.index(date_id)
				del dates[value]
				del TMAXs[value]
				del TMINs[value]
				deleted=True
	os.system('cp daily2.csv daily.csv')
	return jsonify({'Deleted Result':deleted})	


@app.route('/forecast/<date_id>',methods=['GET'])
def get_forecast(date_id):
	try:
		value = dates.index(date_id)
		new_days = []
		t_max = TMAXs[value]
		t_min = TMINs[value]
		forecast = []
		fun_string =[]
		fun_string.append({'Date':str(dates[value])})
		fun_string.append({'TMAX':str(t_max)})
		fun_string.append({'TMIN':str(t_min)})
		forecast.append(fun_string)
		for x in range(1,8):
			new_days.append(int(dates[value])+x)
		for x in new_days:
			new_tmax = int(t_max)+random.randint(-3,3)
			new_tmin = int(t_min)+random.randint(-3,3)
			forecast_string = []
			forecast_string.append({'Date':str(x)})
			forecast_string.append({'TMAX':str(new_tmax)})
			forecast_string.append({'TMIN:':str(new_tmin)})
			forecast.append(forecast_string)
		return json.dumps(forecast)
	except:
		error_message = 'HTTP Error code 404'
		return jsonify({'error':error_message})

if __name__ == "__main__":
	app.run(host='0.0.0.0')
