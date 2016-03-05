#modeldb.py

import sqlite3
import time

#from datetime import date
#d = date.fromordinal(100)

#Start by connecting to the pos.db database
conn = sqlite3.connect('pos.db')
c = conn.cursor()
# MAKE SURE CONN AND C EXIST IN VIEW IF INTERACTING WITH SQLITE

# Create the sales table if it does not exist
def salesTable():
	c.execute('''CREATE TABLE IF NOT EXISTS sales (
		SaleIDcol INTEGER, 
		CustIDcol VARCHAR(9), 
		CCcol BOOLEAN, 
		SKUcol VARCHAR(9), 
		Salescol FLOAT(9), 
		Datecol DATE 
		PRIMARY KEY (SaleIDcol)
		FOREIGN KEY (CustIDcol)
		REFERENCES customers (CustIDcol)
		FOREIGN KEY (SKUcol)
		REFERENCES products (SKUcol)
		)''')
	conn.commit()

# Create the customers table if it does not exist
def customersTable():
	c.execute('''CREATE TABLE IF NOT EXISTS customers (
		CustIDcol VARCHAR(9), 
		Namecol VARCHAR(20), 
		PRIMARY KEY (CustIDcol)
		)''')
	conn.commit()

# Create the products table if it does not exist
def productsTable():
	c.execute('''CREATE TABLE IF NOT EXISTS products (
		SKUcol VARCHAR(9), 
		Productcol VARCHAR(20), 
		PRIMARY KEY (SKUcol)
		)''')
	conn.commit()



# Definition of the Customer class
# Only created when CustID not found in customers table
class Customer(object):
	totalCustomers = 0
	currentID = 100000000

	def __init__(self, Name, date):
		self.CustID = currentID
		Customer.currentID +=1
		self.Name = Name
		self.date = date

# check if custID exists in the customers table
	def checkCustID(self):
		"""checks if custID exists in the customers table"""
		c.execute('''SELECT CustIDcol FROM customers''')
		custIDtuple = c.fetchone()
		if self.CustID in  custIDtuple:
			True
		else:
			False

# check if sale is negative or not a number
	def checkSale(self):
		try:
			if self.Sale > 0 : 
				return True
			elif:
				return False
		except:
			return False

# Push customer object to the sqlite database
	def push(self):
		c.execute('''INSERT INTO customers VALUES (
			self.CustID,
			self.Name,
			self.date
			)''')
		conn.commit()


# Definition of the Product class
class Product(object):
	countProducts = 0

	def __init__(self, SKU):
		Product.countProducts +=1
		self.SKU = SKU

# get unique items from the database	
	def getItems(self):
		c.execute('''SELECT SKUcol, Productcol FROM products''')
		tupleSKU = c.fetchone()
		return tupleSKU

# Add products to the database
	def setItems(self, SKU, Product):
		c.execute('''INSERT INTO products VALUES (
			self.SKU,
			self.Product
			)''')
		conn.commit()



# Definition of the POS class
class POS(object):
	POScount = 0
# Each pos gets a unique SaleID equal to one more than the max SaleID in the database
# Each pos receives arguments CustID, Name, CC, SKU, sales, !!?day?!! that are returned from the GUI.
	def __init__(self, CustID, CC=0, SKU, sales, date):
#		self.SaleID =  totalSales + 1
		self.SaleID = c.execute('''SELECT MAX(SaleIDcol) FROM sales''') + 1
		POS.totalSales +=1

		self.CustID = CustID
#		if CustID NOT IN customers table, then print("must  create new customer")

		self.CC = CC
		self.SKU = SKU
		self.sales = sales
		self.date = date

# The insertDB method inserts the pos information into the sqlite database
	def submit(self):
		c.execute('''INSERT INTO sales VALUES (
			self.SaleID,
			self.CustID,
			self.CC,
			self.SKU,
			self.sales,
			self.date
			)''')
		conn.commit()



# Save and close the database.
def closeDay():
	"""Closes the books for the day."""
	conn.commit()
	conn.close()






