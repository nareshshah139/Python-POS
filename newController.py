import random
import test
import view

def main():
	custID = random.randint(0,10000)
	temp = 0
	while(temp!=1):
		custID = view.inputCustID()
		model.setCustID(CustID)
		model.setCustomerNAME(custID,name)
		model.setSales(custID, view.inputSales())	
		model.setSKU(custID, view.inputSKU())
		model.setCC(custID,view.inputCC())
					
				
					
				
	

    def CommandCall():
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
				
	
