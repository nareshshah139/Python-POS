def inputPurchase():
    """
    Use this function to prompt the user for input for purchases
    """
    purchase = input("Please input purchase variables: ")
    return purchase

def printError():
    print("The input you provided is incorrect")



# do we need these?

def printCRM(crm):
    """
    Use this function to print out a summary of the CRM function
    """
    #Define how to print aggregated values
    print(crm)

def printReport(report):
    """
    Use this function to print out a summary sales for the current day
    """
    #Define how to print aggregated values
    print(report)

def printCloseSales(closeSales):
    """
    Use this function to print out a summary of the current day, clear out the dictionaries and end the day and program
    """
    #Define how to print aggregated values
    print(closeSales)

def idMatch():
    print("This ID already exists in the database, please try another ID.")
    
def intro():
	print("Welcome to Noob_POS1977\n"
    "Possible Inputs:\n"
    "1.Sale AMOUNT SKU:NUMBER CC or leave blank for cash payment ID:NUMBER \n"
    "2.Customer NAME ID:123456789 - to create a new customer, checks whether your ID is taken already.\n"
    "3.CRM - to print breakdown of sales per client. \n"
    "4.Report - to print Sales for the day with a cash vs Credit Card breakdown. \n"
    "5.Close Day - to clear the books and end your day. \n")