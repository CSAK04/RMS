import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',database='rms',\
                             passwd='1234',auth_plugin = 'mysql_native_password')

a = db.cursor()
d,c,f,e="ameer","ceo",23000,1


class update_emp():
    def name(EID,NAME):
        a.execute('update employee set ENAME = %s where EID = %s',(NAME,EID))
        db.commit()
    def department(EID,DEPT):
        a.execute('update employee set DEPARTMENT = %s where EID = %s',(DEPT,EID))
        db.commit()
    def salary(EID,SALARY):
        a.execute('update employee set salary = %s where EID = %s',(SALARY,EID))
        db.commit()
    def EID(EID):
        a.execute('update employee set EID = %s where EID = %s',(EID,1))
        db.commit()
        

def add_emp(d,c,f):
    a.execute("insert into employee(ENAME,DEPARTMENT,salary) values(%s,%s,%s)",(d,c,f))
    db.commit()

def del_emp(EID):
    a.execute("delete from employee where EID = (%s)",(EID,))
    db.commit()
update_emp.EID(5)