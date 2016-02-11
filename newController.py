
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
		#Checks if the user started by inputing the sale price
		if inputList[0] == 'Sale':
			#Checks if the user inputed two values
			if len(inputList) == 2:
				#If second entry is numeric it's the sale price
				if inputList[1].isnumeric():
					model.setSales(float(inputList[1]))
				#If second entry is alphanumeric it's the SKU
				elif inputList[1].isalnum():
					model.setSKU(float(inputList[1].split(':')[1]))
				else:
					view.printError()
			#Checks if the user inputed three values
			elif len(inputList) == 3:
				#If third entry is CC adds it to the Credit Card count
				if inputList[2] == 'CC':
					model.setCC(inputList[2])
					#and second one to the Sales
					model.setSales(inputList[1])
				#else dd the second one to the Sales
				elif inputList[2].isalnum():
					model.setSales(inputList[1])
					#and the third one as Cuctomers Name
					model.setCustID(inputList[2])
				else:
					view.printError()
			else:
				view.printError()
		#Checks if the user started by inputing the customer name
		elif inputList[0].lower() == 'customer':
			#assings the third value as customer id
			model.setCustID(inputList[2])
			model.setCustomerName(inputList[2],inputList[1])
		#Checks if the user wants to close the sales for that day
		elif inputList[0].lower() == 'close day':
			closeday()
		#Checks if the user wants to print the sales for that day with cash or CC breakdwon
		elif inputList[0].lower() == 'report':
			ReportCall1()
		#Checks if the user want to print the sale for that day by client
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
