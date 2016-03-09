from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import time
import pandas as pd
import numpy as np
import Controllerv2
import matplotlib.pyplot as plt
import modeldb as Modelv2
import matplotlib.animation as animation

##from PIL import Image, ImageTk
plt.style.use('ggplot')
##
##image = Image.open('Dilemma.jpg')
##photo = ImageTk.PhotoImage(image)

## Creating Master Frame. Naming Master Frame as root.
root = Tk()
## Creating a frame inside master frame called master.
master = Frame(root, name = 'master')
master.pack(fill = BOTH)
#Setting display title to be equal to 'Point of Sale System'
root.title('Point of Sale System')
#root.protocol('WM_DELETE_WINDOW',master.quit)
n = ttk.Notebook(master, name = 'n')


# SHOULD NOT GO IN THE GUI
# CONSISTENCY -- THIS AND/OR FETCH?
#-----Fotis-----
#def load_data_sql():
#    connection = sqlite3.connect("pos.db")
#    df = pd.read_sql_query("SELECT * FROM sales, customers WHERE sales.CustIDcol=customers.CustIDcol",connection)
#    return(df)

#load_data_sql()


def callback1():
    '''Callback function to push values from GUI to controller'''
    list1 = [C_ID.get(),CC_Var.get(),SKU_Var.get(),Sales.get(),Date_POS_Var]
    print(list1)
    Controllerv2.newsalebutton(list1)

def callback2():
    '''Callback function for adding new user to the database'''
    list2 = [C_Name.get(), Date_CV_Var]
    print(list2)
    Controllerv2.newcustbutton(list2)

def sel():
    '''Callback function for radiobutton to return values'''
    CC_1 = CC_Var.get()


def printerrors():
    '''Callback function to check values input in GUI for errors and return a printed value'''
    Controllerv2.allerrors()



def create_df():
    ''' Creates Dataframe from the Data collected in the database '''
    global df
    df = pd.DataFrame(Modelv2.POS.getPosData(), columns=['SalesID','CustID','CC','SKU','Sales','Date'])
    df['Cash'] = df['CC']==0
    df['CCSales'] = df.Sales*df.CC
    df['CashSales']=df.Sales*df.Cash
    return df


#Top Customer Table
#Group dataframe by CustID and take sum of sales
def top_customers():
    '''Returns a dataframe of highest paying customers in the Database'''
    df_sales = df[['CustID','Name','Sales']].groupby(['CustID','Name']).agg([np.sum, np.count_nonzero])
    df_sales.columns = ['SalesAmount','ItemCount']
    # Sort by sum of sales in descending order
    df_sales = df_sales.sort_values(['SalesAmount'], ascending=False)
    return df_sales.head(10)


#Top SKU Table
def top_sku():
    '''Returns a dataframe of the highest selling items in the product database '''
    df_topSKU = df[['SKU','Sales']].groupby(['SKU']).agg([np.sum, np.count_nonzero])
    df_topSKU.columns=['SalesAmount','SalesCount']
    df_topSKU_sort = df_topSKU.sort_values(['SalesAmount'], ascending=False)
    return df_topSKU_sort.head(10)

#PLOTTING
#Create Sales by Day Table
def sales_overview():
    ''' Defines Daily sales variables. This allows us to plot graphs '''
    global daily_sales
    daily_sales = df[['Date','Sales','CCSales','CashSales']].groupby(['Date']).agg([np.sum])
    daily_sales.columns = ['TotalSales','CCSales','CashSales']
    return daily_sales


#Create Sales by SKU Table
def sku_overview():
    ''' Defines SKU Sales variable. This allows us to plot graphs '''
    global sku_sales
    sku_sales = df[['SKU','CCSales','CashSales']].groupby(['SKU']).agg([np.sum])
    sku_sales.columns = ['CCSales','CashSales']
    sku_sales = sku_sales.sort_values(['CCSales'], ascending=False)
    return sku_sales.head(5)

#created update_data function to ensure that data entered in the POS will be displayed on graphs once the refresh button is clicked. Have not managed to get this to work.
def animate(i):
    create_df()
    sales_overview()
    sku_overview()
    ax1 = f.add_subplot(211)
    ax3 = f.add_subplot(212)
    #pd.options.display.mpl_style = 'default'
    #pd.options.display.mpl_style = 'default'
    ax1.clear()
    ax3.clear()
    sku_sales.plot(kind = 'bar',stacked = True,ax = ax3)
    daily_sales.plot(ax=ax1)
    print("clicked")




##---- Fotis -----
# Setting the Frames of the notebook in the following order:
# 1 - POS View
# 2 - Sales View
# 3 - Customer View - To Add new customers
# 4 - Report View - To plot Report graphs
# 5 - CRM View - To plot CRM graphs

CustomerView = ttk.Frame(n)
SalesView = ttk.Frame(n)
POSView = ttk.Frame(n)
ReportView = ttk.Frame(n)
CRMView = ttk.Frame(n)
n.add(POSView, text = 'Point of Sale System View')
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
B_Add_User = Button(f3_CV,text = 'Add User', command = callback2).pack(side = RIGHT)

