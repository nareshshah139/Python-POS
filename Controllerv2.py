#Controllerv2.py

import Modelv2
import Viewv2

def formatError():
	return "Sorry, wrong format."

def noSale():
	return "Did you even buy anything? Enter a sale > 0.00"

def bigspender():
	return "Are you sure? Toilet paper doesn't cost $400..."

def notnewcust():
	return "Sorry, we don't recognize your ID. Please create a new customer."

def checkCC():
	try:
		if int(griv[0]) == 1:
			pass
		elif int(griv[1]) ==0:
			pass
		else:
			formatError()
	except:
		formatError()


def checkC_ID():
	try:
		ccid = int(griv[1])
		
		c.execute('''SELECT CustIDcol FROM customers''')
		custIDtuple = c.fetchone()
		if ccid in  custIDtuple:
			pass
		else:
			notnewcust()
	except:
		formatError()

	
def checkSales():
	try:
		if int(griv[3]) > 0 : 
			pass
		elif int(griv[3]) > 400:
			return bigspender()
		else:
			return noSale()
	except:
		formatError()


def main():

	Modelv2.Product.setItems("abc123456","Vacuum cleaner")
	Modelv2.Product.setItems("abc123457","Radio")
	Modelv2.Product.setItems("abc123458","Television")
	Modelv2.Product.setItems("abc123459","Laptop")
	Modelv2.Product.setItems("abc123450","Desktop")

# Start by connecting to SQLite database and creating the tables for Sales, Customers and Products
	Modelv2.salesTable()
	Modelv2.customersTable()
	Modelv2.productsTable()

	grv = Viewv2.returnvalues()

	checkCC()
	checkC_ID()
	checkSales()

	CustID = int(grv[0])
	CC = int(grv[1])
	SKU = grv[2]
	sales = float(griv[3])
	datePOS = grv[4]
	dateCV = grv[5]

	hold = POS(CustID, CC, SKU, sales, datePOS)
	hold.submit()





#main()

