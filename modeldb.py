#modeldb.py

import sqlite3
import time
import pandas as pd
import os

#Start by connecting to the pos.db database
conn = sqlite3.connect('pos.db')
c = conn.cursor()

# MAKE SURE CONN AND C EXIST IN VIEW IF INTERACTING WITH SQLITE

def salesTable():
	'''Creates the sales table in the sqlite database
	if it does not already exist.'''
	c.execute('''CREATE TABLE IF NOT EXISTS sales (
		SaleIDcol INTEGER PRIMARY KEY AUTOINCREMENT ,
		CustIDcol VARCHAR(20),
		CCcol BOOLEAN,
		SKUcol VARCHAR(20),
		Salescol FLOAT(20),
		Datecol DATE ,
		FOREIGN KEY (CustIDcol)
		REFERENCES customers (CustIDcol),
		FOREIGN KEY (SKUcol)
		REFERENCES products (SKUcol)
		)''')
	conn.commit()

def customersTable():
	'''Creates the customers table in the sqlite database
	if it does not already exist.'''
	c.execute('''CREATE TABLE IF NOT EXISTS customers (
<<<<<<< HEAD
		CustIDcol VARCHAR(9),
	2	Namecol VARCHAR(20),
		Datecol VARCHAR(20),
		PRIMARY KEY (CustIDcol)
=======
		CustIDcol INTEGER PRIMARY KEY AUTOINCREMENT ,
		Namecol VARCHAR(20),
		Datecol VARCHAR(20)
>>>>>>> origin/master
		)''')
	conn.commit()



def productsTable():
	'''Creates the products table in the sqlite database
	if it does not already exist.'''
	c.execute("CREATE TABLE IF NOT EXISTS products (SKUcol VARCHAR(20) PRIMARY KEY ,Productcol VARCHAR(20))")
	conn.commit()



# Definition of the Customer class
# Only created when CustID not found in customers table
class Customer(object):


	def __init__(self, Name, date):
		'''Create a new instance of a Customer.'''
		self.Name = Name
		self.date = date

	def push(self):
		'''Adds a row in the customers table with the information
		from the customer provided as an argument.'''
		c.execute('''INSERT INTO customers VALUES (?,?,?)''', (None, self.Name, self.date))
		conn.commit()
	@staticmethod
	def checkCust():
		c.execute('''SELECT CustIDcol FROM customers''')
		custIDtuple = c.fetchall()
		print(custIDtuple)
		return custIDtuple



class Product(object):
	countProducts = 0

	def __init__(self, SKU):
		'''Creates a new instance of a Product.'''
		Product.countProducts +=1
		self.SKU = SKU
	@staticmethod
	def getItems():
		'''Returns the list of products available, as stored in the products table.'''
		c.execute('''SELECT SKUcol, Productcol FROM products''')
		tupleSKU = c.fetchall()
		return tupleSKU



# Add products to the database

	@staticmethod
	def setItems(SKU, Product):
		'''Adds a row in the Products table with the information
		from the product provided as an argument.'''
		c.execute("insert into products values (?, ?)", (SKU, Product))
		conn.commit()



# Definition of the POS class
class POS(object):
# Each pos gets a unique SaleID equal to one more than the max SaleID in the database
# Each pos receives arguments CustID, Name, CC, SKU, sales, !!?day?!! that are returned from the GUI.
	def __init__(self, CustID, CC, SKU, sales, date):
		'''Creates a new instance of a POS (sales transaction).'''
		self.CustID = CustID
#		if CustID NOT IN customers table, then print("must  create new customer")
		self.CC = CC
		self.SKU = SKU
		self.sales = sales
		self.date = date

# The insertDB method inserts the pos information into the sqlite database
	def submit(self):
		'''Adds a row in the sales table with the information
		from the POS provided as an argument.'''
		c.execute("INSERT INTO sales VALUES (?,?,?,?,?,?)", (
			None,
			self.CustID,
			self.CC,
			self.SKU,
			self.sales,
			self.date
			))
		conn.commit()

	@staticmethod
	def getPosData():
		c.execute("SELECT * FROM sales")
		sales_data = c.fetchall()
		return(sales_data)


	@staticmethod
	def CRM():
		c.execute("SELECT CustIDcol, Datecol, SUM(Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales) GROUP BY CustIDcol ")
		crm = c.fetchall()
		return crm
	@staticmethod
	def totSales():
		c.execute("SELECT SUM(Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales)")
		report = c.fetchall()
		return report
	@staticmethod
	def totCashSales():
		c.execute("SELECT SUM (Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales) AND CCcol = 0")
		rep1 = c.fetchall()
		return rep1
	@staticmethod
	def totCCsales():
		c.execute("SELECT SUM (Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales) AND CCcol = 0")
		rep2 = c.fetchall()
		return rep2



# Save and close the database.
def closeDay():
	"""Closes the books for the day."""
	conn.commit()
	conn.close()



def write_data_sql():
	"""Function that takes sales.csv and customers.csv files and pushes them into the pos.db via SQLITE"""
	sales_table = pd.DataFrame.from_csv(os.getcwd()+"/sales.csv",sep=";",header=0)
	customer_table = pd.DataFrame.from_csv(os.getcwd()+"/customers.csv",sep=";",header=0)
	sales_table.to_sql('sales', conn, if_exists='append')
	customer_table.to_sql('customers', conn, if_exists='append')


a= POS(2, 1,"ZRRTGf",123,"22/05/1992")
POS.submit(a)
