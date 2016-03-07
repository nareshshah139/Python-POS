# Controllerv2.py

import modeldb as Modelv2
import sqlite3
import Notebook1 as Viewv2


def formatError():
    return "Sorry, wrong format."


def noSale():
    return "Did you even buy anything? Enter a sale > 0.00"


def bigspender():
    return "Are you sure? Toilet paper doesn't cost $400..."


def notcust():
    return "Sorry, we don't recognize your ID. Please create a new customer."


def checkCC():
    try:
        if int(Viewv2.grv[1]) == 1:
            return ""
        elif int(Viewv2.grv[1]) == 0:
            return ""
        else:
            return formatError()
    except:
        return formatError()


def checkC_ID():
    try:
        ccid = int(Viewv2.grv[1])
        return ""
        custIDT = Modelv2.Customer.checkCust()
        if ccid in custIDT:
            return ""
        else:
            return notcust()
    except:
        return formatError()


def checkSales():
    try:
        if int(Viewv2.grv[3]) > 0:
            return ""
        elif int(Viewv2.grv[3]) > 400:
            return bigspender()
        else:
            return noSale()
    except:
        return formatError()


def allerrors():
    '''collects a list of all the errors'''
    return checkCC() + "\n" + checkC_ID() + "\n" + checkSales()


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

#    Modelv2.Product.setItems("abc123456", "Vacuum cleaner")
#    Modelv2.Product.setItems("abc123457", "Radio")
#    Modelv2.Product.setItems("abc123458", "Television")
#    Modelv2.Product.setItems("abc123459", "Laptop")
#    Modelv2.Product.setItems("abc123450", "Desktop")


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
def newcustbutton():
    clist = Viewv2.newcustinfo()
    try:
        name = clist[0]
        dateCV = clist[1]
        cnew = Modelv2.Customer(name, dateCV)
        cnew.push()
    except:
        pass


main()

#a= Modelv2.Customer("Bigboobs","22/08/1990")
#Modelv2.Customer.push(a)


