# Controllerv2.py

import modeldb as Modelv2
import sqlite3


def formatError():
	print("formatError")
	return "Sorry, wrong format."

def broke():
	print("broke")
	return "Did you even buy anything? Enter a sale > 0.00"

def bigspender():
	print("bigspender")
	return "Are you sure? Toilet paper doesn't cost $400..."

def notcust():
	print("notcust")
	return "Sorry, we don't recognize your ID. Please create a new customer."


def checkCC(list1):
	print("checking CC")
	try:
		if int(list1[1]) == 1:
			return ""
		elif int(list1[1]) == 0:
			return ""
		else:
			return formatError()
	except:
		return formatError()

def checkC_ID(list1):
	print("checking C_ID")
	return ""
	try:
		ccid = list1[0]
		return ""
		custIDT = Modelv2.Customer.checkCust()
		if ccid in custIDT:
			return ""
		else:
			return notcust()
	except:
		return formatError()

def checkSales(list1):
	print("checking sales")
	try:
		if int(list1[3]) > 400:
			return bigspender()
		elif int(list1[3]) > 0:
			return ""
		else:
			return broke()
	except:
		return formatError()


def allerrors(list1):
	print("I'm in all errors")
	return checkCC(list1) + "\n" + checkC_ID(list1) + "\n" + checkSales(list1)






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
    Modelv2.Customer.checkCust()


# GETS VALUES FROM GUI, CHECKS FORMATS, CREATES POC OBJECT, SUBMITS TO DB


# Not sure if it is identifying existing customers properly
# It IS checking sales amount correctly
# Need to change print() functions to display on GUI visually

def newsalebutton(list1):
	try:
		CustID = str(list1[0])
# Check if the CustID exists
		custIDT = Modelv2.Customer.checkCust()
		print("latest ID entered:  ", CustID)
		print("list of strings?   ", CustIDT)
		if CustID in custIDT:
			print("Existing Customer")
		else:
			print("New Customer")
		CC = int(list1[1])
		SKU = SKUcode(list1)
		sales = float(list1[3])
# Check if sales > 400 or <=0
		if sales > 400:
			return bigspender()
		elif sales > 0:
			return
		else:
			return broke()
		datePOS = list1[4]
		print(CustID, CC, SKU, sales, datePOS)
		
		hold = Modelv2.POS(CustID, CC, SKU, sales, datePOS)
		hold.submit()
	except:
		print("something broke")
#		return formatError()

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

"""# GETS VALUES FROM GUI, CHECKS FORMATS, CREATES CUSTOMER OBJECT, SUBMITS TO DB """

def newcustbutton(clist):
	try:
		name = clist[0]
# check if CID exists --> return their customer ID
		dateCV = clist[1]
		cnew = Modelv2.Customer(name, dateCV)
		cnew.push()
	except:
		pass

main()

a= Modelv2.Customer("Brains","22/08/1990")
Modelv2.Customer.push(a)
"""
b= Modelv2.POS(123,1,"aer135",12,"12/03/2016")
Modelv2.POS.submit(b)
"""
a = Modelv2.POS.CRM()
print(a)

def getSKUItems():
    skus =Modelv2.Product.getItems()
    return skus

getSKUItems()