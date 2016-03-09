# Controllerv2.py

import modeldb as Modelv2
import sqlite3
import pandas as pd

def formatError():
	return "Sorry, transaction failed. Please complete all fields."

def broke():
	return "Did you buy anything? Please enter a sale > 0"

def bigspender():
	return "Are you sure? Toilet paper doesn't cost $500..."

def notcust():
	return "Please create a new customer ID."

def existingcust():
	return "Welcome back, good sire."

def saleconf():
	return "Thank you for your sale! Have dandy dia!"

def newcustconf():
	newest = c.execute("SELECT max(CustIDcol) FROM customers")
	return "Great to have a new customer! Your ID # is %s" % (newest)

def noproduct():
	return "Please pick the product purchased."


#def checkCC(list1):
#	print("checking CC")
#	try:
#		if int(list1[1]) == 1:
#			return ""
#		elif int(list1[1]) == 0:
#			return ""
#		else:
#			return formatError()
#	except:
#		return formatError()

#def checkC_ID(list1):
#	print("checking C_ID")
#	return ""
#	try:
#		ccid = int(list1[0])
#		return ""
#		custIDT = Modelv2.Customer.checkCust()
#		if ccid in custIDT:
#			return ""
#		else:
#			return notcust()
#	except:
#		return formatError()

#def checkSales(list1):
#	print("checking sales")
#	try:
#		if int(list1[3]) > 400:
#			return bigspender()
#		elif int(list1[3]) > 0:
#			return ""
#		else:
#			return "Did you even buy anything? Enter a sale > 0.00"
#	except:
#		return formatError()



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


# GETS VALUES FROM GUI, CHECKS FORMATS, CREATES POC OBJECT, SUBMITS TO DB

def newsalebutton(list1):
#	try:
#		CustID = int(list1[0])
#		CC = int(list1[1])
#		SKU = SKUcode(list1)
#		sales = float(list1[3])
#		datePOS = list1[4]
#		print(CustID, CC, SKU, sales, datePOS)
#
#		hold = Modelv2.POS(CustID, CC, SKU, sales, datePOS)
#		hold.submit()
	try:
		CustID = str(list1[0])
		custIDT = Modelv2.Customer.checkCust()
		zzz = [item for item in custIDT if CustID in item]
		thresh = 0
		errors = []
		print("errors", errors)
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
	#			print(CustID, CC, SKU, sales, datePOS)			
#			print("input vars:", CustID, CC, SKU, sales, datePOS)
			if thresh == 3:
				hold = Modelv2.POS(CustID, CC, SKU, sales, datePOS)
			#print("hold attributes:", hold.CustID, hold.SKU, hold.CC, hold.sales, hold.datePOS)
				Modelv2.POS.submit1(hold)
				errors.append(saleconf())
#				alphabet = a #+ b + c + d + g + h# + j

			else:
#				print("not meeting all 3 criteria")
				errors.append(formatError())
		return errors
#			print("errors AFTER:  ",errors)
#		print("alphabet in try:  ", alphabet)
#		return alphabet
	except(RuntimeError, TypeError, NameError):
		print("what's going on???")
		print(RuntimeError, TypeError, NameError)
#		formatError()

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
		newcustconf()
	except:
		pass


def allerrors():
	print("allerrors: ", alphabet)
	return alphabet
#	return checkCC(list1) + "\n" + checkC_ID(list1) + "\n" + checkSales(list1)

main()

a= Modelv2.Customer("brains","22/08/1990")
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
