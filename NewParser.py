# check for upper en lower letters

import random
import View as view
import Model as model

def main():
	temp = 0
	while(temp!=1):
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
			salesInput(inputList, custID)
		elif 'customer' in userinput.lower(): 
			customerInput(inputList)
		elif 'crm' in userinput.lower():
			CRM()
		elif 'report' in userinput.lower():
			ReportCall1()
		elif 'close day' in userinput.lower():
			closeDay()
		else:		
			view.printError()
		
 
        
		
def salesInput(inputList, custID):

    if 'CC' in inputList:
        model.setCC(custID, 1)
    else :
        model.setCC(custID, 0)

    if 'SKU:' in inputList:
        for word in inputList:
            if word.startswith('SKU:'):
                sku = word.split(':')[1]
                model.setSKU(custID, sku)
            else :
                pass
    else:
        model.setSKU(custID, 0)

    for word1 in inputList:
        if word1.lower() == 'sale':
            i = inputList.index(word1)
            sales = float(inputList[i+1])
            model.setSales(custID, sales)
        else:
            pass
	
	
	
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
			
		
				
def customerInput():
    #first check whether ID exists somewhere in the dictionary dName
    if inputList[2].split(':')[1] in model.dName:
        view.idMatch()
        main()
    else:
        model.setCustomerNAME(inputList[1], inputList[2])
    
					
	
			
					
						
# Sale 123 CC SKU:123 ID:123		  

		


def closeDay():
        #Close the program and aggregate values in the list. Call get functions from model to do this
		ReportCall1()
		CRM()
		printCloseSales()
		custID = view.inputCustID()
		model.setCustID(CustID)
		model.setCustomerNAME(custID,name)
		model.setSKU(custID, view.inputSKU())
		model.setCC(custID,view.inputCC())
		model.setSales(custID, view.inputSales())


#def CommandCall():
     #Call the set functions from model and the  input functions from view to take user input and enter commands data into the model


def ReportCall1():
    #Call the Get functions from model and use the view functions to print a report
	cashCC = model.CashCC()
	view.printReport(cashCC)


def CRM():
    #Call the Get functions from model and use the view functions to print a CRM Report
	total = model.sumSales()
	view.printCRM(total)




main()
