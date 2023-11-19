import mysql.connector
import customtkinter
from tkinter import *

db = mysql.connector.connect(host='localhost', user='root', passwd='1234', auth_plugin='mysql_native_password')
# db = mysql.connector.connect(host = 'localhost', user='root',passwd='mes123@tirur')
# db = mysql.connector.connect(host = 'localhost', user='root',passwd='')
cursor = db.cursor(buffered=True)
cursor.execute('use rms')

cursor.execute('SELECT ORDER_NO,ITEM,COURSE,PRICE,DATE_TIME FROM ORDERS O,MENU M WHERE O.MCODE = M.MCODE')
if cursor.rowcount == 0:
    print('\nNo Orders Here')
else:
    table = list()
    header = ['ORDER NUMBER','ITEM','COURSE','PRICE','DATE/TIME']
    for tuple in cursor:
        a = list(tuple)
        table.append(a)

def ui():
    print(entryList)
    for i in entryList:
        for j in i:
            print(j[0].get())
        print()

customtkinter.set_appearance_mode('dark')
a = customtkinter.CTk()
print(table)
total_rows = len(table)
total_columns = len(table[0])
entryList = list()

for i in range(5):
    e = customtkinter.CTkEntry(a, width=200,
                               font=('Arial', 16, 'bold'), corner_radius=0)
    e.grid(row=0, column=i)
    e.insert(END, header[i])
    e.configure(state=DISABLED)

for i in range(total_rows):
    rowList = list()
    for j in range(total_columns):
        e = customtkinter.CTkEntry(a, width=200,
                       font=('Arial', 16, 'bold'),corner_radius=0)

        e.grid(row=i+1, column=j)
        e.insert(END, table[i][j])
        rowList.append([e, i, j])
        if j == 2 or j == 0:
            e.configure(state=DISABLED)
    entryList.append(rowList)
c = customtkinter.CTkButton(a, text='submit', command=lambda: ui())
c.grid(row=total_rows+2)

a.mainloop()