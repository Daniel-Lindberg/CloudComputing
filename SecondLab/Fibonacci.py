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
		all_dates += "Date:"+date+"\n"
	return jsonify({'info': all_dates})
	
@app.route('/historical/<date_id>',methods=['GET'])
def get_date(date_id):
	try:
		value = dates.index(date_id)
		info_message = "Date:"+dates[value]+" TMAX:"+TMAXs[value]+" TMIN:"+TMINs[value]
		return(jsonify({'info': info_message}))
	except:
		error_message = "HTTP Error code 404"
		return(jsonify({'error': error_message}))

@app.route("/fibonacci")

def fibonacci():

    def fibons (x):
       if x < 0: return []
       flist = [0, 1, 1] 
       y, z = 1,1
       if x >= 2: 
          for i in range (x-2): 
              z, y = y+z, z
              flist.append(z)
       return flist[0:x] 

    error_message = ""

    try: n = int(request.args.get('n'))
    except: 
        error_message = "use: domain/fibonacci?n=N where N is a positive integer"
        return(jsonify({'error': error_message}))
    return (jsonify({'Fibonacci':fibons(n)}))
    if n < 0: 
        error_message = "requested negative length Fibonacci sequence"
        return(jsonify({'error': error_message}))
    elif n > FIBONACCI_SEQUENCE_LIMIT: 
        error_message = "truncated Fibonacci sequence at 20000"
        n=FIBONACCI_SEQUENCE_LIMIT

    return(jsonify({'error': error_message,'Fibonacci':fibons(n)}))

if __name__ == "__main__":
	app.run(host='0.0.0.0')
