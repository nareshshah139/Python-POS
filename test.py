def inputCustid():
    #Take input sales command and put it into controller
    id = 1
    newCust = input("Is this a new customer (y/n): ")
    if('Y' == newCust.upper()):
        name = input("Enter the customer's name: ")
        custid = id
        id = id +1
    else :
        custid = input("Enter the customer's ID: ")
        name = input("Enter the customer's name: ")
    return custid, name

def inputSales():
    sales = input("Enter the amount of sales in €: ")
    return sales

def inputSKU():
    sku = input("Enter the SKU: ")
    return sku

def inputCC():
    cc = 2
    while(cc not in [0,1]):
        cc = input("Cash (0) or CreditCard (1)? ")
        cc= int(cc)
    return cc


def printCRM(crm):
    #Define how to print aggregated values
    print(crm)


def printReport(report):
    #Define how to print aggregated values
    print(report)

def printCloseSales(closeSales):
    #Define how to print aggregated values
    print(closeSales)


print(inputCustid())
print(inputSales())
print(inputSKU())
print(inputCC())
printCRM(2)
printReport(3)
printCloseSales(4)