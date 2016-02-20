# check for upper en lower letters

import random
import view 
import model 

def main():
	temp = 0
	while(temp!=1):
		view.intro()
		userinput = input("Please Enter a command > ")
		#Parser starts here
		inputList = []
		inputList = userinput.split()

		#Basic idea: Look for CustID as a alphanumeric in the list. If the list finds an alphanumeric, look for a number
		#in the list which is definitely the Sale value. Look for a list value = CC to classify it as a CC Sale. Look for a
		#alphanumeric value which can be parsed as a name. Do the same with a default customer ID otherwise.
	
	
### Sale NUMBER CC SKU:number ID:alphanum9
### Customer NAME ID

		if 'sale' in userinput.lower():
			custID = checkID(userinput, inputList)
			salesInput(inputList, custID, userinput)
		elif 'customer' in userinput.lower(): 
			customerInput(inputList)
		elif 'crm' in userinput.lower():
			CRM()
		elif 'report' in userinput.lower():
			ReportCall1()
		elif 'close day' in userinput.lower():
			model.closeDay()
		else:		
			view.printError()
		
 
        
		
def salesInput(inputList, custID, userinput):

    if 'CC' in inputList:
        model.setCC(custID, 1)
    else :
        model.setCC(custID, 0)

    if 'SKU:' in userinput:
        for word in inputList:
            if word.startswith('SKU:'):
                sku = word.split(':')[1]
                model.setSKU(custID, sku)
            
    else:
        model.setSKU(custID, 0)

    for word1 in inputList:
        try:
            saleAMT = float(word1)
            if saleAMT < 10000:
                model.setSales(custID,saleAMT)
            else:
                pass
        except:
            pass
    """
        if word1.lower() == 'sale':
            i = inputList.index(word1)
            sales = float(inputList[i+1])
            model.setSales(custID, sales)
       """ 
	
	
def checkID(userinput, inputList):	
#check whether ID already exist
	if 'id:' in userinput.lower():		
		for element in inputList:
			if element.startswith('ID:'):
				return element.split(':')[1]
			elif element.startswith('id:'):
				return element.split(':')[1]
	else: 
		return 'Anonymous'
			
		
				
def customerInput(inputList):
    #first check whether ID exists somewhere in the dictionary dName
    if inputList[2].split(':')[1] in model.dName:
        view.idMatch()
        main()
    else:
        model.setCustomerNAME(inputList[2].split(':')[1], inputList[1])
        print(model.dName)
    
					
	
				  

		

#def CommandCall():
     #Call the set functions from model and the  input functions from view to take user input and enter commands data into the model


def ReportCall1():
    #Call the Get functions from model and use the view functions to print a report
	cashCC = model.CashCC()
	view.printReport(cashCC)


def CRM():
    #Call the Get functions from model and use the view functions to print a CRM Report
	total = model.crm()
	view.printCRM(total)




main()
