# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 05:50:30 2016

@author: nareshshah
"""

import ViewOld as view
import Model as model

def main():
	temp = 0
	while(temp!=1):
		userinput = input("Please Enter a command")
		#Parser starts here
		inputList = []
		inputList = userinput.split()
		if inputList[0] == 'Sale':
			if len(inputList) == 2:
				
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
				
	

main()
