#modeldb.py

import sqlite3

# 
conn = sqlite3.connect('pos.db')
c = conn.cursor()
c.execute('CREATE TABLE sales (SaleID INTEGER, CustID VARCHAR(9), CC BOOLEAN, SKU VARCHAR(9), SALES FLOAT(9), Day DATE) IF NOT EXISTS sales')
c.execute('CREATE TABLE items (SKU VARCHAR(9), SALES FLOAT(9), Day DATE) IF NOT EXISTS items')





# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()



cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()