
# Dictionary of Customers: {id: Name}
# Values must be strings
dName = {}

# Dictionary of Sales: {id: sales}
# Values must be floats of 2 decimals
dSales = {}
#print("%.2f" % 3.14159)
#print("%.2f" % round(sales,2))


# Dictionary of SKUs: {id: SKU}
# Values must be 9 digit alphanumerics
dSKU = {}

# Dictionary of CC vs. Cash {id: CC}
# Values must be 0 or 1
dCC = {}

# Dictionary of total sales by customer ID
# values must be floats
dCustSales = {}

Customers = set()

def setSales(id,sales):
    #Add Sales to the list in the dictionary
    dSales.setdefault(id, []).append(sales)
    
    
print(dSales)

def setSKU(id,SKU):
	dSKU.setdefault(id, []).append(SKU)
	

def setCC(id,CC):
    dCC.setdefault(id,[]).append(CC)
   

def setCustomerNAME(id,Name):  #changed
    dName.update({id:Name})


# Takes as argument the Name input by customer
# Generates a new customer ID
# Adds the customer ID and name to the dictionary
def setCustID(CustID):
	Customers.add(CustID)

def closeDay():
	"""Resets all dictionaries, closing out the day."""
	dName = {}
	dSales = {}
	dSKU = {}
	dCC = {}
	dCustSales = {}
	print("The day has been closed and books cleared.")

def getSales(CustID):
	"""Retrieves the sales values for the customer ID input as an argument."""
	return dSales[CustID]

def getSKU(CustID):
	"""Retrieves the SKU values for the customer ID input as an argument."""
	return dSKU[CustID]

def getCCSales(CustID):
    return dSales(CustID)

def getName(CustID):
    return dName(CustID)


def getCustID():
	return CustID

# change name to closeDay()
def sumSales():
	tot = 0
	for key, value in dSales.items():
		a = value
		b = sum(a)
		tot = tot + b
	return (tot)

sumSales()

# change name to report()
def CashCC():
	totCC = 0
	totCash = 0
	for key, value in dCC.items():
		for i in value:
			if i == 1:
				totCC = totCC + (dSales[key])[value.index(i)]
			else :
				totCash = totCash + (dSales[key])[value.index(i)]
	return (totCC, totCash)

CashCC()

#####{custID123: [123,8 0, 100, 12]}


def crm():
    totCust = 0
    for key, value in dSales.items():
        purchase = value
        totCust = sum(purchase)
        dCustSales.update({key:totCust})
    return dCustSales

crm()






