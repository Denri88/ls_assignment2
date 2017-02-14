from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/birthday')
def birthday():
	return 'December 02 1988'

@app.route('/greeting/<name>')
def greeting(name):
	return 'Hello ' + name