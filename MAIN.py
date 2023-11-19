import mysql.connector
import employee
import ORDER
import MENU

def MANAGER():
    while True:
        MANAGER_choice = int(input('\n1:EMPLOYEE\n2:MENU\n3:Order History\n0:Log out\nEnter your Choice:'))
        if MANAGER_choice == 1:
            while True:
                opt = input('''\n1: Recruit Employee \n2: Dismiss Employee
3: Edit Employee Details\n4: View Employee Details
0: Back\nEnter your choice:''')
                if opt == '1':
                    print('\nRecruit Employee')
                    name = input('NAME:')
                    dept = input('DEPARTMENT:')
                    sal = input('SALARY:')
                    employee.add_emp(name.upper(), dept.upper(),sal)
                elif opt == '2':
                    eid = input('EID:')
                    employee.del_emp(eid)
                elif opt == '3':
                    editChoice = input('\n1:NAME\n2:DEPARTMENT\n3:SALARY\n4:EID\n0:BACK\nENTER YOUR CHOICE:')
                    if editChoice == '1':
                        eid = input('EMPLOYEE ID:')
                        name = input('NEW NAME:')
                        employee.update_emp.name(EID=eid,NAME=name.upper())
                    elif editChoice == '2':
                        eid = input('EMPLOYEE ID:')
                        dept = input('NEW DEPARTMENT:')
                        employee.update_emp.department(eid,dept.upper())
                    elif editChoice == '3':
                        eid = input('EMPLOYEE ID:')
                        sal = input('NEW SALARY:')
                        employee.update_emp.salary(eid,sal)
                elif opt == '4':
                    eid = input('EID:')
                    employee.emp_details(eid)
                elif opt == '0':
                    break

        elif MANAGER_choice == 2:
            while True:
                opt = input('''\n1: Add Item \n2: Remove Item
3: Edit Item Details\n4: View Item Details
0: Back\nEnter your choice:''')
                if opt == '1':
                    print("\nAdd Item")
                    name = input('Item Name:')
                    course = input('Course:')
                    veg = input('Is Item Vegetarian(Yes/No):')
                    price = input('Price:')
                    MENU.add_item(ITEM=name.upper(),COURSE=course.upper(),VEG=veg.upper(),PRICE=price)
                elif opt == '2':
                    mcode = input("Enter MCODE:")
                    MENU.remove_item(mcode)
                elif opt == '3':
                    editChoice = input('\n1:NAME\n2:COURSE\n3:PRICE\n4:VEG\n0:BACK\nENTER YOUR CHOICE:')
                    mcode = input("Enter MCODE:")
                    if editChoice == '1':
                        MENU.update_item(mcode, 'ITEM')
                    elif editChoice == '2':
                        MENU.update_item(mcode, 'COURSE')
                    elif editChoice == '3':
                        MENU.update_item(mcode, 'PRICE')
                    elif editChoice == '4':
                        MENU.update_item(mcode, 'VEG')
                elif opt == '4':
                    MENU.view_items()
                elif opt == '0':
                    break

        elif MANAGER_choice == 3:
            table_number = input("Enter Table Number:")
            ORDER.view_order_details(table_number)

        elif MANAGER_choice == 0:
            print('Logged Out\n')
            break


def WAITER():
    EMPLOYEE_choice = int(input('1:Choose Table\n2:Log Out\nEnter your Choice:'))
    if EMPLOYEE_choice == 1:
        order()         
    elif EMPLOYEE_choice == 2:
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
#db = mysql.connector.connect(host = 'localhost', user='root',passwd='mes123@tirur')
#db = mysql.connector.connect(host = 'localhost', user='root',passwd='')
cursor = db.cursor(buffered=True)

#DATABASE CREATION
#cursor.execute('create DATABASE IF NOT EXISTS rms')
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

while True:
    print("Welcome to rms")
    root_input = int(input("1.Log In\n0.Exit\nEnter your Choice:"))
    if root_input == 1:
        verification()
    elif root_input == 0:
        break
