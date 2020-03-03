from typing import List, Dict
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/test')
def f0():
	return jsonify(res="Test")

@app.route('/test1')
def f1():
	return jsonify(res="Test1")

@app.route('/test2')
def f2():
	return jsonify(res="Test2")

@app.route('/test3')
def f3():
	return jsonify(res="Test3")

if __name__ == '__main__':
	app.run(host='0.0.0.0')
