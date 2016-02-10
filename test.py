#this is the model

dName = {}
dSales = {2:[3],5:[4]}
dSKU = {}
dCC = {}
custID = set()





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