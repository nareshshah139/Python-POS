#Controllerv2.py

import modeldb as Modelv2
import sqlite3

#import Viewv2

def main():

	conn = sqlite3.connect('pos.db')
	c = conn.cursor()

# Start by connecting to SQLite database and creating the tables for Sales, Customers and Products
	Modelv2.salesTable()
	Modelv2.customersTable()
	Modelv2.productsTable()


	Modelv2.Product.setItems("abc123456","Vacuum cleaner")
	Modelv2.Product.setItems("abc123457","Radio")
	Modelv2.Product.setItems("abc123458","Television")
	Modelv2.Product.setItems("abc123459","Laptop")
	Modelv2.Product.setItems("abc123450","Desktop")



# Launch GUI with gui() function?
	#Viewv2.gui()

main()


	
