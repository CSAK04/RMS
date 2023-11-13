import mysql.connector
import employee
import ORDER
import MENU

def MANAGER():
    ch = int(input('1:EMPLOYEE\n2:MENU\n3:Order History\n0:Log out\nEnter your Choice:'))
    if ch == 1:
        while True:
            opt = input('''\n1: Recruit Employee \n2: Dismiss Employee
3: Edit Employee Details\n4: View Employee Details
5: Back\nEnter your choice:''')
            if opt == '1':
                name = input('NAME:')
                dept = input('DEPARTMENT:')
                sal = input('SALARY:')
                employee.add_emp(name,dept,sal)
            elif opt == '2':
                eid = input('EID:')
                employee.del_emp(eid)
            elif opt == '3':
                editChoice = input('1:NAME\n2:DEPARTMENT\n3:SALARY\n4:EID\nENTER YOUR CHOICE:')
                if editChoice == '1':
                    eid = input('EMPLOYEE ID:')
                    name = input('NEW NAME:')
                    employee.update_emp.name(EID=eid,NAME=name)
            elif opt == '4':
                eid = input('EID:')
                employee.emp_details(eid)
            elif opt == '5':
                MANAGER()
    if ch == 1:
        pass
    if ch == 1:
        pass
    if ch == 1:
        print('Logged Out')
        verification()


def WAITER():
    ch = int(input('1:Choose Table\n2:Log Out\nEnter your Choice:'))
    if ch == 1:
        order()         
    elif ch == 2:
        print('Logged Out\n')
        verification()
    
def inputId():
    try:
        a = int(input('EMPLOYEE ID:'))
        return a
    except ValueError:
        print('INVALID FORMAT FOR AN ID\nTRY AGAIN')
        inputId()
        
def login():
    global id
    cursor.execute('select EID,PASS,DEPT from employee')
    print("\nEnter Login Credentials")
    id = inputId()
    passwd = input('PASSWORD:')
    
    for i in cursor:
        if i[0] == id:
            if i[1] == passwd:
                return 'Logged In'
            else:
                print('\nIncorrect PASSWORD\nTry Again')
                return 'Incorrect Password'
            break
    else:
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
        table_number = input("\nEnter Table Number:")
        while True:
            opt = input('''\n1. for placing an order \n2. Cancel an order
3. View all orders
4. Back\nEnter your choice:''')
            
            if opt == '4':
                order()
            if opt == '1':
                ans = 'y'
                MENU.view_items()
                while ans.lower() == 'y':
                    MCODE = input('Enter MCODE:')
                    ORDER.new_order(MCODE=MCODE,TABLE_NUMBER=table_number)
                    ans = input('Do you want to order more(y/n):')
                
            elif opt == '2':
                ORDER.view_order_details(table_number)
                ORDER_NUMBER = input('ORDER_NUMBER:')
                ORDER.cancel_order(ORDER_NUMBER=ORDER_NUMBER)
            
            elif opt == '3':
                ORDER.view_order_details(table_number)


def verification():
    state = login()
    ID = str(id)
    if state == 'Logged In':
        cursor.execute('select EID,ENAME,DEPT from employee WHERE EID=%s',(ID,))
        for i in cursor:
            if i[2] == 'WAITER':
                print('\nWELCOME ',i[1],'\n\nLogged In')
                WAITER()
            elif i[2] == 'MANAGER':
                MANAGER()
                
    elif state == 'Incorrect Password':
        verification()
        
    elif state == 'Invalid Id':
        print("\nAn user with this ID doesn't exist\nPlease Try again later")
        verification()

verification()
