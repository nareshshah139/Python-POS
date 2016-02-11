
import random
import view
import model

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
		
		for element in inputList:
			if inputList[element].isalnum():
				for element2 in inputList:	
					if inputList[element2].isnumeric():
						model.SetSales(inputList[element],float(inputList[element2]))
					elif inputList[element2].lower() == 'CC':
						model.SetCC(inputList[element],inputList[element2])
					elif inputList[element2].startswith('SKU:'):
						model.SetSKU(inputList[element],float(inputList[element2].split(':')[1]))
					elif inputList[element2].isalpha():
						model.SetCustomerName(inputList[element],inputList[element2]
					else:
						view.printError()
			else:
				if inputList[element].isnumeric():
					model.SetSales('Anon12345',float(inputList[element]))
				elif inputList[element] == 'CC':
					model.SetCC('Anon12345',inputList[element])
				elif inputList[element2].startswith('SKU:'):
					model.SetSKU('Anon12345',float(inputList[element].split(':')[1]))
				elif inputList[element].isalpha():
					model.SetCustomerName('Anon12345',inputList[element]
				elif inputList[element].lower() == 'close day':
					closeday()
				#Checks if the user wants to print the sales for that day with cash or CC breakdwon
				#Example command: report
				elif inputList[element].lower() == 'report':
					view.printReport(model.CashCC())
				#Checks if the user want to print the sale for that day by client
				#Example command: crm
				elif inputList[element].lower() == 'crm':
					view.printCRM(model.sumSales())
				#Example command: help
				elif inputList[element].lower() == 'help':
					view.printCommandList()
				else:
					view.printError()
			
					
						
		  

		


def closeday(self,):
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


def closeday(self,):
    #Close the program and aggregate values in the list. Call get functions from model to do this
	printCloseSales()

main()
