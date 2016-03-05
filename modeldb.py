#modeldb.py

import sqlite3
import time

#from datetime import date
#d = date.fromordinal(100)

#Start by connecting to the pos.db database
conn = sqlite3.connect('pos.db')
c = conn.cursor()



# Create the table if it does not exists
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
	)''')



c.execute('''CREATE TABLE IF NOT EXISTS customers (
	CustIDcol VARCHAR(9), 
	Namecol VARCHAR(20), 
	PRIMARY KEY (CustIDcol)
	)''')


# Definition of the customer class
# Only created when CustID not found in customers table
class Customer(object):
	totalCustomers = 0
	currentID = 100000000
	date = d

	def _init_(self, Name):
		self.CustID = currentID
		Customer.currentID +=1
		self.Name = Name
		self.date = Customer.date

	def custDBpush(self):
		c.execute('''INSERT INTO customers VALUES (
			self.CustID,
			self.Name,
			self.date
			)''')

#Customer.custDBpush(New_Cust_Name)


# Definition of the POS class
class POS(object):
	POScount = 0
	date = d

# Each pos gets a unique SaleID equal to one more than the max SaleID in the database
# Each pos receives arguments CustID, Name, CC, SKU, sales, !!?day?!! that are returned from the GUI.
	def _init_(self, CustID, CC=0, SKU, sales):
#		self.SaleID =  totalSales + 1
		self.SaleID = c.execute('''SELECT MAX(SaleIDcol) FROM sales''') + 1
		POS.totalSales +=1

		self.CustID = CustID
#		if CustID NOT IN customers table, then print("must  create new customer")

		self.Name = Name
		self.CC = CC
		self.SKU = SKU
		self.sales = sales
		self.date = POS.date

# The insertDB method inserts the pos information into the sqlite database
	def submitPOS(self):
		c.execute('''INSERT INTO sales VALUES (
			self.SaleID,
			self.CustID,
			self.CC,
			self.SKU,
			self.sales,
			self.date
			)''')

	def closeDay():
		"""Closes the books for the day."""
		pos.date +=1

		print("The day has been closed and books reset for tomorrow. Have a nice night! Don't drink and drive.")



#transaction.addSaleDB()







# SAVE CHANGES TO DB
#conn.commit()

# CLOSE THE DB
#conn.close()






