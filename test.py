dName = {}
dSales = {2:[3],5:['t']}
dSKU = {}
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

def setCustomerID(id,Name):
    dName.update({id:Name})

def getSales(CustId):
    return dSales[CustId]

def getSKU(CustID):
    return dSKU[CustID]

def getCCSales(CustID):
    return dSales(CustID)

def getName(CustID):
    return dName(CustID)