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

import random
import csv

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
	all_dates=""
	for date in dates:
		all_dates += "Date:"+date+'\n'
	return jsonify({'info': all_dates})
	
@app.route('/historical/<date_id>',methods=['GET'])
def get_date(date_id):
	try:
		value = dates.index(date_id)
		info_message = "Date:"+dates[value]+" TMAX:"+TMAXs[value]+" TMIN:"+TMINs[value]
		return (jsonify({'info': info_message}))
	except:
		error_message = "HTTP Error code 404"
		return (jsonify({'error': error_message}))

@app.route('/historical/data_info',methods=['POST'])
def post_date(date_info):
	print date_info
	#TO ADD: get date info to give a date, tmax and tmin
	with open(r'daily.csv','a') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow([])
		spamwriter.writerow([date,tmax,tmin])

@app.route('/forecast/<date_id>',methods=['GET'])
def get_forecast(date_id):
	try:
		value = dates.index(date_id)
		new_days = []
		t_max = TMAXs[value]
		t_min = TMINs[value]
		forecast = []
		fun_string = 'Date:'+str(dates[value])
		fun_string +=' TMAX:'+str(t_max)
		fun_string +=' TMIN:'+str(t_min)+'\n'
		forecast.append(fun_string)
		for x in range(1,8):
			new_days.append(int(dates[value])+x)
		for x in new_days:
			new_tmax = int(t_max)+random.randint(-3,3)
			new_tmin = int(t_min)+random.randint(-3,3)
			forecast_string = 'Date:'+str(x)
			forecast_string +=' TMAX:'+str(new_tmax)
			forecast_string +=' TMIN:'+str(new_tmin)+'\n'
			forecast.append(forecast_string)
		info_message = ''
		for x in forecast:
			info_message+=x
		return (jsonify({'info': info_message}))
	except:
		error_message = 'HTTP Error code 404'
		return jsonify({'error':error_message})

if __name__ == "__main__":
	app.run(host='0.0.0.0')
