
def inputPurchase():
	return 0


def inputCustID():
    #Take input sales command and put it into controller
    id = 1
    print("<3 Rose")
    newCust = input("is this a new customer (y/n)")
    if('Y' == newCust.upper()):
        name = input("Enter the customer's name ")
        custid = id
        id = id +1
    else :
        custid = input("Enter the customer's ID")
        name = input("Enter the customer's name")
    return custid, name

def inputName():
	return input("input name por favor")

def inputSales():
    sales = input("Enter the sales amount in €: ")
    return sales
#put this into controller
    # set sales to 0
    sales = 0
    # while loop to check whether input can be converted to float
    while sales != type(float):
        # have user input the sales amount
        sales = input("Enter the sales amount in €: ")
        try:
            # try to convert sales input to float
            sales = float(sales)
            # if it works return sales
            return sales
        except:
            # provide an error message explaining wrong input
            print("Input:", sales,"is  invalid. Please provide a number in format 1 or 1.00 ")



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
	# check for when characters are added


def inputCC():
    #Take input credit card command and put it into controller
    cc = 2
    while (cc not in [0,1]):
        try:
            cc = int(input("Cash (0) or CreditCard (1)?"))
            if (cc not in [0,1]):
                print("Wrong input! Either 0 for Cash or 1 for CreditCard!")
                cc = int(input("Cash (0) or CreditCard (1)?"))
            else:
                break
        except:
            print("Wrong input! Either number 0 or 1 not CHARACTERS!")
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
