from tkinter import *
from tkinter import ttk
import mysql.connector

import customtkinter

a = Tk()
db = mysql.connector.connect(host='localhost', user='root', passwd='1234', auth_plugin='mysql_native_password')
#db = mysql.connector.connect(host='localhost', user='root', passwd='mes123@tirur')
#db = mysql.connector.connect(host='localhost', user='root', passwd='')
cursor = db.cursor(buffered=True)

cursor.execute('use rms')

cursor.execute('select ORDER_NO,TABLE_NO,ITEM,COURSE,VEG,PRICE,DATE_TIME from ORDERS natural join menu')
data = list()
for tuple in cursor:
    data.append(tuple)
frame = Frame(a, height=25)
frame.pack()

st = ttk.Style()
st.element_create("Custom.TreeHeading.border","from","default")
st.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky':'nswe'}),
    ("Custom.Treeheading.Border", {'sticky':'nswe', 'children':[
        ("Custom.Treeheading.padding", {'sticky':'nswe', 'children':[
            ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
            ("Custom.Treeheading.text", {'sticky':'nswe'})
        ]})
    ]})
])
st.configure("Treeview", background="#2FA572", foreground="gray98")
st.configure("Custom.Treeview.Heading", background="#2FA572", foreground="gray98", fieldBackground="red")
st.map("Custom.Treeview.Heading", relief = [('active','groove'),('pressed','flat')])

tableView = ttk.Treeview(frame, style="Custom.Treeview")
tableView['columns'] = ('ORDER_NO','TABLE_NO','ITEM','COURSE','VEG','PRICE','DATE_TIME')
tableView.column('#0', width=0, stretch=NO)
tableView.column('ORDER_NO', anchor=CENTER, width=80)
tableView.column('TABLE_NO', anchor=CENTER, width=80)
tableView.column('ITEM', anchor=CENTER, width=80)
tableView.column('COURSE', anchor=CENTER, width=80)
tableView.column('VEG', anchor=CENTER, width=80)
tableView.column('PRICE', anchor=CENTER, width=80)
tableView.column('DATE_TIME', anchor=CENTER, width=80)

tableView.heading("#0",text="")
tableView.heading('ORDER_NO', anchor=CENTER, text='ORDER_NO')
tableView.heading('TABLE_NO', anchor=CENTER, text='TABLE_NO')
tableView.heading('ITEM', anchor=CENTER, text='ITEM')
tableView.heading('COURSE', anchor=CENTER, text='COURSE')
tableView.heading('VEG', anchor=CENTER, text='VEG')
tableView.heading('PRICE', anchor=CENTER, text='PRICE')
tableView.heading('DATE_TIME', anchor=CENTER, text='DATE_TIME')

for i in range(len(data)):
    tableView.insert(parent='', index='end', iid=i, text='', values=data[i])

print(tableView.get_children())
tableView.pack()
a.mainloop()