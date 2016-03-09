# Controllerv2.py

import modeldb as Modelv2
import sqlite3
import pandas as pd

conn = sqlite3.connect('pos.db')
c = conn.cursor()

def formatError():
	return "Sorry, transaction failed."

def broke():
	return "Did you buy anything? Please enter a sale > 0"

def bigspender():
	return "Are you sure? Toilet paper doesn't cost $500... Try again."

def notcust():
	return "Transaction Failed. Please create a new customer ID."

def existingcust():
	return "Welcome back, good sire."

def saleconf():
	return "Thank you for your sale! Have dandy dia!"

def newcustconf():
	c.execute("SELECT max(CustIDcol) FROM customers")
	newest = c.fetchone()
	return "Great to have a new customer! Your ID # is %s" % (newest)

def noproduct():
	return "Please pick the product purchased."

def main():

	conn = sqlite3.connect('pos.db')
	c = conn.cursor()

#	c.execute("drop table customers")
#	c.execute("drop table sales")
#	c.execute("drop table products")

# Start by connecting to SQLite database and creating the tables for Sales, Customers and Products
	Modelv2.salesTable()
	Modelv2.customersTable()
	Modelv2.productsTable()

#	Modelv2.Product.setItems("abc123456", "Vacuum cleaner")
#	Modelv2.Product.setItems("abc123457", "Radio")
#	Modelv2.Product.setItems("abc123458", "Television")
#	Modelv2.Product.setItems("abc123459", "Laptop")
#	Modelv2.Product.setItems("abc123450", "Desktop")

	Modelv2.write_data_sql()

def nameplease():
	return "Please enter a Customer ID."

def saleplease():
	return "Please enter a sale amount."

def newsalebutton(list1):
	try:
		thresh = 0
		errors = []
		if list1[0] == '':
			errors.append(nameplease())
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
	try:
		name = clist[0]
		dateCV = clist[1]
		cnew = Modelv2.Customer(name, dateCV)
		cnew.push()
		return newcustconf()
	except:
		pass


def allerrors():
	print("allerrors: ", alphabet)
	return alphabet

main()

