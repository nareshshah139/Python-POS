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
			custID = checkID(inputList)
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
		setCC(custID, 1)
	else : 
		setCC(custID, 0)
		
	if 'SKU:' in inputList:
		for word in inputList:
			if word.startswith('SKU:'):
				sku = word.split(':')[1]
				setSKU(custID, sku)
	else:
		setSKU(custID, sku)
	
	for element in inputList:
        try:
            saleAMT = float(element)
            if saleAMT < 10000:
                setSales(custID,saleAMT)
            else:
                pass
        except:
            pass
		
		"""
		if word.lower() == 'sale' :
			i = inputList.index(word)
			sales = float(inputList[i+1])
			model.setSales(custID, sales)
			"""
        
		
	
	
	
	
	
def checkID(inputList)	
#check whether ID already exist
	if 'id:' in userinput:		
		for element in inputList:
			if element.startswith == 'ID:':
				return element.split(':')[1]
	else: 
		return 'Anonymous'
			
		
				
						
	
			
					
						
		  

		


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
