import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',database='rms',\
                             passwd='1234',auth_plugin = 'mysql_native_password')

cursor = db.cursor()
d,c,f,e="ameer","ceo",23000,1


class update_emp():
    #To update Name of an Employee
    def name(EID,NAME):
        cursor.execute('update employee set ENAME = %s where EID = %s',(NAME,EID))
        db.commit()
    #To Change Department of an Employee
    def department(EID,DEPT):
        cursor.execute('update employee set DEPARTMENT = %s where EID = %s',(DEPT,EID))
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
    for ID in range(1,100):
        if ID not in listOfEid:
            EID = ID
            break
    cursor.execute("insert into employee(EID,ENAME,USER,salary) values(%s,%s,%s,%s)",(EID,NAME,DEPT,sal))
    db.commit()

def del_emp(EID):
    cursor.execute("delete from employee where EID = (%s)",(EID,))
    db.commit()

def emp_details(EID):
    cursor.execute("select* from employee where EID = (%s)",(EID,))
    print(cursor.fetchall())

emp_details(1)