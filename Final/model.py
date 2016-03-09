#modeldb.py

import sqlite3
import time
import pandas as pd
import os

#Start by connecting to the pos.db database
conn = sqlite3.connect('pos.db')
c = conn.cursor()


def salesTable():
	'''Creates the sales table in the sqlite database
	if it does not already exist.'''
	c.execute('''CREATE TABLE IF NOT EXISTS sales (
		SaleIDcol INTEGER PRIMARY KEY AUTOINCREMENT ,
		CustIDcol INTEGER,
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

		CustIDcol INTEGER PRIMARY KEY AUTOINCREMENT ,
		Namecol VARCHAR(20),
		Datecol VARCHAR(20)
		)''')
	conn.commit()



def productsTable():
	'''Creates the products table in the sqlite database
	if it does not already exist.'''
	c.execute("CREATE TABLE IF NOT EXISTS products (SKUcol VARCHAR(20) PRIMARY KEY ,Productcol VARCHAR(20))")
	conn.commit()







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

	@staticmethod
	def setItems(SKU, Product):
		'''Adds a row in the Products table with the information
		from the product provided as an argument.'''
		c.execute("insert into products values (?, ?)", (SKU, Product))
		conn.commit()


class POS(object):
# Each pos gets a unique SaleID equal to one more than the max SaleID in the database
# Each pos receives arguments CustID, Name, CC, SKU, sales, !!?day?!! that are returned from the GUI.
	def __init__(self, CustID, CC, SKU, sales, date):
		'''Creates a new instance of a POS (sales transaction).'''
		self.CustID = CustID
		self.CC = CC
		self.SKU = SKU
		self.sales = sales
		self.date = date

# The insertDB method inserts the pos information into the sqlite database
	def submit1(self):
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
		'''Gets the sales data out of the POS database'''
		c.execute("SELECT * FROM sales")
		sales_data = c.fetchall()
		return (sales_data)

	@staticmethod
	def CRM():
		'''gets the sales of the day per customer'''
		c.execute("SELECT CustIDcol, Datecol, SUM(Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales) GROUP BY CustIDcol ")
		crm = c.fetchall()
		return crm
	@staticmethod
	def totSales():
		'''gets the sales of the day'''
		c.execute("SELECT SUM(Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales)")
		report = c.fetchall()
		return report
	@staticmethod
	def totCashSales():
		'''gets the Cash sales of the day'''
		c.execute("SELECT SUM (Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales) AND CCcol = 0")
		rep1 = c.fetchall()
		return rep1
	@staticmethod
	def totCCsales():
		'''gets the Credit Card sales of the day'''
		c.execute("SELECT SUM (Salescol) FROM sales WHERE Datecol = (SELECT MAX(Datecol) FROM sales) AND CCcol = 0")
		rep2 = c.fetchall()
		return rep2




def write_data_sql():
	"""Function that takes sales.csv and customers.csv files and pushes them into the pos.db via SQLITE"""
	c.execute("SELECT COUNT(*) FROM sales")
	count1 = c.fetchone()
	if count1[0] == 0:
		sales_table = pd.DataFrame.from_csv(os.getcwd()+"/sales.csv",sep=";",header=0)
		customer_table = pd.DataFrame.from_csv(os.getcwd()+"/customers.csv",sep=";",header=0)
		sku_table = pd.DataFrame.from_csv(os.getcwd()+"/sku.csv",sep=";",header=0)
		sales_table.to_sql('sales', conn, if_exists='append')
		customer_table.to_sql('customers', conn, if_exists='append')
		sku_table.to_sql('products', conn, if_exists='append')
	else:
		pass
