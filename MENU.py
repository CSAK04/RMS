import mysql.connector 

db = mysql.connector.connect(host = 'localhost', user='root',\
                             passwd='1234',\
                             auth_plugin = 'mysql_native_password')

cursor = db.cursor()

#DATABASE CREATION
'''cursor.execute('create database rms')'''
cursor.execute('use rms')

#TABLE CREATION
'''cursor.execute('create table MENU(MCODE int(3) primary key,ITEM varchar(50),\
                COURSE varchar(20),VEG varchar(3),PRICE int(5),\
                CONSTRAINT CHECK_VEG CHECK (VEG = "YES" OR VEG = "NO"))')'''

#INSERTING VALUES TO MENU TABLE
'''cursor.execute("insert into menu values (101,'BUFFALO CHICKEN MEATBALLS','APPETIZER','NO',199),\
(102,'JALAPENO POPPERS','APPETIZER','YES',189),\
(103,'GOAT CHEESE MUSHROOMS','APPETIZER','NO',349),\
(104,'CHICKEN POCKETS','APPETIZER','NO',329),\
(105,'YOGURT FRUIT CUPS','APPETIZER','YES',199),\
(201,'LASAGNA','MAIN','NO',599),(202,'CHICKEN BIRIYANI','MAIN','NO',449),\
(203,'TEMPURA','MAIN','YES',429),(204,'PULAO','MAIN','YES',449),\
(205,'SUSHI','MAIN','NO',499),(206,'CHICKEN KEBAB','MAIN','NO',599),\
(301,'TIRAMISU','DESSERT','YES',299),(302,'CREME BRULEE','DESSERT','YES',399),\
(303,'BAKLAVA','DESSERT','YES',249),(304,'GULAB JAMUN','DESSERT','YES',199),\
(305,'CHURROS','DESSERT','YES',299),(401,'MOJITO','BEVERAGE','YES',99),\
(402,'CINNAMON TEA','BEVERAGE','YES',79),(403,'COFFEE','BEVERAGE','YES',99)")
db.commit()'''

#Add to Menu
def add_item(ITEM,COURSE,VEG,PRICE):
    courses = ['APPETIZER','MAIN','DESSERT','BEVERAGE']
    for i in range(len(courses)):
        if courses[i] == COURSE:
            break
    i+=1
    cursor.execute('select * from menu where COURSE = %s',(COURSE,))
    l = list(cursor)
    MCODE = i*100+len(l)+1
    cursor.execute('insert into menu values(%s,%s,%s,%s,%s)',(MCODE,ITEM,COURSE,VEG,PRICE))
    db.commit()

#Remove from Menu
def remove_item(MCODE):
    cursor.execute('delete from menu where MCODE = %s',(MCODE,))
    db.commit()

#Update Menu
def update_item(MCODE,FIELD_NAME):
    if FIELD_NAME == 'ITEM':
        ITEM = input('Enter the corrected item name:')
        cursor.execute('update menu set ITEM = %s where MCODE = %s',(ITEM,MCODE))
        db.commit()

    elif FIELD_NAME == 'COURSE':
        course = input('Enter the corrected course:')
        cursor.execute('update menu set COURSE = %s where MCODE = %s',(course,MCODE))
        db.commit()
        
     
