
# Dictionary of Customers: {id: Name}
# Values must be strings
dName = {}

# Dictionary of Sales: {id: sales}
# Values must be floats of 2 decimals
dSales = {2:[3],5:[4,2]}
#print("%.2f" % 3.14159)
#print("%.2f" % round(sales,2))


# Dictionary of SKUs: {id: SKU}
# Values must be 9 digit alphanumerics
dSKU = {}

# Dictionary of CC vs. Cash {id: CC}
# Values must be 0 or 1
dCC = {2:[1],5:[0,1]}

Customers = set()



def setSales(id,sales):
    #Add Sales to the list in the dictionary
    dSales.setdefault(id, []).append(sales)
    print(dSales)

setSales(2,3)

print(dSales)

def setSKU(id,SKU):
    dSKU.setdefault(id, []).append(SKU)


def setCC(id,CC):
    dCC.setdefault(id,[]).append(CC)

def setCustomerNAME(id,Name):  #changed
    dName.update({id:Name})

def newCustomer(Name):
	return 0
# Takes as argument the Name input by customer
# Generates a new customer ID
# Adds the customer ID and name to the dictionary
def setCustID(CustID):
	Customers.add(CustID)



def getSales(CustID):
	return dSales[CustID]

def getSKU(CustID):
    return dSKU[CustID]

def getCCSales(CustID):
    return dSales(CustID)

def getName(CustID):
    return dName(CustID)


def getCustID():
	return CustID

def sumSales():
	tot = 0
	for key, value in dSales.items():
		a = value
		b = sum(a)
		tot = tot + b
	return (tot)

sumSales()

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

print( CashCC())
