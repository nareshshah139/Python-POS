
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
