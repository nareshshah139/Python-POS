import random
import view
import model

def main():
	custID = random.randint(0,10000)
	temp = 0
	while(temp!=1):
		custID = view.inputCustID()
		model.setCustID(CustID)
		model.setCustomerNAME(custID,name)
		model.setSKU(custID, view.inputSKU())
		model.setCC(custID,view.inputCC())
		model.setSales(custID, view.inputSales())

		while view.inputSales() != type(float):
			view.inputSales()
			try:

        # have user input the sales amount
        sales = input("Enter the sales amount in €: ")
        try:
            # try to convert sales input to float
            sales = float(sales)
            # if it works return sales
            return sales
        except:
            # provide an error message explaining wrong input
            print("Input:", sales,"is  invalid. Please provide a number in format 1 or 1.00 ")

				
					
				
	

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
				
	
