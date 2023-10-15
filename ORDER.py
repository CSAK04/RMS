import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',\
                             passwd='1234',\
                             auth_plugin = 'mysql_native_password')

cursor = db.cursor()

#DATABASE CREATION
'''cursor.execute('create database rms')'''
cursor.execute('use rms')

#TABLE CREATION
'''cursor.execute('create table ORDERS(ORDER_NO int primary key,TABLE_NO INT(3),\
                            MCODE int(3),ORDER_STATE varchar(12) default "PREPARING",\
                            foreign key(MCODE) references MENU(MCODE))')
'''



#Make an Order
def new_order(MCODE,TABLE_NUMBER):
    cursor.execute('select ORDER_NO from orders')
    listOfOrderNumber = list()
    for tuple in cursor:
        for orderNo in tuple:
            listOfOrderNumber.append(orderNo)
    newOrderNumber = max(listOfOrderNumber) + 1
    cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO) VALUES\
        (%s,%s,%s)',(newOrderNumber,MCODE,TABLE_NUMBER))
    db.commit()

#Cancel an order
def cancel_order(ORDER_NUMBER):
    cursor.execute('Update orders set state="CANCELLED" where ORDER_NO = %s',(ORDER_NUMBER,))
    db.commit()    

#To view all orders of a table
def view_order_details(TABLE_NUMBER):
    cursor.execute('SELECT ITEM,COURSE,PRICE,STATE FROM ORDERS O,MENU M WHERE TABLE_NO = %s AND\
                    O.MCODE = M.MCODE',(TABLE_NUMBER,))
    for tuple in cursor:
        for item in tuple:
            print(item,end=' ')
        print()