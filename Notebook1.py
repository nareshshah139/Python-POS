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
'Payment':[1,0,1,0,1,0,0,1,1,0],
'SKU':['123456789','123456788','123456788','123456787','123456784','123456789','123456788','123456788','123456787','123456784'],
'Sales':[20,30,30,40,10,20,30,30,40,10],
'Day':[1,1,2,3,4,4,5,5,5,6],
'Date': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04','2015-01-05', '2015-01-05', '2015-01-06', '2015-01-07','2015-01-08', '2015-01-09']}

transaction_data = {'SalesID': [1,2,3,4,5,6,7,8,9,10],
'CustID':['123','123','124','125','122','123','123','124','125','122'],
'Name':['Chris','Chris','Lionel','Jonas','Fotis','Chris','Chris','Lionel','Jonas','Fotis'],
'Payment':[1,0,1,0,1,0,0,1,1,0],
'SKU':['123456789','123456788','123456788','123456787','123456784','123456789','123456788','123456788','123456787','123456784'],
'Sales':[20,30,30,40,20,20,30,30,40,30],
'Date': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04','2015-01-05', '2015-01-05', '2015-01-06', '2015-01-07','2015-01-08', '2015-01-09']}

df5 = pd.DataFrame(graphArray)
df2 = df5.groupby('Name')['Sales'].sum()
df3 = pd.DataFrame({'Name':df2.index, 'TotalSales':df2.values})

def create_df():
    global df
    df = pd.DataFrame(transaction_data)
    df['CC'] = df['Payment']==1
    df['Cash'] = df['Payment']==0
    df['CCSales'] = df.Sales*df.CC
    df['CashSales']= df.Sales*df.Cash
    return df

#Top Customer Table
#Group dataframe by CustID and take sum of sales
def top_customers():
    df_sales = df[['CustID','Name','Sales']].groupby(['CustID','Name']).agg([np.sum, np.count_nonzero])
    df_sales.columns = ['SalesAmount','ItemCount']
    # Sort by sum of sales in descending order
    df_sales = df_sales.sort_values(['SalesAmount'], ascending=False)
    return df_sales.head(10)


#Top SKU Table
def top_sku():
    df_topSKU = df[['SKU','Sales']].groupby(['SKU']).agg([np.sum, np.count_nonzero])
    df_topSKU.columns=['SalesAmount','SalesCount']
    df_topSKU_sort = df_topSKU.sort_values(['SalesAmount'], ascending=False)
    return df_topSKU_sort.head(10)

#PLOTTING
#Create Sales by Day Table
def sales_overview():
    global daily_sales
    daily_sales = df[['Date','Sales','CCSales','CashSales']].groupby(['Date']).agg([np.sum])
    daily_sales.columns = ['TotalSales','CCSales','CashSales']
    return daily_sales

#create plot
##def sales_plot():
##    global plot1
##    plot1 = daily_sales.plot(title="Sales by Payment Method", xticks=df['Day'],lw=2,colormap='gnuplot',marker='.',markersize=10)
##    plot1.set(xlabel="Date", ylabel="Sales Amount")
##    return plot1

#Create Sales by SKU Table
def sku_overview():
    global sku_sales
    sku_sales = df[['SKU','CCSales','CashSales']].groupby(['SKU']).agg([np.sum])
    sku_sales.columns = ['CCSales','CashSales']
    sku_sales = sku_sales.sort_values(['CCSales'], ascending=False)
    return sku_sales.head(5)



    



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

create_df()
sales_overview()
sku_overview()

ax1 = f.add_subplot(211)
ax3 = f.add_subplot(212)
pd.options.display.mpl_style = 'default'
daily_sales.plot(title="Sales by Payment Method",lw=2, marker='.',markersize=10,ax=ax1)
pd.options.display.mpl_style = 'default'
sku_sales.plot(kind = 'bar',stacked = True,ax = ax3)


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
ax2 = f1.add_subplot(211)
ax3 = f1.add_subplot(212)
df3.plot(x = 'Name', y= 'TotalSales',kind = 'bar', ax = ax2)
df3.plot(x = 'Name',y = 'TotalSales',kind = 'bar',ax=ax3)

canvas = FigureCanvasTkAgg(f1, f2_CRM)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2TkAgg(canvas, f2_CRM)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

def returnValues():
    return [CC,C_ID_Var,SKU_Var,Sales_Var,Date_POS_Var]


        
