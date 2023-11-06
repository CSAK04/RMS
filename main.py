import mysql.connector
#import employee as e
from ORDER import *
from MENU import *

def login():
    id = input('EMPLOYEE ID:')
    passwd = input('PASSWORD:')
    
    for i in cursor:
        print(i)
        if i[0] == int(id):
            if i[1] == passwd:
                print('Logged In')
                return
            else:
                print('Incorrect PASSWORD\nTry Again')
                login()
            break
    else:
        print('Enter a Valid ID')
        login()
    
db = mysql.connector.connect(host = 'localhost', user='root',\
                             passwd='1234',\
                             auth_plugin = 'mysql_native_password'
                             )

cursor = db.cursor()
cursor.execute('use rms')
cursor.execute('select EID,PASS from employee')


while True:

    opt = input('''1. for placing an order \n2. For cancelling an order
3.To view all orders
Enter your choice:''')
    if opt == '1':
        ans = 'y'
        table_number = input("Enter Table Number:")
        view_items()
        while ans == 'y':
            MCODE = input('Enter MCODE:')
            ans = input('Do you want to order more(y/n):')
            new_order(MCODE=MCODE,TABLE_NUMBER=table_number)
            
    elif opt == '2':
        table_number = input("Enter Table Number:")
        ORDER_NUMBER = input('ORDER_NUMBER:')
        cancel_order(ORDER_NUMBER=ORDER_NUMBER)
    elif opt == '3':
        table_number = input("Enter Table Number:")
        view_order_details(table_number)    

