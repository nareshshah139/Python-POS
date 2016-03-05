from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import time


##class POSApp(tk.Tk):
##
##    def __init__(self,*args,**kwargs):
##        tk.Tk.__init__(self,*args,**kwargs)
##        tk.Tk.wm_title(self,'POS Application Client')
##
root = Tk()
master = Frame(root, name = 'master')
master.pack(fill = BOTH)
root.title('Point of Sale System')
root.protocol('WM_DELETE_WINDOW',master.quit)
n = ttk.Notebook(master, name = 'n')

CC = IntVar()
Cash = IntVar()

def callback():
    print('Button Clicked')


##        f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
##        f2 = ttk.Frame(n)   # second page
##        n.add(f1, text='One')
##        n.add(f2, text='Two')
##        n.pack()
##
CustomerView = ttk.Frame(n)
SalesView = ttk.Frame(n)
POSView = ttk.Frame(n)
ReportView = ttk.Frame(n)
CRMView = ttk.Frame(n)
n.add(POSView, text = 'Pont of Sale System View')
n.add(SalesView, text = 'Sales View')
n.add(CustomerView,text = 'New Customer View')
n.add(ReportView, text = 'Report View')
n.add(CRMView, text = 'CRM View')
n.pack(fill = BOTH,expand = TRUE)


# Customer View Tab
f1_CV = Frame(CustomerView)
f1_CV.pack(fill = X)

Label(f1_CV,text = 'Customer Name').pack(side = LEFT)
C_Name = Entry(f1_CV)
C_Name.pack(fill = X,padx = 10, expand = TRUE)


f2_CV = Frame(CustomerView)
f2_CV.pack(fill = X)
Label(f2_CV,text = 'Customer ID').pack(side = LEFT)


f3_CV = Frame(CustomerView)
f3_CV.pack(fill = X)
B_Add_User = Button(f3_CV,text = 'Add User', command = callback).pack()

# POS View Tab
f1_POS = Frame(POSView)
f1_POS.pack(fill = X)
Label(f1_POS,text = 'Customer ID').pack(side = LEFT)
C_ID = Entry(f1_POS)
C_ID.pack(fill = X,padx = 5, expand = TRUE)


f2_POS = Frame(POSView)
f2_POS.pack(fill = X)
Label(f2_POS,text = 'Credit Card').pack(side = LEFT)
Checkbutton(f2_POS, text="CC", variable=CC).pack(side = LEFT,padx = 5)
Checkbutton(f2_POS, text='Cash',variable =Cash).pack(side = LEFT,padx = 5)

f3_POS = Frame(POSView)
f3_POS.pack(fill = X)
Label(f3_POS,text = 'SKU').pack(side = LEFT)
SKU = Entry(f3_POS)
SKU.pack(fill = X,padx = 5, expand = TRUE)

f4_POS = Frame(POSView)
f4_POS.pack(fill = X)
Label(f4_POS,text = 'Sales Amount').pack(side = LEFT)
Sales = Entry(f4_POS)
Sales.pack(fill = X,padx = 5,expand = TRUE)

f5_POS = Frame(POSView)
f5_POS.pack(fill=X)
Label(f5_POS,text = 'Current Date').pack(side = LEFT)
Label(f5_POS,text = time.strftime("%d/%m/%Y")).pack(side = LEFT, padx = 5)

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
f = Figure(figsize = (5,5),dpi = 100)
a = f.add_subplot(111)
a.plot([range(10)],[range(10)])

##graphArray = {'SalesID':[1,2,3,4,5,6,7,8,9,10],
##              'CustID':['123','124','125','122','123','124','125','122'],
##              'Name':['Chris','Chris','Lionel','Jonas','Fotis','Chris'
##                      'Chris','Lionel','Jonas','Fotis'],
##              'Payment':[

canvas = FigureCanvasTkAgg(f, f2_RV)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2TkAgg(canvas, f2_RV)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        
##class CustomerView(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
##
##        button1 = ttk.Button(self, text="Back to Home",
##                            command=lambda: controller.show_frame(StartPage))
##        button1.pack()
##
##        button2 = ttk.Button(self, text="Page Two",
##                            command=lambda: controller.show_frame(PageTwo))
##        button2.pack()
##        
##        
##class SalesView(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
##
##        button1 = ttk.Button(self, text="Back to Home",
##                            command=lambda: controller.show_frame(StartPage))
##        button1.pack()
##
##        button2 = ttk.Button(self, text="Page Two",
##                            command=lambda: controller.show_frame(PageTwo))
##        button2.pack()
##
##class POSView(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
##
##        button1 = ttk.Button(self, text="Back to Home",
##                            command=lambda: controller.show_frame(StartPage))
##        button1.pack()
##
##        button2 = ttk.Button(self, text="Page Two",
##                            command=lambda: controller.show_frame(PageTwo))
##        button2.pack()
##
##
##class SKUView(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
##
##        button1 = ttk.Button(self, text="Back to Home",
##                            command=lambda: controller.show_frame(StartPage))
##        button1.pack()
##
##        button2 = ttk.Button(self, text="Page One",
##                            command=lambda: controller.show_frame(PageOne))
##        button2.pack()
##
##
##class ReportView(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
##
##        button1 = ttk.Button(self, text="Back to Home",
##                            command=lambda: controller.show_frame(StartPage))
##        button1.pack()
##
##        f = Figure(figsize=(5,5), dpi=100)
##        a = f.add_subplot(111)
##        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
##
##        
##
##        canvas = FigureCanvasTkAgg(f, self)
##        canvas.show()
##        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
##
##        toolbar = NavigationToolbar2TkAgg(canvas, self)
##        toolbar.update()
##        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
##
