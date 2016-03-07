from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import time
import pandas as pd
import numpy as np


## Creating Master Frame.
root = Tk()
master = Frame(root, name = 'master')
master.pack(fill = BOTH)
root.title('Point of Sale System')
root.protocol('WM_DELETE_WINDOW',master.quit)
n = ttk.Notebook(master, name = 'n')

#-----Fotis-----
#def load_data_sql():
#    connection = sqlite3.connect("pos.db")
#    df = pd.read_sql_query("SELECT * FROM sales, customer LEFT JOIN sales.custid, customer.custid",connection)
#    return(df)

#load_data_sql()


CC = IntVar()
Cash = IntVar()

def callback():
    print('Button Clicked')

graphArray = {'SalesID': [1,2,3,4,5,6,7,8,9,10],
'CustID':['123','123','124','125','122','123','123','124','125','122'],
'Name':['Chris','Chris','Lionel','Jonas','Fotis','Chris','Chris','Lionel','Jonas','Fotis'],
'Payment':['CC','Cash','CC','Cash','CC','Cash','Cash','CC','CC','Cash'],
'SKU':['123456789','123456788','123456788','123456787','123456784','123456789','123456788','123456788','123456787','123456784'],
'Sales':[20,30,30,40,10,20,30,30,40,10],
'Day':[1,1,2,3,4,4,5,5,5,6]}

df = pd.DataFrame(graphArray)
df2 =df.groupby('Name')['Sales'].sum()
df3 = pd.DataFrame({'Name':df2.index, 'TotalSales':df2.values})



##---- Fotis -----
    
CustomerView = ttk.Frame(n)
SalesView = ttk.Frame(n)
POSView = ttk.Frame(n)
ReportView = ttk.Frame(n)
CRMView = ttk.Frame(n)
n.add(POSView, text = 'Point of Sale System View')
n.add(SalesView, text = 'Sales View')
n.add(CustomerView,text = 'New Customer View')
n.add(ReportView, text = 'Report View')
n.add(CRMView, text = 'CRM View')
n.pack(fill = BOTH,expand = TRUE)


# Customer View Tab
# Make a frame to hold all elements
# Make smaller frames in order to hold pairs of elements per line.
# Add buttons with default callback. Callback can be changed to a different function

f1_CV = Frame(CustomerView)
f1_CV.pack(fill = X)

Label(f1_CV,text = 'Customer Name').pack(side = LEFT)
C_Name = Entry(f1_CV)
C_Name.pack(fill = X,padx = 10, expand = TRUE)
C_Name_Var = C_Name.get()
C_Name.delete(0,END)


f2_CV = Frame(CustomerView)
f2_CV.pack(fill = X)
Label(f2_CV,text = 'Customer ID').pack(side = LEFT)


f3_CV = Frame(CustomerView)
f3_CV.pack(fill = X)
Label(f3_CV,text = "Today's date is "+time.strftime("%d/%m/%Y")).pack(side = LEFT)
Date_CV_Var = time.strftime("%d/%m/%Y")
B_Add_User = Button(f3_CV,text = 'Add User', command = callback).pack(side = RIGHT)
B_Switch = Button(f3_CV,text = 'POS Pane',command = callback).pack(side = RIGHT)

# POS View Tab
# Make a frame to hold all elements
# Make smaller frames in order to hold pairs of elements per line.
# Add buttons with default callback. Callback can be changed to a different function
# CC Variable is CC
# CustomerID Variable is C_ID_Var
# SKU Variable is SKU_Var
# Sales Variable is Sales_Var
# Date Variable in POS is Date_POS_Var

f1_POS = Frame(POSView)
f1_POS.pack(fill = X)
Label(f1_POS,text = 'Customer ID').pack(side = LEFT)
C_ID = Entry(f1_POS)
C_ID.pack(fill = X,padx = 5, expand = TRUE)
C_ID_Var = C_ID.get()
C_ID.delete(0,END)

f2_POS = Frame(POSView)
f2_POS.pack(fill = X)
Label(f2_POS,text = 'Credit Card').pack(side = LEFT)
Checkbutton(f2_POS, text="Yes/No", variable=CC).pack(side = LEFT)

f3_POS = Frame(POSView)
f3_POS.pack(fill = X)
Label(f3_POS,text = 'SKU').pack(side = LEFT)
SKU = Entry(f3_POS)
SKU.pack(fill = X,padx = 5, expand = TRUE)
SKU_Var = SKU.get()
SKU.delete(0,END)

f4_POS = Frame(POSView)
f4_POS.pack(fill = X)
Label(f4_POS,text = 'Sales Amount').pack(side = LEFT)
Sales = Entry(f4_POS)
Sales.pack(fill = X,padx = 5,expand = TRUE)
Sales_Var = Sales.get()
Sales.delete(0,END)

f5_POS = Frame(POSView)
f5_POS.pack(fill=X)
Label(f5_POS,text = 'Current Date').pack(side = LEFT)
Label(f5_POS,text = time.strftime("%d/%m/%Y")).pack(side = LEFT, padx = 5)
Date_POS_Var = time.strftime("%d/%m/%Y")


f6_POS = Frame(POSView)
f6_POS.pack(fill = X)
B_POS_Submit = Button(f6_POS,text = 'Submit', command = callback).pack()



#Report View
f1_RV = Frame(ReportView)
f1_RV.pack(fill=X)
Label(f1_RV,text = 'Report and Graphs').pack(padx = 10,pady=10)

f2_RV = Frame(ReportView)
f2_RV.pack(fill=BOTH, expand = TRUE)
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

canvas = FigureCanvasTkAgg(f, f2_RV)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2TkAgg(canvas, f2_RV)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

#CRM View
f1_CRM = Frame(CRMView)
f1_CRM.pack(fill = X)
Label(f1_CRM,text = 'CRM Reports').pack(padx = 10, pady = 10)

f2_CRM = Frame(CRMView)
f2_CRM.pack(fill = BOTH, expand = TRUE)
f1 = Figure(figsize = (5,5),dpi = 100)
ax = f1.add_subplot(111)
df3.plot(x = 'Name', y= 'TotalSales',kind = 'bar', ax = ax)


canvas = FigureCanvasTkAgg(f1, f2_CRM)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2TkAgg(canvas, f2_CRM)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

def returnValues():
    return [CC,C_ID_Var,SKU_Var,Sales_Var,Date_POS_Var]
        

# CC Variable is CC
# CustomerID Variable is C_ID_Var
# SKU Variable is SKU_Var
# Sales Variable is Sales_Var
# Date Variable in POS is Date_POS_Var


def returnvalues():
	return [CC, C_ID_Var, SKU_Var, Sales_Var, Date_POS_Var, Date_CV_Var]









