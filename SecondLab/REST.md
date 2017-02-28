Lab 2
daniel Lindberg
date: 2-28-2017



Different calls to my server on 52.33.88.132:5000

Get Historical 
virtual path: /historical
Info:Reads all of the csv, and prints the dates
Returns: [{"DATE": "20130101"}, 
{"DATE": "20130102"}, 
{"DATE": "20130103"},
{"DATE": "20130112"}, 
{"DATE": "20130113"}, 
{"DATE": “20130114"},
....
 {"DATE": “20170115"}]

Get HIstorical specific
virtual path: /historical/YYYYMMDD
Info: Reads all of the csv, and prints the specific date, returns 202 if it is not there
Returns:{"DATE":"20130101","TMAX":
34.0,"TMIN":26.0}

Get Forecast
virtual path: /forecast/YYYYMMDD
Info: Returns the date if it exists , and then returns the next 7 days, it will randomly turn the date at that time plus or minus some number within negative 3 an positive 3 
Returns:[{"DATE":"20130101","TMAX":
34.0,"TMIN":26.0},
{"DATE":"20130102","TMAX":
29.5,"TMIN":15.0},
{"DATE":"20130103","TMAX":
34.5,"TMIN":12.0},
{"DATE":"20130104","TMAX":
36.5,"TMIN":23.0},
{"DATE":"20130105","TMAX":
41.0,"TMIN":19.0},
{"DATE":"20130106","TMAX":
40.0,"TMIN":28.0},
{"DATE":"20130107","TMAX":
39.5,"TMIN":19.0} ]


historical post
Virtual path: /historical/YYYYMMDD
Info: Takes in the following input, then well add the date at the very end of csv
Sample Input: {"DATE":"20130101","TMAX":34.0,"TMIN":26.0}
Returns: Post: Response

historical delete
Virtual path: /historical/YYYYMMdd
Info: Will find date and values, then write to new csv without that info. Then it will copy that new csv on top of the old csv
Returns: deleted result : False


