
# Dictionary of Customers: {id: Name}
# Values must be strings
dName = {}

# Dictionary of Sales: {id: sales}
# Values must be floats of 2 decimals
dSales = {2:[3],5:['t']}
#print("%.2f" % 3.14159)
#print("%.2f" % round(sales,2))


# Dictionary of SKUs: {id: SKU}
# Values must be 9 digit alphanumerics
dSKU = {}

# Dictionary of CC vs. Cash {id: CC}
# Values must be 0 or 1
dCC = {}



def setSales(id,sales):
    #Add Sales to the list in the dictionary
    dSales.setdefault(id, []).append(sales)


setSales(2,3)

print(dSales)

def setSKU(id,SKU):
    dSKU.setdefault(id, []).append(SKU)


def setCCSales(id,CC):
    dCC.setdefault(id,[]).append(SKU)

def setCustomerNAME(id,Name):  #changed
    dName.update({id:Name})

def newCustomer(Name):
# Takes as argument the Name input by customer
# Generates a new customer ID
# Adds the customer ID and name to the dictionary



def getSales(CustId):
    return dSales[CustId]

def getSKU(CustID):
    return dSKU[CustID]

def getCCSales(CustID):
    return dSales(CustID)

def getName(CustID):
    return dName(CustID)
    
def setCustID(CustID):
	custID.add(CustID)
	
def getCustID():
	return custID
	
def sumSales():
	tot = 0 
	for key, value in dSales.items():
		a = value
		b = sum(a)
		tot = tot + b
	print (tot)

sumSales()
