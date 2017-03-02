Second Lab
Daniel Lindberg
03.02.2017


URL: 52.33.88.132:5000
-------------------------------------------------------------------
First virtual path: /historical

Method:historical()

Request type:GET 

URL Params: none

Required:None

Code: 200 
Content: { [{"Date": "20130101"}, {"Date": "20130102"}, {"Date": "20130103"},......{"Date": "20170209"}] }
Error Response: Not applicable 404 if not found

Info:
Should always return data after reading the csv or database within our system.

Notes:
This function involves reading the daily.csv and getting all of the dates. Assumes that dates is filled in the csv. Assumes it is there. 
-----------------------------------------------------------------------
Get HIstorical specific

virtual path: /historical/YYYYMMDD

Request type: GET 

method:get_data(date_id)

Success status code: 200

Error status code: 404 "error: HTTP Error code 404"

Info: Reads all of the csv, and prints the specific date, returns 202 if it is not there 

Example Call:http://52.33.88.132:5000/historical/20140101

Returns:{"DATE":"20140101","TMAX": 34.0,"TMIN":26.0}
--------------------------------------------------------------
Get Forecast 

virtual path: /forecast/YYYYMMDD

Request type:GET

method:get_forecast(date_id)

Info: Returns the date if it exists , and then returns the next 7 days, it will randomly turn the date at that time plus or minus some number within negative 3 an positive 3 

Success status code: 200

Error stutus code: 400 'Error: http Error code 404'

Ex Call: http://52.33.88.132:5000/forecast/20130101

Returns:[{"DATE":"20130101","TMAX": 34.0,"TMIN":26.0}, {"DATE":"20130102","TMAX": 29.5,"TMIN":15.0}, {"DATE":"20130103","TMAX": 34.5,"TMIN":12.0}, {"DATE":"20130104","TMAX": 36.5,"TMIN":23.0}, {"DATE":"20130105","TMAX": 41.0,"TMIN":19.0}, {"DATE":"20130106","TMAX": 40.0,"TMIN":28.0}, {"DATE":"20130107","TMAX": 39.5,"TMIN":19.0} ]
-------------------------------------------------------------
historical post

Virtual path: /historical/YYYYMMDD 

Request type: POST

method post_date(data_info)

Info: Takes in the following input, then well add the date at the very end of csv 

Sample Input: {"DATE":"20130101","TMAX":34.0,"TMIN":26.0} 

Success status code: 200

Error status code: 400

Returns: Post: Response

Notes: assumes you are putting in correct data such as our sample input. ANd as raw text in the body, not as JSON. Also will put it into the excel file
---------------------------------------------------------------
historical delete 

Virtual path: /historical/YYYYMMdd 

Request type: DELETE

method: delete_date(data_id)

Info: Will find date and values, then write to new csv without that info. Then it will copy that new csv on top of the old csv 

Returns: deleted result : False

IN the function call it tells you whether it worked or not. Always returns status code 200
