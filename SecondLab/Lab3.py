from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
'''
def fibonacciSequence():
	fileToRead = open("index.html","r")
	return fileToRead.read()
'''

