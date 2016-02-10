# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
class Controller:
    def __init__(self,):
        #initialize objects of Model and View classes here
        #Define while loop and control logic here
				self.model = Model()
				self.view = View()
				custID = random.randint(0,10000)
				temp = 0
				
					
				
	

    def CommandCall(self,):
        #Call the set functions from model and the  input functions from view to take user input and enter commands data into the model
        while(temp!=0):
					choice = input("Please enter the correct choice 1 for sales input,2 for SKU input and 3 for CC input ")
					if choice == 1:
						self.model.setSales(custID,self.view.inputSales())
					elif choice == 2:
						self.model.setSKU(custID,self.view.inputSKU())
					elif choice == 3:
						self.model.setCC(custID,self.view.inputCC())
					else:
						temp =1

    def ReportCall1(self,):
        #Call the Get functions from model and use the view functions to print a report
				printReport()

    def CRM(self,):
        #Call the Get functions from model and use the view functions to print a CRM Report
				printCRM()

    def closeday(self,):
        #Close the program and aggregate values in the list. Call get functions from model to do this
				printCloseSales()
