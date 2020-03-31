from typing import List, Dict
from flask import Flask
import mysql.connector
import json

#Functie pentru inserarea unui nou zbor in baza de date

def add_flight(source, dest, departureDay, departureHour, duration, numberOfSeats, flightId, books, bT):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'flightsDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = "INSERT INTO flights (source, dest, departureDay, departureHour, duration, numberOfSeats, flightId, books,boughtTickets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (source, dest, departureDay, departureHour, duration, numberOfSeats, flightId, books, bT)
	cursor.execute(sql, val)


	connection.commit()

	cursor.close()
	connection.close()

#Functie pentru stergerea unui zbor din baza de date

def cancel_flight(flightId):

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'flightsDatabase'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = "DELETE FROM flights WHERE flightId = %s"
	val = (flightId, )
	cursor.execute(sql, val)


	connection.commit()

	cursor.close()
	connection.close()

#Functie pentru selectia unui zbor din baza de date

def selectFlight(idF):
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'flightsDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	sql = 'SELECT * FROM flights WHERE flightId = %s'
	var = (idF,)	

	cursor.execute(sql, var)

	result = []
	for line in cursor:
		result.append(line)

	cursor.close()
	connection.close()

	return result

def bookFlight(fId):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'flightsDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'UPDATE flights SET books = books + 1 WHERE flightId = %s'
	args = (fId,)
	cursor.execute(sql, args)

	connection.commit()
	cursor.close()
	connection.close()

def getAllFlightsAfter(source, departureDay, departureHour):

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'flightsDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	sql = 'SELECT * FROM flights WHERE source = %s AND departureDay > %s OR (departureDay = %s AND departureHour >= %s)'
	var = (source, departureDay, departureDay, departureHour)	

	cursor.execute(sql, var)

	result = []
	for line in cursor:
		result.append(line)

	cursor.close()
	connection.close()

	return result


def buyFlight(fId):
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'flightsDatabase'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	sql = 'UPDATE flights SET boughtTickets = boughtTickets + 1 WHERE flightId = %s'
	args = (fId,)
	cursor.execute(sql, args)

	connection.commit()
	cursor.close()
	connection.close()

def main():

	while(True):

		command = input("Enter command: add cancel select\n")

		if command == "add":
			args = input("\nInsert arguments: source, dest, departureDay, departureHour, duration, numberOfSeats, flightId\n")

			argsL = args.split()			
			add_flight(argsL[0], argsL[1], argsL[2], argsL[3], argsL[4], argsL[5], argsL[6], str(0), str(0))

		if command == 'cancel':
			args = input("\nInsert id\n")
			cancel_flight(args)

		if command == 'select':
			args = input("\nInsert id\n")
			res = selectFlight(args)
			print(res)

		if command == 'book':
			args = input("\nInsert id\n")
			bookFlight(args)

		if command == 'flights':

			args = input("Insert start location and departureDay and hour\n")
			argsL = args.split()

			res = getAllFlightsAfter(argsL[0], argsL[1], argsL[2])
			for r in res:
				print(r)

		if command == 'buy':
			args = input("Insert id\n")
			buyFlight(args)

if __name__ == '__main__':

	main()
