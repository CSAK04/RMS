import mysql.connector
import tabulate

db = mysql.connector.connect(host = 'localhost', user='root',passwd='1234',auth_plugin = 'mysql_native_password')
#db = mysql.connector.connect(host = 'localhost', user='root',passwd='mes123@tirur')
#db = mysql.connector.connect(host = 'localhost', user='root',passwd='')
cursor = db.cursor(buffered=True)

cursor.execute('use rms')
#Make an Order
def new_order(MCODE,TABLE_NUMBER):
    cursor.execute('select ORDER_NO from orders')
    listOfOrderNumber = list()
    for tuple in cursor:
        for orderNo in tuple:
            listOfOrderNumber.append(orderNo)
    newOrderNumber = max(listOfOrderNumber) + 1
    cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
        (%s,%s,%s,%s)',(newOrderNumber,MCODE,TABLE_NUMBER,QUANTITY))

#Cancel an order
def cancel_order(ORDER_NUMBER):
    cursor.execute('Update orders set state="CANCELLED" where ORDER_NO = %s',(ORDER_NUMBER,))

#To view all orders of BillWindow table
def view_order_details(TABLE_NUMBER):
    cursor.execute('SELECT ORDER_NO,ITEM,COURSE,PRICE,DATE_TIME FROM ORDERS O,MENU M WHERE TABLE_NO = %s AND\
                    O.MCODE = M.MCODE',(TABLE_NUMBER,))
    if cursor.rowcount == 0:
        print('\nNo Orders Here')
    else:
        table = list()
        header = ['ORDER NUMBER','ITEM','COURSE','PRICE','DATE/TIME']
        for tuple in cursor:
            a = list(tuple)
            table.append(a)
        print(tabulate.tabulate(table,header,tablefmt="grid"))