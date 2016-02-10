def inputCustid():
    #Take input sales command and put it into controller
    id = 1
    newCust = input("is this a new customer (y/n)")
    if('Y' == newCust.upper()):
        name = input("enter the customer's name")
        custid = id
        id = id +1
    else :
        custid = input("Enter the customer's ID")
        name = input("Enter the customer's name")
    return custid, name

def inputSales():
    sales = 0
    while sales != type(float):
        sales = input("Enter the sales amount in €: ")
        try:
            float(sales)
            return sales
        except:
            print("Error")



def inputSKU():
    sku = ''
    # while loop to ensure the right SKU format
    while len(sku)!=9:
        # have user input SKU
        sku = input("Enter the SKU: ")
        # check whether the SKU is in the correct format alphanumeric length 9
        if len(sku)==9:
            # feedback to user
            print("Correct format ")
            return sku
        # if format is wrong have user input it again
        elif len(sku)!=9:
            print("Please enter a SKU in the correct format (9 digits): ")
    # no way to check wehterh SKU exists in our dictionary as we are not storing anything yet



def inputCC():
    cc = 2
    while(cc not in [0,1]):
        cc = input("Cash (0) or CreditCard (1)?")
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