import mysql.connector
#import employee as e
from ORDER import *
from MENU import *

def inputId():
    try:
        a = int(input('\nEMPLOYEE ID:'))
        return a
    except ValueError:
        print('INVALID FORMAT FOR AN ID\nTRY AGAIN')
        inputId()
        
def login():
    cursor.execute('select EID,PASS,DEPT from employee')
    
    id = inputId()
    passwd = input('PASSWORD:')
    
    for i in cursor:
        if i[0] == id:
            if i[1] == passwd:
                return 'Logged In'
            else:
                print('Incorrect PASSWORD\nTry Again')
                return 'Incorrect Password'
            break
    else:
        print('\nEnter a Valid ID')
        return 'Invalid Id'
    
db = mysql.connector.connect(host = 'localhost', user='root',passwd='1234',auth_plugin = 'mysql_native_password')
cursor = db.cursor(buffered= True)

#DATABASE CREATION
cursor.execute('create DATABASE IF NOT EXISTS rms')
cursor.execute('use rms')

#TABLE CREATION
cursor.execute('create table IF NOT EXISTS ORDERS(ORDER_NO int primary key,TABLE_NO INT(3),\
                            MCODE int(3),ORDER_STATE varchar(12) default "PREPARING",\
                            foreign key(MCODE) references MENU(MCODE))')

cursor.execute('create table IF NOT EXISTS MENU(MCODE int(3) primary key,ITEM varchar(50),\
                COURSE varchar(20),VEG varchar(3),PRICE int(5),\
                CONSTRAINT CHECK_VEG CHECK (VEG = "YES" OR VEG = "NO"))')

def order():
    table_number = input("Enter Table Number:")
    while True:
        opt = input('''\n1. for placing an order \n2. Cancel an order
3. View all orders
0. Back\nEnter your choice:''')
        if opt == '0':
            break
        if opt == '1':
            ans = 'y'
            view_items()
            while ans.lower() == 'y':
                MCODE = input('Enter MCODE:')
                new_order(MCODE=MCODE,TABLE_NUMBER=table_number)
                ans = input('Do you want to order more(y/n):')
                
        elif opt == '2':
            view_order_details(table_number)
            ORDER_NUMBER = input('ORDER_NUMBER:')
            cancel_order(ORDER_NUMBER=ORDER_NUMBER)
            
        elif opt == '3':
            view_order_details(table_number)


def verification():
    state = login()
    
    if state == 'Logged In':
        cursor.execute('select EID,ENAME,DEPT from employee')
        for i in cursor:
            if i[2] == 'WAITER':
                print('\nWELCOME ',i[1],'\n')
                order()
                
    elif state == 'Incorrect Password':
        verification()
        
    elif state == 'Invalid Id':
        print("An user with this ID doesn't exist\nPlease Try again later")
        verification()

verification()