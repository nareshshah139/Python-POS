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
<<<<<<< HEAD
	
	
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

		
=======

		for element in inputList:
			try:
				round(float(element),2)
			except:
				view.printError()

			finally:
				if element.isalnum():
					for element2 in inputList:
						# catch sales amount
						if element2.isnumeric():
							model.setSales(element,float(element2))
						elif element2.lower() == 'CC':
							model.setCC(element,element2)
						elif element2.startswith('SKU:'):
							model.setSKU(element,float(element2.split(':')[1]))
						elif element2.isalpha():
							model.setCustomerNAME(element,element2)
						else:
							view.printError()
				else:
					if element.isnumeric():
						model.setSales('Anon12345',float(element))
					elif element == 'CC':
						model.setCC('Anon12345',element)
					elif element2.startswith('SKU:'):
						model.setSKU('Anon12345',float(element.split(':')[1]))
					elif element.isalpha():
						model.setCustomerNAME('Anon12345',element)
					elif element.lower() == 'close day':
						closeday()
					#Checks if the user wants to print the sales for that day with cash or CC breakdwon
					#Example command: report
					elif element.lower() == 'report':
						view.printReport(model.CashCC())
					#Checks if the user want to print the sale for that day by client
					#Example command: crm
					elif element.lower() == 'crm':
						view.printCRM(model.sumSales())
					#Example command: help
					elif element.lower() == 'help':
						view.printCommandList()
					else:
						view.printError()
>>>>>>> 7f3b6115dad5cc50b83545fbafeb8eee37b9e66c


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
