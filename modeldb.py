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
		SaleIDcol INTEGER PRIMARY KEY ,
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
		CustIDcol VARCHAR(9),
		Namecol VARCHAR(20),
		Datecol VARCHAR(20),
		PRIMARY KEY (CustIDcol)
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
	totalCustomers = 0
	currentID = 100000000

	def __init__(self, Name, date):
		'''Create a new instance of a Customer.'''
		self.CustID = Customer.currentID
		Customer.currentID +=1
		self.Name = Name
		self.date = date

	def push(self):
		'''Adds a row in the customers table with the information
		from the customer provided as an argument.'''
		c.execute('''INSERT INTO customers VALUES (?,?,?)''', (Customer.currentID, self.Name, self.date))
		conn.commit()
	@staticmethod
	def checkCust():
		c.execute('''SELECT CustIDcol FROM customers''')
		custIDtuple = c.fetchall()
#		elon = pd.DataFrame(custIDtuple, columns=['custids'])
#		return elon
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
	maxSaleID = 1000
# Each pos gets a unique SaleID equal to one more than the max SaleID in the database
# Each pos receives arguments CustID, Name, CC, SKU, sales, !!?day?!! that are returned from the GUI.
	def __init__(self, CustID, CC, SKU, sales, date):
		'''Creates a new instance of a POS (sales transaction).'''
		POS.maxSaleID += 1
		self.CustID = CustID
#		if CustID NOT IN customers table, then print("must  create new customer")
		self.CC = CC
		self.SKU = SKU
		self.sales = sales
		self.date = date
		print("this is my creation...", self.CustID, self.CC, self.SKU, self.sales)

# The insertDB method inserts the pos information into the sqlite database
	def submit1(self):
		'''Adds a row in the sales table with the information
		from the POS provided as an argument.'''
		print("Am I reaching?")
		c.execute("INSERT INTO sales VALUES (?,?,?,?,?,?)", (
			POS.maxSaleID,
			self.CustID,
			self.CC,
			self.SKU,
			self.sales,
			self.date
			))
		print("going, going, gone? Submit!")
		conn.commit()

	@staticmethod
	def getPosData():
		c.execute("SELECT * FROM sales")
		sales_data = c.fetchall()
		return (sales_data)


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
