# Controllerv2.py

import model
import sqlite3
import pandas as pd

# Start by connecting and opening the sqlite database.
conn = sqlite3.connect('pos.db')
c = conn.cursor()

# All of the below functions simply provide the text used for the GUI messages.
# They are called when certain things happen, as described in the docstrings.

def formatError():
	"""Provides a message if the transaction is not pushed to the database."""
	return "Sorry dude, your transaction failed."

def broke():
	"""Provides a message if the sales amount entered is zero or less."""
	return "Did you buy anything? Please enter a sale > 0"

def bigspender():
	"""Provides a message if the sales amount entered is greater than 500..."""
	return "Are you sure? Toilet paper doesn't cost that much... Try again."

def notcust():
	"""Provides a message if the customer ID entered does not exist in the database."""
	return "Sorry, transaction failed. Start by creating a new customer ID (see tab above)."

def existingcust():
	"""Provides a message if the customer ID is recognized in the database."""
	return "Welcome back, good sire."

def saleconf():
	"""Provides a message if the transaction is successfully pushed to the database."""
	return "Thank you for your sale! Have dandy dia!"

def newcustconf():
	"""Provides a message with the new customer's ID after being successfully added to the database."""
	c.execute("SELECT max(CustIDcol) FROM customers")
	newest = c.fetchone()
	return "Great to have a new customer! Your ID # is %s" % (newest)

def noproduct():
	"""Provides a message if an item is not selected from the SKU dropdown."""
	return "You paid that much for nothing? Pick a product please."

def idplease():
	"""Provides a message if the Customer ID is left blank."""
	return "Please enter your Customer ID. Don't remember (dummy)? Create a new one in the customer tab."

def saleplease():
	"""Provides a message if the sales amount is left blank."""
	return "And... how much money would you like to give us? (just the number, please)."

def nameplease():
	"""Provides a message if the Name is left blank."""
	return "Come on, that's not your name. Enter SOMETHING."


def main():

	conn = sqlite3.connect('pos.db')
	c = conn.cursor()

#	c.execute("drop table customers")
#	c.execute("drop table sales")
#	c.execute("drop table products")

# Start by connecting to SQLite database and creating the tables for Sales, Customers and Products
	model.salesTable()
	model.customersTable()
	model.productsTable()

#	model.Product.setItems("abc123456", "Vacuum cleaner")
#	model.Product.setItems("abc123457", "Radio")
#	model.Product.setItems("abc123458", "Television")
#	model.Product.setItems("abc123459", "Laptop")
#	model.Product.setItems("abc123450", "Desktop")

	model.write_data_sql()

def newsalebutton(list1):
	"""Receives the data input by the user in the GUI's POS view when the submit button is clicked.
	Checks if the customer ID already exists or not;
	checks the Customer ID, SKU and sales are not left blank;
	checks the sales amount is a positive number 500 or less.
	If all 3 criteria are passed, a POS object is created and its attributes are pushed to the databse.
	For each scenario, functions are called to display relevant messages."""
	try:
		thresh = 0
		errors = []
		if list1[0] == '':
			errors.append(idplease())
		elif list1[3] == '':
			errors.append(saleplease())
		else:
			CustID = int(list1[0])
			custIDT = model.Customer.checkCust()
			zzz = [item for item in custIDT if CustID in item]
			if zzz == []:
				errors.append(notcust())
			else:
				errors.append(existingcust())
				thresh += 1
				CC = int(list1[1])
				SKU = SKUcode(list1)
				if SKU is None:
					errors.append(noproduct())
				else:
					thresh += 1
				sales = float(list1[3])
				if sales > 500:
					errors.append(bigspender())
				elif sales > 0:
					thresh += 1
				else:
					errors.append(broke())
					thresh = 0
				datePOS = list1[4]
				if thresh == 3:
					hold = model.POS(CustID, CC, SKU, sales, datePOS)
					model.POS.submit1(hold)
					errors.append(saleconf())

				else:
					errors.append(formatError())
		return errors
	except(RuntimeError, TypeError, NameError):
		print(RuntimeError, TypeError, NameError)

def SKUcode(list1):
	'''Matches SKU code with product name. Our grocery store specializes in electronics.'''
	try:
		skucode1 = list1[2]
		if skucode1 == "Vacuum Cleaner":
			return 'abc123456'
		elif skucode1 == "Radio":
			return 'abc123457'
		elif skucode1 == "Television":
			return 'abc123458'
		elif skucode1 == "Laptop":
			return 'abc123459'
		elif skucode1 == "Desktop":
			return "abc123460"
	except:
		pass

def newcustbutton(clist):
	"""Receives the data input by the user in the GUI's New Customer tab when the add new user
	button is clicked. Creates a new Customer object and pushes to the database.
	Calls a message to """
	try:
		myerrors = []
		if clist[0] == '':
			myerrors.append(nameplease())
		else:
			name = clist[0]
			dateCV = clist[1]
			cnew = model.Customer(name, dateCV)
			cnew.push()
			myerrors.append(newcustconf())
		return myerrors
	except:
		pass


main()
