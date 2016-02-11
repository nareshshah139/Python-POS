
import random
import View
import Model

def main():
	temp = 0
	while(temp!=1):
		# ask user for input string
		userinput = input("Please Enter a command > ")
		#Parser starts here
		# create empty list for inputs
		inputList = []
		# take userinput and splits it on spaces
		inputList = userinput.split()
		# if inputList has Sale in first location of the list
		if inputList[0] == 'Sale':
			# if the number of inputs is 2
			if len(inputList) == 2:
				#
				if inputList[1].isnumeric():
					model.setSales(float(inputList[1]))

				elif inputList[1].isalnum():
					model.setSKU(float(inputList[1].split(':')[1]))
				else:
					view.printError()

			elif len(inputList) == 3:

				if inputList[2] == 'CC':
					model.setCC(inputList[2])
					model.setSales(inputList[1])
				elif inputList[2].isalnum():
					model.setSales(inputList[1])
					model.setCustID(inputList[2])
				else:
					view.printError()
			else:
				view.printError()

		elif inputList[0].lower() == 'customer':
			model.setCustID(inputList[2])
			model.setCustomerName(inputList[2],inputList[1])
		elif inputList[0].lower() == 'close day':
			closeday()
		elif inputList[0].lower() == 'report':
			ReportCall1()
		elif inputList[0].lower() == 'crm':
			CRM()
		elif inputList[0].lower() == 'help':
			view.printCommandList()
		else:
			view.printError()


def ReportCall1():
        #Call the Get functions from model and use the view functions to print a report
		view.printReport(model.CashCC())


def CRM():
        #Call the Get functions from model and use the view functions to print a CRM Report
		view.printCRM(model.sumSales())


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
