import random
import ViewOld as view
import Model as model

def main():
	temp = 0
	while(temp!=1):
		CustID = view.inputCustID()
		model.setCustID(CustID)
		model.setCustomerNAME(CustID, view.inputName())
		model.setSKU(CustID, view.inputSKU())
		model.setCC(CustID,view.inputCC())
		model.setSales(CustID, view.inputSales())
		
		
		
				
					
				
	

        

def ReportCall1():
        #Call the Get functions from model and use the view functions to print a report
		cash = model.CashCC()
		view.printReport(cash)
	

def CRM():
        #Call the Get functions from model and use the view functions to print a CRM Report
		total = model.sumSales()
		view.printCRM(total)
			

def closeday(self,):
        #Close the program and aggregate values in the list. Call get functions from model to do this
		ReportCall1()
		CRM()		
		printCloseSales()
				
	

main()