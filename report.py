
import sqlite3
import pandas as pd
import matplotlib as plt
plt.style.use('ggplot')
import numpy as np
import os

#get table from SQL once DB is set up to build the tables and graphs below
#Probably need to fix the sql query
def load_data_sql():
    connection = sqlite3.connect("pos.db")
    df = pd.read_sql_query("SELECT * FROM sales, customer LEFT JOIN sales.custid, customer.custid",connection)
    return(df)
load_data_sql()

#test array
transaction_data = {'SalesID': [1,2,3,4,5,6,7,8,9,10],
'CustID':['123','123','124','125','122','123','123','124','125','122'],
'Name':['Chris','Chris','Lionel','Jonas','Fotis','Chris','Chris','Lionel','Jonas','Fotis'],
'Payment':[1,0,1,0,1,0,0,1,1,0],
'SKU':['123456789','123456788','123456788','123456787','123456784','123456789','123456788','123456788','123456787','123456784'],
'Sales':[20,30,30,40,20,20,30,30,40,30],
'Date': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04','2015-01-05', '2015-01-05', '2015-01-06', '2015-01-07','2015-01-08', '2015-01-09']}



#create df from .csv files and insert into sales, customer and sku table
def write_data_sql():
    connection = sqlit3.connect("pos.db")
    sales_table = pd.DataFrame.from_csv(os.getcwd()+"/sales.csv",sep=";",header=0)
    customer_table = pd.DataFrame.from_csv(os.getcwd()+"/sales.csv",sep=";",header=0) #specify path
    sku_table = pd.DataFrame.from_csv(os.getcwd()+"/sales.csv",sep=";",header=0) #specify path
    sales_table.to_sql("sales", connection)
    customer_table.to_sql("customer", connection)
    sku_table.to_sql("sku", connection)
write_data_sql()

# Create pandas dataframe from graph array with additional variable creation
def create_df():
    global df
    df = pd.DataFrame(transaction_data)
    df['CC'] = df['Payment']==1
    df['Cash'] = df['Payment']==0
    df['CCSales'] = df.Sales*df.CC
    df['CashSales']=df.Sales*df.Cash
create_df()

#Top Customer Table
#Group dataframe by CustID and take sum of sales
def top_customers():
    df_sales = df[['CustID','Name','Sales']].groupby(['CustID','Name']).agg([np.sum, np.count_nonzero])
    df_sales.columns = ['SalesAmount','ItemCount']
    # Sort by sum of sales in descending order
    df_sales = df_sales.sort_values(['SalesAmount'], ascending=False)
    return(df_sales.head(10))


#Top SKU Table
def top_sku():
    df_topSKU = df[['SKU','Sales']].groupby(['SKU']).agg([np.sum, np.count_nonzero])
    df_topSKU.columns=['SalesAmount','SalesCount']
    df_topSKU_sort = df_topSKU.sort_values(['SalesAmount'], ascending=False)
    return(df_topSKU_sort.head(10))

#PLOTTING
#Create Sales by Day Table
def sales_overview():
    global daily_sales
    daily_sales = df[['Date','Sales','CCSales','CashSales']].groupby(['Day']).agg([np.sum])
    daily_sales.columns = ['TotalSales','CCSales','CashSales']

#create plot
def sales_plot():
    global plot1
    plot1 = daily_sales.plot(title="Sales by Payment Method", xticks=df['Day'],lw=2,colormap='gnuplot',marker='.',markersize=10)
    plot1.set(xlabel="Date", ylabel="Sales Amount")
    return plot1

#Create Sales by SKU Table
def sku_overview():
    global sku_sales
    sku_sales = df[['SKU','Sales']].groupby(['SKU']).agg([np.sum])
    sku_sales.columns = ['Amount']
    sku_sales = sort_values(['Amount'], ascending=False)
    return(sku_sales)


create_df()
top_customers()
top_sku()
sales_overview()
sales_plot()
sku_overview()
