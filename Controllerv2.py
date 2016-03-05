#Controllerv2.py

import Modelv2
import Viewv2

def main():

# Start by connecting to SQLite database and creating the tables for Sales, Customers and Products

	Modelv2.salesTable()
	Modelv2.customersTable()
	Modelv2.productsTable()

# Launch GUI with gui() function?
	Viewv2.gui()