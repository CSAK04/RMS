import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',passwd='1234',auth_plugin = 'mysql_native_password')
#db = mysql.connector.connect(host = 'localhost', user='root',passwd='mes123@tirur')
#db = mysql.connector.connect(host = 'localhost', user='root',passwd='')

cursor = db.cursor()
cursor.execute('create DATABASE IF NOT EXISTS rms')
cursor.execute('use rms')
cursor.execute('create table IF NOT EXISTS employee(EID int primary key,ENAME varchar(50),DEPT varchar(50),SALARY int,PASS varchar(8) DEFAULT "0",DOJ DATE DEFAULT (DATE_FORMAT(NOW(), "%Y-%m-%d")))')
try:
    cursor.execute('insert into employee(EID,ENAME,DEPT,SALARY,PASS) values(1,"AMAN","MANAGER",4569,"1234"),\
                   (2,"IBADH","WAITER",346474654,"0")')
    db.commit()
except:
    pass

class update_emp():
    #To update Name of an Employee
    def name(EID,NAME):
        cursor.execute('update employee set ENAME = %s where EID = %s',(NAME,EID))
        db.commit()
    #To Change Department of an Employee
    def department(EID,DEPT):
        cursor.execute('update employee set DEPT = %s where EID = %s',(DEPT,EID))
        db.commit()
    #To change salary of an employee
    def salary(EID,SALARY):
        cursor.execute('update employee set salary = %s where EID = %s',(SALARY,EID))
        db.commit()
    #To change Employee ID of an employee
    def EID(current_EID,new_EID):
        cursor.execute('update employee set EID = %s where EID = %s',(new_EID,current_EID))
        db.commit()
    #To increase/decrease salary of an Employee
    '''to decrease add minus(-) sign before value'''
    def salaryinc(EID,sal):
        cursor.execute('update employee set salary = salary+%s where EID = %s',(sal,EID))
        db.commit()
        

def add_emp(NAME,DEPT,sal):
    
    listOfEid = list()
    cursor.execute('select EID from employee')
    for record in cursor:
        for EID in record:
            listOfEid.append(EID)
    for ID in range(1,10000):
        if ID not in listOfEid:
            EID = ID
            break
    cursor.execute("insert into employee(EID,ENAME,DEPT,salary) values(%s,%s,%s,%s)",(EID,NAME,DEPT,sal))
    db.commit()

def del_emp(EID):
    cursor.execute("delete from employee where EID = (%s)",(EID,))
    db.commit()

def emp_details(EID):
    cursor.execute("select* from employee where EID = (%s)",(EID,))
    if cursor.rowcount == -1:
        print("No employee with this EID")
    else:
        for tuple in cursor:
            print('EID       :',tuple[0],'\nENAME     :',tuple[1],'\nDEPARTMENT:',tuple[2],'\nSALARY    :',
                  tuple[3],'\nPASSWORD  :',tuple[4])
