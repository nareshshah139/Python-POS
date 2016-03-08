# Controllerv2.py

import modeldb as Modelv2
import sqlite3


def formatError():
    return "Sorry, wrong format."

def noSale():
    return "Did you even buy anything? Enter a sale > 0.00"

def bigspender():
    return "Are you sure? Toilet paper doesn't cost $400..."

def notcust():
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
'''
    try:
        ccid = int(list1[0])
        return ""
        custIDT = Modelv2.Customer.checkCust()
       	if ccid in custIDT:
         	return ""
	    else:
        	return notcust()
    except:
        return formatError()
'''

def checkSales(list1):
	print("checking sales")
	try:
		if int(list1[3]) > 400:
			return bigspender()
		elif int(list1[3]) > 0:
			return ""
		else:
			return "Did you even buy anything? Enter a sale > 0.00"
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


# GETS VALUES FROM GUI, CHECKS FORMATS, CREATES POC OBJECT, SUBMITS TO DB

def newsalebutton(list1):
	
# should we check for negative numbers, etc. here before pushing?
# check if CustID exists
	try:
		CustID = int(list1[0])
		CC = int(list1[1])
		SKU = list1[2]
		sales = float(list1[3])
		datePOS = list1[4]
		print(CustID, CC, SKU, sales, datePOS)
		
		hold = Modelv2.POS(CustID, CC, SKU, sales, datePOS)
		hold.submit()
	except:
		pass

# GETS VALUES FROM GUI, CHECKS FORMATS, CREATES CUSTOMER OBJECT, SUBMITS TO DB
def newcustbutton(clist):
    try:
        name = clist[0]
        dateCV = clist[1]
        cnew = Modelv2.Customer(name, dateCV)
        cnew.push()
    except:
        pass

main()

a= Modelv2.Customer("Bigboobs","22/08/1990")
Modelv2.Customer.push(a)

b= Modelv2.POS(123,1,"aer135",12,"12/03/2016")
Modelv2.POS.submit(b)

a = Modelv2.POS.CRM()
print(a)

def getSKUItems():
    skus =Modelv2.Product.getItems()
    print(skus)

getSKUItems()