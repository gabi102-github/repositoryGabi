from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import sys
from tabulate import tabulate

def add_smartphone(smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = "INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock) VALUES (%s, %s, %s, %s, %s)"
	val = (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
	cursor.execute(sql, val)

	connection.commit()
	cursor.close()
	connection.close()

def list_smartphones():

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM smartphones")
    result = cursor.fetchall()
    print (result)
    #print(tabulate(result, headers=["smartphone_name", "smartphone_id", "smartphone_brand", "smartphone_price", "smartphone_stock"], tablefmt='psql'))

    cursor.close()
    connection.close()

def list_users():

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(tabulate(result, headers=["username", "pwd", "userid"], tablefmt='psql'))

    cursor.close()
    connection.close()

def list_orders():

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    print(tabulate(result, headers=["productId", "userId", "orderId"], tablefmt='psql'))

    cursor.close()
    connection.close()

def update_smartphone_stock(Id, Stock):

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    sql = ("UPDATE smartphones SET smartphone_stock = %s WHERE smartphone_id = %s")
    sql_data = (Stock, Id)
    cursor.execute(sql, sql_data)

    connection.commit()
    cursor.close()
    connection.close()

def remove_smartphone(ID):

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    sql = ("DELETE FROM smartphones WHERE smartphone_id = %s")
    smartphone_Id = (ID, )
    cursor.execute(sql, smartphone_Id)

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

def delUser(userid):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'smartphonesDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'DELETE FROM users WHERE userId = %s'
	args = (userid,)
	cursor.execute(sql, args)

	connection.commit()
	cursor.close()
	connection.close()

def main():

	while(True):

		command = input("Enter command:\n1. Add smartphone\n2. Remove smartphone\n3. Show products\n4. Update stock\n5. Show users\n6. Show orders\n7. Delete user\n8. Insert user\n\n")

		if command == "add" or command == "1":
			args = input("\nInsert arguments: smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock\n")
			argsL = args.split()
			print(argsL)
			add_smartphone(argsL[0], argsL[1], argsL[2], argsL[3], argsL[4])

		if command == "remove" or command == "2":
			args = input("\nRemove arguments: smartphone_id\n")
			argsL = args.split()
			remove_smartphone(argsL[0])	

		if command == "show" or command == "3":
			print("List of smartphones:\n")
			list_smartphones()

		if command == "update stock" or command == "4":
			args = input("\nInsert arguments: smartphone_id, smartphone_new_stock\n")
			argsL = args.split()
			update_smartphone_stock(argsL[0], argsL[1])

		if command == "users" or command == "5":
			list_users()

		if command == "orders" or command == "6":
			list_orders()

		if command == "delete user" or command == "7":
			args = input("\nInsert arguments: user id\n")
			argsL = args.split()
			delUser(argsL[0])

		if command == "insert user" or command == "8":
			args = input("\nInsert arguments: username, new password\n")
			argsL = args.split()
			addUser(argsL[0], argsL[1])

if __name__ == '__main__':

	main()
