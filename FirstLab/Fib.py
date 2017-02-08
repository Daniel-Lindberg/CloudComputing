from flask import Flask
app = Flask(__name__)
@app.route('/')
def fibonacciSequence():
	fileToRead = open("index.html","r")
	return fileToRead.read()
