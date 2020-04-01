from typing import List, Dict
from flask import Flask
import mysql.connector
import json

def add_smartphone(smartphone_name, smartphone_id):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'smartphonesDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = "INSERT INTO smartphones (smartphone_name, smartphone_id) VALUES (%s, %s)"
	val = (smartphone_name, smartphone_id)
	cursor.execute(sql, val)

	connection.commit()
	cursor.close()
	connection.close()

def main():

	while(True):

		command = input("Enter command: add or remove\n")

		if command == "add":
			args = input("\nInsert arguments: smartphone Id, smartphone Name\n")
			argsL = args.split()
			add_smartphone(argsL[0], argsL[1])
		if command == "remove":
			args = input("\nRemove arguments: smartphone Id\n")
			argsL = args.split()
s
if __name__ == '__main__':

	main()
