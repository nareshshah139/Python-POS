def inputCustid():
    #Take input sales command and put it into controller
    id = 100000001
    # this id needs to be = to the highest id stored in the dictionary
    newCust = input("Is this a new customer (y/n): ")
    while newcust not in ['Y','N'] :
        if('Y' == newCust.upper()):
            name = input("Enter the customer's name: ")
            custid = id+1
            #id += 1 # add 1 to highest in dictionary
        elif('N' == newCust.upper()) :
            custid = input("Enter the customer's 9 digit ID: ")
            try: 
                # check if in the database by calling a function
        else :
            newCust = input("Y/N only, please.")
    return custid

def inputSales():
    sales = input("Enter the amount of sales in €: ")
    return sales

def inputSKU():
    sku = input("Enter the Product SKU: ")
    return sku

def inputCC():
    cc = 2
    while(cc not in [0,1]):
        cc = input("Paid in Cash (0) or CreditCard (1)? ")
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