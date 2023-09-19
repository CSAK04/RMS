import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',database='rms',\
                             passwd='1234',auth_plugin = 'mysql_native_password')

a = db.cursor()
d,c,f,e="ameer","ceo",23000,1


class update_emp():
    def rename_emp(EID):
        a.execute('update employee set ENAME = %s where EID = %s',(d,e))
        db.commit()

def add_emp(d,c,f):
    a.execute("insert into employee(ENAME,DEPARTMENT,salary) values(%s,%s,%s)",(d,c,f))
    db.commit()

def del_emp(EID):
    a.execute("delete from employee where EID = (%s)",(EID,))
    db.commit()
