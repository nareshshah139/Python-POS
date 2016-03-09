# Controllerv2.py

import modeldb as Modelv2
import sqlite3
import pandas as pd

# Start by connecting and opening the sqlite database.
conn = sqlite3.connect('pos.db')
c = conn.cursor()

# All of the below functions simply provide the text used for the GUI messages.
# They are called when certain things happen, as described in the docstrings.

def formatError():
	"""Provides a message if the transaction is not pushed to the database."""
	return "Sorry, transaction failed."

def broke():
	"""Provides a message if the sales amount entered is zero or less."""
	return "Did you buy anything? Please enter a sale > 0"

def bigspender():
	"""Provides a message if the sales amount entered is greater than 500..."""
	return "Are you sure? Toilet paper doesn't cost $500... Try again."

def notcust():
	"""Provides a message if the customer ID entered does not exist in the database."""
	return "Transaction Failed. Please create a new customer ID."

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
	return "Please pick the product purchased."

def idplease():
	"""Provides a message if the Customer ID is left blank."""
	return "Please enter a Customer ID."

def saleplease():
	"""Provides a message if the sales amount is left blank."""
	return "Please enter a sale amount."

def nameplease():
	"""Provides a message if the Name is left blank."""
	return "Come on, that's not your name. Please enter SOMETHING."


def main():

	conn = sqlite3.connect('pos.db')
	c = conn.cursor()

	c.execute("drop table customers")
	c.execute("drop table sales")
	c.execute("drop table products")

# Start by connecting to SQLite database and creating the tables for Sales, Customers and Products
	Modelv2.salesTable()
	Modelv2.customersTable()
	Modelv2.productsTable()

	Modelv2.Product.setItems("abc123456", "Vacuum cleaner")
	Modelv2.Product.setItems("abc123457", "Radio")
	Modelv2.Product.setItems("abc123458", "Television")
	Modelv2.Product.setItems("abc123459", "Laptop")
	Modelv2.Product.setItems("abc123450", "Desktop")

	Modelv2.write_data_sql()

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
			custIDT = Modelv2.Customer.checkCust()
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
					hold = Modelv2.POS(CustID, CC, SKU, sales, datePOS)
					Modelv2.POS.submit1(hold)
					errors.append(saleconf())

				else:
					errors.append(formatError())
		return errors
	except(RuntimeError, TypeError, NameError):
		print(RuntimeError, TypeError, NameError)

def SKUcode(list1):
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
		if list1[0] == '':
			myerrors.append(nameplease())
		else:
			name = clist[0]
			dateCV = clist[1]
			cnew = Modelv2.Customer(name, dateCV)
			cnew.push()
			myerrors.append(newcustconf())
		return myerrors
	except:
		pass


main()

