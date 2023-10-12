import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',database='rms',\
                             passwd='1234',auth_plugin = 'mysql_native_password')

a = db.cursor()
d,c,f,e="ameer","ceo",23000,1


class update_emp():
    #To update Name of an Employee
    def name(EID,NAME):
        a.execute('update employee set ENAME = %s where EID = %s',(NAME,EID))
        db.commit()
    #To Change Department of an Employee
    def department(EID,DEPT):
        a.execute('update employee set DEPARTMENT = %s where EID = %s',(DEPT,EID))
        db.commit()
    #To change salary of an employee
    def salary(EID,SALARY):
        a.execute('update employee set salary = %s where EID = %s',(SALARY,EID))
        db.commit()
    #To change Employee ID of an employee
    def EID(current_EID,new_EID):
        a.execute('update employee set EID = %s where EID = %s',(new_EID,current_EID))
        db.commit()
    #To increase/decrease salary of an Employee
    '''to decrease add minus(-) sign before value'''
    def salaryinc(EID,sal):
        a.execute('update employee set salary = salary+%s where EID = %s',(sal,EID))
        db.commit()
        

def add_emp(d,c,f):
    a.execute("insert into employee(ENAME,DEPARTMENT,salary) values(%s,%s,%s)",(d,c,f))
    db.commit()

def del_emp(EID):
    a.execute("delete from employee where EID = (%s)",(EID,))
    db.commit()

def emp_details(EID):
    a.execute("select* from employee where EID = (%s)",(EID,))
    print(a.fetchall())