# POS View Tab
# Make a frame to hold all elements
# Make smaller frames in order to hold pairs of elements per line.
# Add buttons with default callback. Callback can be changed to a different function
# CC Variable is CC_Var
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

f2_POS = Frame(POSView)
f2_POS.pack(fill = X)
Label(f2_POS,text = 'Payment').pack(side = LEFT)
CC_Var = IntVar()
CC = Radiobutton(f2_POS, text="Credit Card", variable=CC_Var, value=1,command=sel).pack(side = LEFT)
Cash = Radiobutton(f2_POS,text = "Cash",variable = CC_Var,value=0,command = sel).pack(side = LEFT)

f3_POS = Frame(POSView)
f3_POS.pack(fill = X)
Label(f3_POS,text = 'Product').pack(side = LEFT)
SKU_Var = StringVar()
SKU = OptionMenu(f3_POS,SKU_Var,'Vacuum Cleaner','Radio','Television','Laptop','Desktop')
SKU.pack(fill = X,padx = 5, expand = TRUE)


f4_POS = Frame(POSView)
f4_POS.pack(fill = X)
Label(f4_POS,text = 'Sales Amount').pack(side = LEFT)
Sales = Entry(f4_POS)
Sales.pack(fill = X,padx = 5,expand = TRUE)
Sales_Var = Sales.get()

f5_POS = Frame(POSView)
f5_POS.pack(fill=X)
Label(f5_POS,text = 'Current Date').pack(side = LEFT)
Label(f5_POS,text = time.strftime("%d/%m/%Y")).pack(side = LEFT, padx = 5)
Date_POS_Var = time.strftime("%d/%m/%Y")


f6_POS = Frame(POSView)
f6_POS.pack(fill = X)
B_POS_Submit = Button(f6_POS,text = 'Submit Sale', command = callback1).pack()



##f7_POS = Frame(POSView)
##f7_POS.pack(fill=BOTH,expand = TRUE)
##Label(f7_POS,image=photo).pack()

#f7_POS = Frame(POSView)
#f7_POS.pack(fill=X)
#Label(f7_POS, text = printerrors()).pack(side= LEFT)


#Report View
#Plotting works like this
# 1. Create a figure in a frame using f = Figure(figsize(5,5), dpi = 100)
# 2. Set the axes for the figures ax1 = f.add_subplot(111) for example
# 3. Plot the graph mentioning where you want the graph to be placed by
#    mentioning the correct axis

f1_RV = Frame(ReportView)
f1_RV.pack(fill=X)
Label(f1_RV,text = 'Report and Graphs').pack(padx = 10,pady=10)

f2_RV = Frame(ReportView)
f2_RV.pack(fill=BOTH, expand = TRUE)
f = Figure(figsize=(5,5), dpi=100)

create_df()
sales_overview()
sku_overview()


## commenting out the plots for now. Checking to see whether I can create the frame and two graphs by calling the function
## update_data() when pressing the button Refresh_data in f1_RV above.
#ax1 = f.add_subplot(211)
#ax3 = f.add_subplot(212)
#pd.options.display.mpl_style = 'default'
#daily_sales.plot(ax=ax1)
#pd.options.display.mpl_style = 'default'
#sku_sales.plot(kind = 'bar',stacked = True,ax = ax3)


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
f2_CRM.pack(fill = X)
Label(f2_CRM,text = 'Total Sales').pack(side = LEFT)
Label(f2_CRM,text = Modelv2.POS.totSales()).pack(side = LEFT,padx = 5)

f3_CRM = Frame(CRMView)
f3_CRM.pack(fill=X)
Label(f3_CRM,text = 'CC Sales').pack(side = LEFT)
Label(f3_CRM,text = Modelv2.POS.totCCsales()).pack(side = LEFT, padx = 5)

f4_CRM = Frame(CRMView)
f4_CRM.pack(fill=X)
Label(f4_CRM,text = 'Cash Sales').pack(side = LEFT)
Label(f4_CRM,text = Modelv2.POS.totCashSales()).pack(side = LEFT, padx = 5)


f5_CRM = Frame(CRMView)
f5_CRM.pack(fill = BOTH, expand = TRUE)
f1 = Figure(figsize = (5,5),dpi = 100)
ax2 = f1.add_subplot(111)
df5 = create_df()
df2 = df5.groupby('CustID')['Sales'].sum()
df3 = pd.DataFrame({'Name':df2.index, 'TotalSales':df2.values}).sort_values(['TotalSales'], ascending=False)
df3.plot(x = 'Name', y= 'TotalSales',kind = 'bar', ax = ax2)


canvas = FigureCanvasTkAgg(f1, f5_CRM)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2TkAgg(canvas, f5_CRM)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)


ani = animation.FuncAnimation(f, animate, interval=10000)

root.mainloop()

#C_ID.delete(0,END)
#SKU.delete(0,END)
#Sales.delete(0,END)
