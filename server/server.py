from typing import List, Dict
from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

current_order_id = 0

def checkUsernamePassword(username, pwd):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'smartphonesDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'SELECT pwd FROM users WHERE username = %s'
	args = (username,)
	cursor.execute(sql, args)

	result = []
	for line in cursor:
		print(line)
		result.append(line)

	cursor.close()
	connection.close()

	if result[0][0] == pwd:
		return 1
	else:
		return 0

def checkUsernameExist(username):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'smartphonesDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'SELECT pwd FROM users WHERE username = %s'
	args = (username,)
	cursor.execute(sql, args)

	result = []
	for line in cursor:
		print(line)
		result.append(line)

	cursor.close()
	connection.close()

	if result != []:
		return 1
	else:
		return 0

def displaySmartphones():

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute("SELECT smartphone_name, smartphone_id, smartphone_brand, smartphone_price  FROM smartphones")
	result = cursor.fetchall()

	cursor.close()
	connection.close()

	return result

def findUserID(username):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = "SELECT userId FROM users WHERE username = %s"
	args = (username, )
	cursor.execute(sql, args)

	result = cursor.fetchall()

	cursor.close()
	connection.close()

	return result

def findSmartphone(sId):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'SELECT smartphone_name, smartphone_id, smartphone_brand, smartphone_price  FROM smartphones WHERE smartphone_id = %s'
	args = (sId,)
	cursor.execute(sql, args)

	result = cursor.fetchall()

	cursor.close()
	connection.close()

	return result

def findStock(sId):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'SELECT smartphone_stock FROM smartphones WHERE smartphone_id = %s'
	args = (sId,)
	cursor.execute(sql, args)

	result = cursor.fetchall()

	cursor.close()
	connection.close()

	return result

def decreaseStock(sId):
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'smartphonesDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'UPDATE smartphones SET smartphone_stock = smartphone_stock - 1 WHERE smartphone_id = %s'
	args = (sId,)
	cursor.execute(sql, args)

	connection.commit()
	cursor.close()
	connection.close()

def addOrder(sId, uId, orderId):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'smartphonesDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'INSERT INTO orders (productId, userId, orderId) VALUES (%s, %s, %s)'
	args = (sId, uId, orderId)
	cursor.execute(sql, args)

	connection.commit()
	cursor.close()
	connection.close()

def addUser(username, password):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'smartphonesDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'INSERT INTO users (username, pwd) VALUES (%s, %s)'
	args = (username, password)
	cursor.execute(sql, args)

	connection.commit()
	cursor.close()
	connection.close()

@app.route('/loginCheck')
def f0():

	username = request.args.get('us', default = None, type = str)
	pwd = request.args.get('pwd', default = None, type = str)

	result = checkUsernamePassword(username, pwd)

	return jsonify(res=result)

@app.route('/displaySmartphones')
def f1():

	result = displaySmartphones()

	return jsonify(res=result)

@app.route('/findSmartphone')
def f2():

	sId = request.args.get('sid', default = None, type = str)
	result = findSmartphone(sId)

	return jsonify(res=result)

@app.route('/makeBuy')
def f3():

	global current_order_id
	username = request.args.get('us', default = None, type = str)
	creditCard = request.args.get('cd', default = None, type = str)
	nr = request.args.get('nr', default = None, type = int)

	idVect = []

	for i in range(nr):
		idVect.append(request.args.get("i"+str(i), default = None, type = str))

	if nr == 0:
		return jsonify(res="Error")
	else:

		for sid in idVect:
			stock = findStock(sid)
			print(stock)
			if stock[0][0] <= 0:
				return jsonify(res="Error")

		uid = findUserID(username)[0][0]

		for sid in idVect:
			addOrder(sid, uid, current_order_id)
			decreaseStock(sid)

		current_order_id += 1

		return jsonify(res="Succes")

@app.route('/singinCheck')
def f4():
	username = request.args.get('us', default = None, type = str)
	pwd = request.args.get('pwd', default = None, type = str)

	#return jsonify(res=checkUsernameExist(username))

	if checkUsernameExist(username) == 1:
		return jsonify(res="Error")
	else:
		addUser(username, pwd)
		return jsonify(res="Succes")


if __name__ == '__main__':
	app.run(host='0.0.0.0')
