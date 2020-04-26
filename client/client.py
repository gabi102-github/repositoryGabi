import requests
import sys
import json
from tabulate import tabulate
import urllib.request

logged_in = False
username = ""
logging_in = False
my_cart = []

def main():

	global logged_in
	global username
	global my_cart

	while(True):


		if logged_in == False:

			print("Currently not logged in\n")

			command = input("Enter command:\n1. Log in\n2. Sing in\n3. Show Products\n\n")

			if command == "log in" or command == "1":
				
				args = input("\nInsert arguments:\nUsername: ")
				args1 = args.split()
				username = args1[0]
				#print("arg1 " + args1[0])


				args = input("\nPassword: ")
				args2 = args.split()
				print("\n")
				#print("arg2 " + args2[0])

				url = "http://server:5000/loginCheck?us=" + args1[0] + "&pwd=" + args2[0]

				oUrl = urllib.request.urlopen(url)
				data = json.loads(oUrl.read().decode())

				if data['res'] is None:
					print("No data found\n")
				else:
					#print(data['res'])
					if data['res'] == 1:
						logged_in = True

					elif data['res'] == 0:
						logged_in = False
						username = ""

			if command == "sing in" or command == "2":
				args = input("\nInsert arguments:\nNew username: ")
				args1 = args.split()
				args = input("\nNew password: ")
				args2 = args.split()
				print("\n")


				url = "http://server:5000/singinCheck?us=" + args1[0] + "&pwd=" + args2[0]

				oUrl = urllib.request.urlopen(url)
				data = json.loads(oUrl.read().decode())

				#print(data['res'])

				if data['res'] == "Succes":
					print("Sing in succesful, please log in\n")
				if data['res'] == "Error":
					print("Error: Sing in failed\n")

			if command == "show" or command == "3":
				url = "http://server:5000/displaySmartphones"
				oUrl = urllib.request.urlopen(url)
				data = json.loads(oUrl.read().decode())
				result = data['res']
				print(tabulate(result, headers=["smartphone_name", "smartphone_id", "smartphone_brand", "smartphone_price"], tablefmt='psql'))
				print("\n")

		else:
			print("Logged in as " + username + "\n")
			command = input("Enter command:\n1. Log out\n2. Show Products\n3. Cart\n4. Add to cart\n5. remove\n6. Buy\n\n")

			if command == "log out" or command == "1":
				logged_in = False
				username = ""
				print("\n")

			if command == "show" or command == "2":
				url = "http://server:5000/displaySmartphones"
				oUrl = urllib.request.urlopen(url)
				data = json.loads(oUrl.read().decode())
				result = data['res']
				print(tabulate(result, headers=["smartphone_name", "smartphone_id", "smartphone_brand", "smartphone_price"], tablefmt='psql'))
				print("\n")
			if command == "cart" or command == "3":

				#for elem in my_cart:
				#	if elem != []:
				print(tabulate(my_cart, headers=["smartphone_name", "smartphone_id", "smartphone_brand", "smartphone_price"], tablefmt='psql'))
				print("\n")

			if command == "add" or command == "4":
				smartId = input("Enter phone id: ")
				url = "http://server:5000/findSmartphone?sid=" + smartId
				oUrl = urllib.request.urlopen(url)
				data = json.loads(oUrl.read().decode())
				result = data['res']
				#print(result)
				#print(tabulate(result, headers=["smartphone_name", "smartphone_id", "smartphone_brand", "smartphone_price"], tablefmt='psql'))

				if result == []:
					print("No phone found with that id\n")
					continue
				else:
					my_cart.append(tuple(result[0]))

			if command == "remove" or command == "5":
				smartId = input("Enter phone id: ")
				new_my_cart = []
				first = True

				#print(smartId)

				for elem in my_cart:
					print(elem[1])
					if str(elem[1]) == smartId and first == True:
						first = False
					else:
						new_my_cart.append(tuple(elem))

				my_cart = new_my_cart

			if command == "buy" or command == "6":

				if my_cart == []:
					print("Cart is empty, please add products\n")
				else:

					creditCard = input("Enter credit card details: ")

					url = "http://server:5000/makeBuy?us="+ username +"&cd=" + creditCard[0]

					url += "&nr=" + str(len(my_cart))

					i = 0
					for elem in my_cart:
						url += '&i'+ str(i) + '=' + str(elem[1])
						i += 1

					oUrl = urllib.request.urlopen(url)
					data = json.loads(oUrl.read().decode())
					result = data['res']
					#print(result)

					my_cart = []

if __name__ == '__main__':

	main()
