# ljcontrol.py

# sale 300 CC SKU:alpha1234 ID: 9alphanum

import random
import view
import model

def main():
	temp = 0
	while (temp!=1):
		userpinput = input("Please submit the sale information > ")

		inputList = []
		inputList = userinput.split()



if "sale" in input.lower():
	# enter sale info
	custID = checkID(inputList)
	salesInput(inputList, custID)


elif "customer" in input.lower():
	# enter customer id

elif "crm" in input.lower():
	# call 

elif "report" in input.lower():
	# call report function

elif "close day" in input.lower():
	# call close day function

else:
	# print error


def salesInput(inputList, custID):

	for element in inputList:
		try:
			round(float(element),2)
			
		except:
			# error




	def checkID(inputList):
		if "id:" in userinput:
			for element in inputList:
				if element.startswith == 'ID:':
					return element.split(:)[1]
		else:
			return "Anonymous"