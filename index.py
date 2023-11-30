from tkinter import *
from tkinter import ttk
import CTkMessagebox
import customtkinter
from PIL import Image,ImageTk
import mysql.connector


class MENU:
    def add_item(ITEM, COURSE, VEG, PRICE):
        for i in range(len(courses)):
            if courses[i] == COURSE:
                break
        i += 1
        cursor.execute('select * from menu where COURSE = %s', (COURSE,))
        l = list(cursor)
        MCODE = i * 100 + len(l) + 1
        cursor.execute('insert into menu(MCODE,ITEM,COURSE,VEG,PRICE) values(%s,%s,%s,%s,%s)',
                       (MCODE, ITEM, COURSE, VEG, PRICE))
        db.commit()

    # Remove from Menu
    def remove_item(MCODE):
        cursor.execute('delete from menu where MCODE = %s', (MCODE,))
        db.commit()


class employee:
    def add_emp(NAME, DEPT, sal):
        listOfEid = list()
        cursor.execute('select EID from employee')
        for record in cursor:
            for EID in record:
                listOfEid.append(EID)
        for ID in range(1, 10000):
            if ID not in listOfEid:
                EID = ID
                break
        cursor.execute("insert into employee(EID,ENAME,DEPT,salary) values(%s,%s,%s,%s)", (EID, NAME, DEPT, sal))
        db.commit()

    def del_emp(EID):
        cursor.execute("delete from employee where EID = (%s)", (EID,))
        db.commit()
        
def QUIT():
    ans = CTkMessagebox.CTkMessagebox(title='rms', message='Do you want to Quit', icon='question', option_1="Ok", option_2="Cancel")
    if ans.get() == "Ok":
        a.destroy()

def Emp_Update(item):
    if item == "ADD":
        a.unbind('<Return>')
        ENAME = Name_Entry.get()
        DEPT = DeptOptionMenu.get()
        print(DEPT)
        SAL = Sal_Entry.get()
        if DEPT == 'DEPARTMENT':
            CTkMessagebox.CTkMessagebox(title='RMS', message='Choose BillWindow Department')
            a.bind('<Return>', lambda event: Emp_Update("ADD"))
        else:
            employee.add_emp(NAME=ENAME, DEPT=DEPT, sal=SAL)
            EMPLOYEE()
            CTkMessagebox.CTkMessagebox(title="RMS", message="Employee Recruited Successfully")
    elif item == "REMOVE":
        if entered_pass == Pass_Entry.get():
            a.unbind('<Return>')
            EID = Id_Entry.get()
            employee.del_emp(EID=EID)
            EMPLOYEE()
            CTkMessagebox.CTkMessagebox(message="Employee Dismissed Successfully", title="RMS")
        else:
            CTkMessagebox.CTkMessagebox(message="Wrong Password Entered",title="RMS")
    elif item == 'employee':
        EID = Id_OptionMenu.get()
        ENAME = Name_Entry.get()
        DEPT = DeptOptionMenu.get()
        SAL = Sal_Entry.get()
        Pass = Pass_Entry.get()

        cursor.execute('select ENAME,DEPT,salary,PASS from employee where EID = %s', (EID,))
        data = cursor.fetchone()
        print(data)
        if ENAME == '':
            pass
        elif data[0][0] != ENAME:
            cursor.execute('update employee set ENAME = %s where EID = %s', (ENAME.upper(), EID))
            db.commit()

        if data[0][1] != DEPT:
            cursor.execute('update employee set DEPT = %s where EID = %s', (DEPT.upper(), EID))
            db.commit()

        if SAL == '':
            pass
        elif data[0][2] != SAL:
            cursor.execute('update employee set salary = %s where EID = %s', (SAL, EID))
            db.commit()

        if Pass == '':
            pass
        elif data[0][3] != Pass:
            cursor.execute('update employee set PASS = %s where EID = %s', (Pass, EID))
            db.commit()

        CTkMessagebox.CTkMessagebox(message="Employee Details Updated Successfully", title="RMS")

def Add_employee():
    Name_Entry.delete(0, END)
    Sal_Entry.delete(0, END)
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Edit_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()

    MainLabel.configure(text='EMPLOYEE RECRUITMENT')
    Name_Entry.configure(placeholder_text='EMPLOYEE NAME')
    DeptOptionMenu.set('DEPARTMENT')
    #Dept_Entry.configure(placeholder_text='DEPARTMENT')
    Sal_Entry.configure(placeholder_text='SALARY')
    submit_btn.configure(text='SAVE', command=lambda: Emp_Update("ADD"))
    Left_arrow_btn.configure(command=lambda: EMPLOYEE())

    Name_Entry.place(relx=0.5, rely=0.45, anchor='center')
    DeptOptionMenu.place(relx=0.5, rely=0.58, anchor='center')
    #Dept_Entry.place(relx=0.5, rely=0.58, anchor='center')
    Sal_Entry.place(relx=0.5, rely=0.71, anchor='center')
    MainLabel.place(relx=0.5, rely=0.2, anchor='center')
    submit_btn.place(relx=0.8, rely=0.87)

    a.bind('<Return>', lambda event: Emp_Update("ADD"))

def Dismiss_employee():
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Edit_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Id_Entry.delete(0, END)
    Pass_Entry.delete(0, END)

    Left_arrow_btn.configure(command=lambda: EMPLOYEE())
    Id_Entry.configure(placeholder_text='EMPLOYEE ID')
    Pass_Entry.configure(placeholder_text='YOUR PASSWORD')
    submit_btn.configure(text='SAVE', command=lambda: Emp_Update("REMOVE"))
    MainLabel.configure(text='EMPLOYEE DISMISSAL')

    Id_Entry.place(relx=0.5, rely=0.4, anchor='center')
    Pass_Entry.place(relx=0.5, rely=0.52, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')
    submit_btn.place(relx=0.8, rely=0.87)

    a.bind('<Return>', lambda event: Emp_Update("REMOVE"))

'''def Info_employee():
    global entryList
    Add_Employee_btn.place_forget()
    Edit_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()

    Left_arrow_btn.configure(command=lambda: EMPLOYEE())
    submit_btn.configure(text='SAVE', command=lambda: Emp_Update())

    Info_Employee_Frame.place(relx=0.02, rely=0.15)
    cursor.execute('SELECT EID,ENAME,DEPT,salary,DOJ,PASS FROM employee')
    table = list()
    header = ['EID', 'NAME', 'DEPARTMENT', 'SALARY', 'DOJ', 'PASS']
    for tuple in cursor:
        empList = list(tuple)
        table.append(empList)
    total_rows = len(table)
    total_columns = len(table[0])
    entryList = list()
    for i in range(len(header)):
        e = customtkinter.CTkEntry(Info_Employee_Frame, width=160, font=('Arial', 16, 'bold'), corner_radius=0)
        e.grid(row=0, column=i)
        e.insert(END, header[i])
        e.configure(state=DISABLED)
    for i in range(total_rows):
        rowList = list()
        for j in range(total_columns):
            e = customtkinter.CTkEntry(Info_Employee_Frame, width=160, font=('Arial', 16, 'bold'), corner_radius=0)

            e.grid(row=i + 1, column=j)
            e.insert(END, table[i][j])
            rowList.append([e, i, j])
            if j in [0, 4]:
                e.configure(state=DISABLED)
        entryList.append(rowList)

    submit_btn.place(relx=0.8, rely=0.87)
    BillWindow.bind('<Return>', lambda: Emp_Update())'''

def Id_Menu(ID):
    Pass_Entry.configure(placeholder_text='PASSWORD')
    print(ID)
    for list in data:
        if int(ID) == list[0]:
            id = list[0]
            name = list[1]
            dept = list[2]
            sal = list[3]
            doj = list[4]
            passwd = list[5]
    Name_Entry.configure(state=NORMAL, placeholder_text=name)
    DeptOptionMenu.configure(state=NORMAL)
    DeptOptionMenu.set(dept)
    Sal_Entry.configure(state=NORMAL, placeholder_text=sal)
    DOJ_Entry.configure(state=NORMAL, placeholder_text=doj)
    Pass_Entry.configure(show='', state=NORMAL, placeholder_text=passwd)
    submit_btn.configure(command=lambda: Emp_Update('employee'), text='SAVE')

    submit_btn.place(relx=0.8, rely=0.87)

def Edit_Employee():
    global data
    Pass_Entry.delete(0, END)
    Name_Entry.delete(0, END)
    DOJ_Entry.delete(0, END)
    Sal_Entry.delete(0, END)
    Add_Employee_btn.place_forget()
    Edit_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()

    data = []
    Id_list = []
    cursor.execute('SELECT EID,ENAME,DEPT,salary,DOJ,PASS FROM employee')
    for tuple in cursor:
        data.append(list(tuple))
    for list1 in data:
        Id_list.append(str(list1[0]))

    Id_OptionMenu.configure(values=Id_list, command=Id_Menu)
    Id_OptionMenu.set("Employee ID")
    DeptOptionMenu.set("DEPARTMENT")
    Name_Entry.configure(placeholder_text='EMPLOYEE NAME')
    Name_Entry.configure(state=DISABLED)
    DeptOptionMenu.configure(state=DISABLED)
    Sal_Entry.configure(placeholder_text='SALARY')
    Sal_Entry.configure(state=DISABLED)
    DOJ_Entry.configure(placeholder_text='DOJ')
    DOJ_Entry.configure(state=DISABLED)
    Pass_Entry.configure(show='', placeholder_text="PASSWORD")
    Pass_Entry.configure(state=DISABLED)
    Left_arrow_btn.configure(command=lambda: EMPLOYEE())
    MainLabel.configure(text='EDIT EMPLOYEE INFO')

    Id_OptionMenu.place(relx=0.5, rely=0.3, anchor='center')
    Name_Entry.place(relx=0.5, rely=0.4, anchor='center')
    DeptOptionMenu.place(relx=0.5, rely=0.5, anchor='center')
    Sal_Entry.place(relx=0.5, rely=0.6, anchor='center')
    DOJ_Entry.place(relx=0.5, rely=0.7, anchor='center')
    Pass_Entry.place(relx=0.5, rely=0.8, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')

#############
#################
#Make the position of buttons correct in employee
#################
#############
def EMPLOYEE():
    Id_Entry.place_forget()
    Pass_Entry.place_forget()
    MainLabel.place_forget()
    Name_Entry.place_forget()
    Dept_Entry.place_forget()
    Sal_Entry.place_forget()
    Menu_btn.place_forget()
    Employee_btn.place_forget()
    Order_history_btn.place_forget()
    Info_Employee_Frame.place_forget()
    submit_btn.place_forget()
    LogOut_btn.place_forget()
    Id_OptionMenu.place_forget()
    DeptOptionMenu.place_forget()
    DOJ_Entry.place_forget()

    Left_arrow_btn.configure(command=lambda: MANAGER())
    Info_Employee_btn.configure(command=lambda: Edit_Employee())
    Pass_Entry.configure(state=NORMAL)
    Name_Entry.configure(state=NORMAL)
    DeptOptionMenu.configure(state=NORMAL)
    Sal_Entry.configure(state=NORMAL)

    Add_Employee_btn.place(relx=0.25, rely=0.5, anchor='center')
    Dismiss_Employee_btn.place(relx=0.65, rely=0.5, anchor='center')
    Info_Employee_btn.place(relx=0.45, rely=0.5, anchor='center')
    Left_arrow_btn.place(relx=0.025, rely=0.03)

def MenuUpdate(item):
    if item == 'ADD':
        Dish = Name_Entry.get()
        course = CoursesOptionMenu.get()
        Veg = VegOptionMenu.get()
        Price = Sal_Entry.get()
        MENU.add_item(Dish,course,Veg,Price)
    elif item == "REMOVE":
        if entered_pass == Pass_Entry.get():
            a.unbind('<Return>')
            MCODE = Id_OptionMenu.get()
            MENU.remove_item(MCODE)
            FOOD()
            CTkMessagebox.CTkMessagebox(message="Dish Removed Successfully", title="RMS")
        else:
            CTkMessagebox.CTkMessagebox(message="Wrong Password Entered", title="RMS")
    elif item == 'MENU':
        MCODE = Id_OptionMenu.get()
        ITEM = Name_Entry.get()
        COURSE = CoursesOptionMenu.get()
        VEG = VegOptionMenu.get()
        PRICE = Sal_Entry.get()

        cursor.execute('SELECT ITEM,COURSE,VEG,PRICE FROM MENU where MCODE = %s', (MCODE,))
        data = cursor.fetchone()
        if ITEM == '':
            pass
        elif ITEM != data[0][0]:
            cursor.execute('update MENU set ITEM = %s where MCODE = %s', (ITEM.upper(), MCODE))
            db.commit()

        if COURSE == 'COURSE':
            pass
        elif COURSE != data[0][1]:
            cursor.execute('update MENU set COURSE = %s where MCODE = %s', (COURSE.upper(), MCODE))
            db.commit()

        if VEG == 'VEGETARIAN':
            pass
        elif VEG != data[0][2]:
            cursor.execute('update MENU set VEG = %s where MCODE = %s', (VEG.upper(), MCODE))
            db.commit()

        if PRICE == '':
            pass
        elif PRICE != data[0][3]:
            cursor.execute('update MENU set PRICE = %s where MCODE = %s', (PRICE, MCODE))
            db.commit()

        CTkMessagebox.CTkMessagebox(message="Menu Details Updated Successfully", title="RMS")

def NewMenu():
    Name_Entry.delete(0, END)
    Sal_Entry.delete(0, END)
    Add_Menu_btn.place_forget()
    Remove_Menu_btn.place_forget()
    Info_Menu_btn.place_forget()

    Left_arrow_btn.configure(command=lambda: FOOD())
    MainLabel.configure(text='NEW DISH')
    Name_Entry.configure(placeholder_text="DISH NAME")
    Sal_Entry.configure(placeholder_text='PRICE')
    CoursesOptionMenu.set('COURSES')
    VegOptionMenu.set('VEGETARIAN(YES/NO)')
    submit_btn.configure(text='SAVE', command=lambda: MenuUpdate('ADD'))

    Name_Entry.place(relx=0.5, rely=0.45, anchor='center')
    CoursesOptionMenu.place(relx=0.5, rely=0.58, anchor='center')
    VegOptionMenu.place(relx=0.5, rely=0.71, anchor='center')
    Sal_Entry.place(relx=0.5, rely=0.84, anchor='center')
    MainLabel.place(relx=0.5, rely=0.2, anchor='center')
    submit_btn.place(relx=0.8, rely=0.87)

def RemoveItem():
    Pass_Entry.delete(0, END)
    Add_Menu_btn.place_forget()
    Remove_Menu_btn.place_forget()
    Info_Menu_btn.place_forget()

    data = []
    Id_list = []
    cursor.execute('SELECT MCODE FROM menu')
    for tuple in cursor:
        data.append(list(tuple))
    for list1 in data:
        Id_list.append(str(list1[0]))

    Id_OptionMenu.configure(values=Id_list)
    Id_OptionMenu.set('MCODE')
    Pass_Entry.configure(placeholder_text='YOUR PASSWORD')
    submit_btn.configure(text='SAVE', command=lambda: MenuUpdate("REMOVE"))
    MainLabel.configure(text='REMOVE DISH')
    Left_arrow_btn.configure(command=lambda: FOOD())

    Id_OptionMenu.place(relx=0.5, rely=0.4, anchor='center')
    Pass_Entry.place(relx=0.5, rely=0.52, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')
    submit_btn.place(relx=0.8, rely=0.87)

    a.bind('<Return>', lambda event: MenuUpdate("REMOVE"))

def MCODE_MENU(MCODE):
    for list in data:
        if int(MCODE) == list[0]:
            MCODE = list[0]
            ITEM = list[1]
            COURSE = list[2]
            VEG = list[3]
            PRICE = list[4]
    Name_Entry.configure(state=NORMAL,placeholder_text=ITEM)
    CoursesOptionMenu.configure(state=NORMAL)
    CoursesOptionMenu.set(COURSE)
    VegOptionMenu.configure(state=NORMAL)
    VegOptionMenu.set(VEG)
    Sal_Entry.configure(state=NORMAL,placeholder_text=PRICE)
    submit_btn.configure(command=lambda: MenuUpdate('MENU'), text='SAVE')

    submit_btn.place(relx=0.8, rely=0.87)

def EditItem():
    global data
    Name_Entry.delete(0, END)
    Sal_Entry.delete(0, END)
    Add_Menu_btn.place_forget()
    Remove_Menu_btn.place_forget()
    Info_Menu_btn.place_forget()

    data = []
    MCODE_list = []
    cursor.execute('SELECT MCODE,ITEM,COURSE,VEG,PRICE FROM menu')
    for tuple in cursor:
        data.append(list(tuple))
    for list1 in data:
        MCODE_list.append(str(list1[0]))

    Id_OptionMenu.configure(values=MCODE_list, command=MCODE_MENU)
    Id_OptionMenu.set('MCODE')
    CoursesOptionMenu.set('COURSE')
    CoursesOptionMenu.configure(state=DISABLED)
    Name_Entry.configure(placeholder_text='DISH NAME')
    Name_Entry.configure(state=DISABLED)
    Sal_Entry.configure(placeholder_text='PRICE')
    Sal_Entry.configure(state=DISABLED)
    VegOptionMenu.set('VEGETARIAN')
    VegOptionMenu.configure(state=DISABLED)
    Left_arrow_btn.configure(command=lambda: FOOD())
    MainLabel.configure(text='EDIT MENU DETAILS')

    Id_OptionMenu.place(relx=0.5, rely=0.3, anchor='center')
    Name_Entry.place(relx=0.5, rely=0.4, anchor='center')
    CoursesOptionMenu.place(relx=0.5, rely=0.5, anchor='center')
    VegOptionMenu.place(relx=0.5, rely=0.6, anchor='center')
    Sal_Entry.place(relx=0.5, rely=0.7, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')

def FOOD():
    LogOut_btn.place_forget()
    Menu_btn.place_forget()
    Employee_btn.place_forget()
    Order_history_btn.place_forget()
    Name_Entry.place_forget()
    CoursesOptionMenu.place_forget()
    VegOptionMenu.place_forget()
    Sal_Entry.place_forget()
    submit_btn.place_forget()
    Id_OptionMenu.place_forget()
    Pass_Entry.place_forget()
    MainLabel.place_forget()

    Left_arrow_btn.configure(command=lambda: MANAGER())
    Add_Menu_btn.configure(command=lambda: NewMenu())
    Remove_Menu_btn.configure(command=lambda: RemoveItem())
    Info_Menu_btn.configure(command=lambda: EditItem())

    Add_Menu_btn.place(relx=0.25, rely=0.5, anchor='center')
    Remove_Menu_btn.place(relx=0.65, rely=0.5, anchor='center')
    Info_Menu_btn.place(relx=0.45, rely=0.5, anchor='center')
    Left_arrow_btn.place(relx=0.025, rely=0.03)

def OrderHistory():
    global frame
    Menu_btn.place_forget()
    Employee_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()

    Info_Employee_Frame.place(relx=0.02, rely=0.15)
    '''cursor.execute('SELECT ORDER_NO,TABLE_NO,ITEM,COURSE,VEG,PRICE,DATE_TIME FROM ORDERS NATURAL JOIN MENU')
    table = list()
    header = ['ORDER_NO','TABLE_NO','ITEM','COURSE','VEG','PRICE','DATE_TIME']
    for tuple in cursor:
        MenuList = list(tuple)
        table.append(MenuList)
    total_rows = len(table)
    total_columns = len(table[0])
    for i in range(len(header)):
        e = customtkinter.CTkEntry(Info_Employee_Frame, width=180, font=('Arial', 16, 'bold'), corner_radius=0)
        e.grid(row=0, column=i)
        e.insert(END, header[i])
        e.configure(state=DISABLED)
    for i in range(total_rows):
        for j in range(total_columns):
            e = customtkinter.CTkEntry(Info_Employee_Frame, width=180, font=('Arial', 16, 'bold'), corner_radius=0)
            e.grid(row=i + 1, column=j)
            e.insert(END, table[i][j])
            e.configure(state=DISABLED)'''
    cursor.execute('SELECT ORDER_NO,TABLE_NO,ITEM,COURSE,VEG,QUANTITY,PRICE,DATE_TIME,STATE FROM ORDERHISTORY NATURAL JOIN MENU')
    data = list()
    for tuple in cursor:
        data.append(tuple)
    frame = Frame(Info_Employee_Frame, height=400, width=800)
    frame.pack()


    tableView = ttk.Treeview(frame, style="Custom.Treeview", height=len(data))
    tableView['columns'] = ('ORDER_NO', 'TABLE_NO', 'ITEM', 'COURSE', 'VEG', 'QUANTITY', 'PRICE', 'DATE_TIME', 'STATE')
    tableView.column('#0', width=0, stretch=NO)
    tableView.column('ORDER_NO', anchor=CENTER, width=80)
    tableView.column('TABLE_NO', anchor=CENTER, width=80)
    tableView.column('ITEM', anchor=CENTER, width=200)
    tableView.column('COURSE', anchor=CENTER, width=100)
    tableView.column('VEG', anchor=CENTER, width=60)
    tableView.column('QUANTITY', anchor=CENTER, width=90)
    tableView.column('PRICE', anchor=CENTER, width=90)
    tableView.column('DATE_TIME', anchor=CENTER, width=110)
    tableView.column('STATE', anchor=CENTER, width=130)

    tableView.heading("#0", text="")
    tableView.heading('ORDER_NO', anchor=CENTER, text='ORDER_NO')
    tableView.heading('TABLE_NO', anchor=CENTER, text='TABLE_NO')
    tableView.heading('ITEM', anchor=CENTER, text='ITEM')
    tableView.heading('COURSE', anchor=CENTER, text='COURSE')
    tableView.heading('VEG', anchor=CENTER, text='VEG')
    tableView.heading('QUANTITY', anchor=CENTER, text='QUANTITY')
    tableView.heading('PRICE', anchor=CENTER, text='PRICE')
    tableView.heading('DATE_TIME', anchor=CENTER, text='DATE_TIME')
    tableView.heading('STATE', anchor=CENTER, text='STATE')

    for i in range(len(data)):
        tableView.insert(parent='', index='end', iid=i, text='', values=data[i])

    tableView.pack()
    Left_arrow_btn.configure(command=lambda: MANAGER())

    Left_arrow_btn.place(relx=0.025, rely=0.03)

def PlaceOrder():
    global mainFrame
    TABLE_NUMBER = TableNumber
    cursor.execute('select ORDER_NO from orders')
    if cursor.rowcount == 0:
        NewOrderNumber = 1
    else:
        listOfOrderNumber = list()
        for tuple in cursor:
            for orderNo in tuple:
                listOfOrderNumber.append(orderNo)
        NewOrderNumber = max(listOfOrderNumber) + 1
    for course in courses:
        if course == courses[0]:
            cursor.execute('select * from menu where course = %s',(courses[0],))
            data = cursor.fetchall()
            print(data)
            for APPETIZER in list_of_APPETIZER:
                QUANTITY = APPETIZER[1].get()
                if QUANTITY == '':
                    if APPETIZER[4] != 0:
                        QUANTITY = APPETIZER[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[APPETIZER[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
                cursor.execute('INSERT INTO ORDERHISTORY(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                                                        (%s,%s,%s,%s)',
                               (NewOrderNumber, data[APPETIZER[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
        elif course == courses[1]:
            cursor.execute('select * from menu where course = %s',(courses[1],))
            data = cursor.fetchall()
            print(data)
            for MAIN in list_of_MAIN:
                QUANTITY = MAIN[1].get()
                if QUANTITY == '':
                    if MAIN[4] != 0:
                        QUANTITY = MAIN[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[MAIN[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
                cursor.execute('INSERT INTO ORDERHISTORY(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                                                        (%s,%s,%s,%s)',
                               (NewOrderNumber, data[MAIN[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
        elif course == courses[2]:
            cursor.execute('select * from menu where course = %s',(courses[2],))
            data = cursor.fetchall()
            print(data)
            for DESSERT in list_of_DESSERT:
                QUANTITY = DESSERT[1].get()
                if QUANTITY == '':
                    if DESSERT[4] != 0:
                        QUANTITY = DESSERT[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[DESSERT[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
                cursor.execute('INSERT INTO ORDERHISTORY(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                                                        (%s,%s,%s,%s)',
                               (NewOrderNumber, data[DESSERT[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
        elif course == courses[3]:
            cursor.execute('select * from menu where course = %s',(courses[3],))
            data = cursor.fetchall()
            print(data)
            for BEVERAGE in list_of_BEVERAGE:
                QUANTITY = BEVERAGE[1].get()
                if QUANTITY == '':
                    if BEVERAGE[4] != 0:
                        QUANTITY = BEVERAGE[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[BEVERAGE[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
                cursor.execute('INSERT INTO ORDERHISTORY(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                                        (%s,%s,%s,%s)', (NewOrderNumber, data[BEVERAGE[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
    CTkMessagebox.CTkMessagebox(title='RMS', message="Order Place Successfully", icon='check')
    WAITER()

def course():
    global list_of_APPETIZER
    global list_of_MAIN
    global list_of_DESSERT
    global list_of_BEVERAGE

    TableNumberOptionMenu.place_forget()
    PlaceOrder_btn.place_forget()
    Bill_btn.place_forget()
    LogOut_btn.place_forget()

    def itemincrement(index,course):
        if course == 'APPETIZER':
            if list_of_APPETIZER[index][1].get() == '':
                if list_of_APPETIZER[index][4] == 0:
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(1))
                    list_of_APPETIZER[index][4] = 1
                else:
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(list_of_APPETIZER[index][4] + 1))
                    list_of_APPETIZER[index][4] += 1
            else:
                n = int(list_of_APPETIZER[index][1].get())
                list_of_APPETIZER[index][1].delete(0,END)
                list_of_APPETIZER[index][1].configure(placeholder_text=str(n+1))
                list_of_APPETIZER[index][4] = n + 1
        elif course == 'MAIN':
            if list_of_MAIN[index][1].get() == '':
                if list_of_MAIN[index][4] == 0:
                    list_of_MAIN[index][1].configure(placeholder_text=str(1))
                    list_of_MAIN[index][4] = 1
                else:
                    list_of_MAIN[index][1].configure(placeholder_text=str(list_of_MAIN[index][4] + 1))
                    list_of_MAIN[index][4] += 1
            else:
                n = int(list_of_MAIN[index][1].get())
                list_of_MAIN[index][1].delete(0,END)
                list_of_MAIN[index][1].configure(placeholder_text=str(n+1))
                list_of_MAIN[index][4] = n + 1
        elif course == 'DESSERT':
            if list_of_DESSERT[index][1].get() == '':
                if list_of_DESSERT[index][4] == 0:
                    list_of_DESSERT[index][1].configure(placeholder_text=str(1))
                    list_of_DESSERT[index][4] = 1
                else:
                    list_of_DESSERT[index][1].configure(placeholder_text=str(list_of_DESSERT[index][4] + 1))
                    list_of_DESSERT[index][4] += 1
            else:
                n = int(list_of_DESSERT[index][1].get())
                list_of_DESSERT[index][1].delete(0,END)
                list_of_DESSERT[index][1].configure(placeholder_text=str(n+1))
                list_of_DESSERT[index][4] = n + 1
        elif course == 'BEVERAGE':
            if list_of_BEVERAGE[index][1].get() == '':
                if list_of_BEVERAGE[index][4] == 0:
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(1))
                    list_of_BEVERAGE[index][4] = 1
                else:
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(list_of_BEVERAGE[index][4] + 1))
                    list_of_BEVERAGE[index][4] += 1
            else:
                n = int(list_of_BEVERAGE[index][1].get())
                list_of_BEVERAGE[index][1].delete(0,END)
                list_of_BEVERAGE[index][1].configure(placeholder_text=str(n+1))
                list_of_BEVERAGE[index][4] = n + 1

    def itemdecrement(index, course):
        list_of_APPETIZER[index][1].configure(state=NORMAL)
        if course == 'APPETIZER':
            if list_of_APPETIZER[index][1].get() == '':
                if list_of_APPETIZER[index][4] == 0:
                    pass
                else:
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(list_of_APPETIZER[index][4] - 1))
                    list_of_APPETIZER[index][4] -= 1
            else:
                if list_of_APPETIZER[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_APPETIZER[index][1].get())
                    list_of_APPETIZER[index][1].delete(0,END)
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(n-1))
                    list_of_APPETIZER[index][4] = n - 1
        elif course == 'MAIN':
            if list_of_MAIN[index][1].get() == '':
                if list_of_MAIN[index][4] == 0:
                    pass
                else:
                    list_of_MAIN[index][1].configure(placeholder_text=str(list_of_MAIN[index][4] - 1))
                    list_of_MAIN[index][4] -= 1
            else:
                if list_of_MAIN[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_MAIN[index][1].get())
                    list_of_MAIN[index][1].delete(0,END)
                    list_of_MAIN[index][1].configure(placeholder_text=str(n-1))
                    list_of_MAIN[index][4] = n - 1
        elif course == 'DESSERT':
            if list_of_DESSERT[index][1].get() == '':
                if list_of_DESSERT[index][4] == 0:
                    pass
                else:
                    list_of_DESSERT[index][1].configure(placeholder_text=str(list_of_DESSERT[index][4] - 1))
                    list_of_DESSERT[index][4] -= 1
            else:
                if list_of_DESSERT[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_DESSERT[index][1].get())
                    list_of_DESSERT[index][1].delete(0,END)
                    list_of_DESSERT[index][1].configure(placeholder_text=str(n-1))
                    list_of_DESSERT[index][4] = n - 1
        elif course == 'BEVERAGE':
            if list_of_BEVERAGE[index][1].get() == '':
                if list_of_BEVERAGE[index][4] == 0:
                    pass
                else:
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(list_of_BEVERAGE[index][4] - 1))
                    list_of_BEVERAGE[index][4] -= 1
            else:
                if list_of_BEVERAGE[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_BEVERAGE[index][1].get())
                    list_of_BEVERAGE[index][1].delete(0,END)
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(n-1))
                    list_of_BEVERAGE[index][4] = n - 1

    list_of_APPETIZER = []
    list_of_MAIN = []
    list_of_DESSERT = []
    list_of_BEVERAGE = []

    mainFrame.place(relx=0, rely=0.1)
    MainLabel.configure(text="MENU")
    a.geometry('1300x650')
    a.resizable(0,0)
    submit_btn.configure(text='PLACE ORDER', command=lambda: PlaceOrder())
    Left_arrow_btn.configure(command=lambda: WAITER())
    MainLabel.place(rely=0.05, relx=0.5, anchor='center')
    submit_btn.place(relx=0.87, rely=0.90)
    Left_arrow_btn.place(relx=0.025, rely=0.03)

    for course in courses:
        list_of_items = list()
        cursor.execute('select * from menu where course=%s',(course,))
        for record in cursor:
            list_of_items.append(record)

        secondaryFrame = customtkinter.CTkScrollableFrame(master= mainFrame,width=1274,fg_color='transparent',
                                                          height=260,orientation='horizontal',label_text=course)
        secondaryFrame.grid(column=0, row=courses.index(course), pady=(20,0))

        for i in range(len(list_of_items)):
            menu_frame = customtkinter.CTkFrame(secondaryFrame)
            name = list_of_items[i][1]
            name = name.split()
            tempName = ''
            for j in range(len(name)):
                tempName += '_' + name[j]
            name = tempName
            try:
                menu_img = Image.open('images/{}.png'.format(name))
                menu_icon = customtkinter.CTkImage(light_image=menu_img, size=(120,120))
            except:
                try:
                    menu_img = Image.open('images/{}.jpg'.format(name))
                    menu_icon = customtkinter.CTkImage(light_image=menu_img, size=(120,120))
                except:
                    pass

            menu_label = customtkinter.CTkLabel(menu_frame, text=list_of_items[i][1], anchor='center')
            img_label = customtkinter.CTkLabel(menu_frame, image=menu_icon, text=None)
            QuantityFrame = customtkinter.CTkFrame(menu_frame, fg_color='transparent')
            quantityLabel = customtkinter.CTkLabel(QuantityFrame, text='QUANTITY')
            PriceLabel = customtkinter.CTkLabel(QuantityFrame, text='PRICE')
            priceLabel = customtkinter.CTkLabel(QuantityFrame, text='$ ' + str(list_of_items[i][4]))
            quantityEntry = customtkinter.CTkEntry(QuantityFrame, placeholder_text='0', width=80, corner_radius=0)
            incrementButton = customtkinter.CTkButton(QuantityFrame, text='+', width=30, corner_radius=0)
            decrementButton = customtkinter.CTkButton(QuantityFrame, text='-', width=30, corner_radius=0)

            menu_frame.grid(column=i, row=0, padx=(20,20))
            menu_label.grid(column=0, row=0, padx=(20,20),pady=(10,5))
            img_label.grid(column=0, row=1)
            QuantityFrame.grid(column=0, row=2, padx=(20,20), pady=(20,0))
            quantityLabel.grid(column=0, row=0, padx=(0,10))
            decrementButton.grid(column=1, row=0)
            quantityEntry.grid(column=2, row=0)
            incrementButton.grid(column=3, row=0)
            PriceLabel.grid(column=0, row=3, pady=(10,5))
            priceLabel.grid(column=1, row=3, columnspan=3, pady=(10,5))
            if course == courses[0]:
                list_of_APPETIZER.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
            elif course == courses[1]:
                list_of_MAIN.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
            elif course == courses[2]:
                list_of_DESSERT.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
            elif course == courses[3]:
                list_of_BEVERAGE.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
    try:
        list_of_APPETIZER[0][2].configure(command=lambda: itemincrement(list_of_APPETIZER[0][0], courses[0]))
        list_of_APPETIZER[0][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[0][0], courses[0]))
        list_of_APPETIZER[1][2].configure(command=lambda: itemincrement(list_of_APPETIZER[1][0], courses[0]))
        list_of_APPETIZER[1][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[1][0], courses[0]))
        list_of_APPETIZER[2][2].configure(command=lambda: itemincrement(list_of_APPETIZER[2][0], courses[0]))
        list_of_APPETIZER[2][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[2][0], courses[0]))
        list_of_APPETIZER[3][2].configure(command=lambda: itemincrement(list_of_APPETIZER[3][0], courses[0]))
        list_of_APPETIZER[3][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[3][0], courses[0]))
        list_of_APPETIZER[4][2].configure(command=lambda: itemincrement(list_of_APPETIZER[4][0], courses[0]))
        list_of_APPETIZER[4][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[4][0], courses[0]))
        list_of_APPETIZER[5][2].configure(command=lambda: itemincrement(list_of_APPETIZER[5][0], courses[0]))
        list_of_APPETIZER[5][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[5][0], courses[0]))
        list_of_APPETIZER[6][2].configure(command=lambda: itemincrement(list_of_APPETIZER[6][0], courses[0]))
        list_of_APPETIZER[6][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[6][0], courses[0]))
    except:
        pass
    try:
        list_of_MAIN[0][2].configure(command=lambda: itemincrement(list_of_MAIN[0][0], courses[1]))
        list_of_MAIN[0][3].configure(command=lambda: itemdecrement(list_of_MAIN[0][0], courses[1]))
        list_of_MAIN[1][2].configure(command=lambda: itemincrement(list_of_MAIN[1][0], courses[1]))
        list_of_MAIN[1][3].configure(command=lambda: itemdecrement(list_of_MAIN[1][0], courses[1]))
        list_of_MAIN[2][2].configure(command=lambda: itemincrement(list_of_MAIN[2][0], courses[1]))
        list_of_MAIN[2][3].configure(command=lambda: itemdecrement(list_of_MAIN[2][0], courses[1]))
        list_of_MAIN[3][2].configure(command=lambda: itemincrement(list_of_MAIN[3][0], courses[1]))
        list_of_MAIN[3][3].configure(command=lambda: itemdecrement(list_of_MAIN[3][0], courses[1]))
        list_of_MAIN[4][2].configure(command=lambda: itemincrement(list_of_MAIN[4][0], courses[1]))
        list_of_MAIN[4][3].configure(command=lambda: itemdecrement(list_of_MAIN[4][0], courses[1]))
        list_of_MAIN[5][2].configure(command=lambda: itemincrement(list_of_MAIN[5][0], courses[1]))
        list_of_MAIN[5][3].configure(command=lambda: itemdecrement(list_of_MAIN[5][0], courses[1]))
        list_of_MAIN[6][2].configure(command=lambda: itemincrement(list_of_MAIN[6][0], courses[1]))
        list_of_MAIN[6][3].configure(command=lambda: itemdecrement(list_of_MAIN[6][0], courses[1]))
    except:
        pass
    try:
        list_of_DESSERT[0][2].configure(command=lambda: itemincrement(list_of_DESSERT[0][0], courses[2]))
        list_of_DESSERT[0][3].configure(command=lambda: itemdecrement(list_of_DESSERT[0][0], courses[2]))
        list_of_DESSERT[1][2].configure(command=lambda: itemincrement(list_of_DESSERT[1][0], courses[2]))
        list_of_DESSERT[1][3].configure(command=lambda: itemdecrement(list_of_DESSERT[1][0], courses[2]))
        list_of_DESSERT[2][2].configure(command=lambda: itemincrement(list_of_DESSERT[2][0], courses[2]))
        list_of_DESSERT[2][3].configure(command=lambda: itemdecrement(list_of_DESSERT[2][0], courses[2]))
        list_of_DESSERT[3][2].configure(command=lambda: itemincrement(list_of_DESSERT[3][0], courses[2]))
        list_of_DESSERT[3][3].configure(command=lambda: itemdecrement(list_of_DESSERT[3][0], courses[2]))
        list_of_DESSERT[4][2].configure(command=lambda: itemincrement(list_of_DESSERT[4][0], courses[2]))
        list_of_DESSERT[4][3].configure(command=lambda: itemdecrement(list_of_DESSERT[4][0], courses[2]))
        list_of_DESSERT[5][2].configure(command=lambda: itemincrement(list_of_DESSERT[5][0], courses[2]))
        list_of_DESSERT[5][3].configure(command=lambda: itemdecrement(list_of_DESSERT[5][0], courses[2]))
        list_of_DESSERT[6][2].configure(command=lambda: itemincrement(list_of_DESSERT[6][0], courses[2]))
        list_of_DESSERT[6][3].configure(command=lambda: itemdecrement(list_of_DESSERT[6][0], courses[2]))
    except:
        pass
    try:
        list_of_BEVERAGE[0][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[0][0], courses[3]))
        list_of_BEVERAGE[0][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[0][0], courses[3]))
        list_of_BEVERAGE[1][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[1][0], courses[3]))
        list_of_BEVERAGE[1][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[1][0], courses[3]))
        list_of_BEVERAGE[2][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[2][0], courses[3]))
        list_of_BEVERAGE[2][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[2][0], courses[3]))
        list_of_BEVERAGE[3][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[3][0], courses[3]))
        list_of_BEVERAGE[3][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[3][0], courses[3]))
        list_of_BEVERAGE[4][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[4][0], courses[3]))
        list_of_BEVERAGE[4][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[4][0], courses[3]))
        list_of_BEVERAGE[5][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[5][0], courses[3]))
        list_of_BEVERAGE[5][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[5][0], courses[3]))
        list_of_BEVERAGE[6][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[6][0], courses[3]))
        list_of_BEVERAGE[6][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[6][0], courses[3]))
    except:
        pass

def BillPaid(TOTAL, TABLENUMBER):
    ans = CTkMessagebox.CTkMessagebox(title='RMS', message='Payment of $ '+str(TOTAL)+' successful',
                                      icon='check')
    cursor.execute('update ORDERHISTORY set state="PAID" where TABLE_NO=%s', (TABLENUMBER,))
    cursor.execute('delete from ORDERS where TABLE_NO=%s', (TABLENUMBER,))
    db.commit()
    if ans.get() == 'OK':
        BillWindow.destroy()


def PayBills(TABLE_NUMBER):
    global BillWindow
    BillWindow = customtkinter.CTkToplevel()
    BillWindow.after(250, lambda: BillWindow.iconbitmap('images/logo.ico'))
    BillWindow.geometry('600x500')
    MainLabel = customtkinter.CTkLabel(BillWindow, text="Main Label", font=customtkinter.CTkFont(size=40),
                                       text_color='#2fa572')
    submit_btn = customtkinter.CTkButton(BillWindow, text='SUBMIT', height=50,
                                         font=customtkinter.CTkFont(size=15, weight='bold'))
    list_of_items = list()
    cursor.execute('select ITEM,QUANTITY,PRICE,PRICE*QUANTITY from ORDERS natural join menu where TABLE_NO=%s',
                   (TABLE_NUMBER,))
    for record in cursor:
        list_of_items.append(record)
    if list_of_items == []:
        BillWindow.destroy()
        CTkMessagebox.CTkMessagebox(title='RMS', message='No Orders', icon='warning')
    else:
        TotalAmount = 0
        secondaryFrame = customtkinter.CTkScrollableFrame(BillWindow, width=574, fg_color='transparent', height=300)
        secondaryFrame.grid(column=0, row=2, columnspan=3, pady=(20, 0))
        for i in range(len(list_of_items)):
            name = list_of_items[i][0]
            name = name.split()
            tempName = ''
            for j in range(len(name)):
                tempName += '_' + name[j]
            name = tempName
            try:
                img = Image.open('images/{}.png'.format(name))
                icon = customtkinter.CTkImage(dark_image=img, size=(50, 50))
            except:
                try:
                    img = Image.open('images/{}.jpg'.format(name))
                    icon = customtkinter.CTkImage(dark_image=img, size=(50, 50))
                except:
                    pass
            name_label = customtkinter.CTkLabel(secondaryFrame, text=list_of_items[i][0], anchor='center')
            img_label = customtkinter.CTkLabel(secondaryFrame, image=icon, text=None, compound='left')
            quantity_label = customtkinter.CTkLabel(secondaryFrame, text=list_of_items[i][1], anchor='center')
            price_label = customtkinter.CTkLabel(secondaryFrame, text='$ ' + str(list_of_items[i][2]), anchor='center')
            amount_label = customtkinter.CTkLabel(secondaryFrame, text='$ ' + str(list_of_items[i][3]), anchor='center')

            name_label.grid(column=1, row=i + 1, padx=(20, 0), pady=(10, 5))
            img_label.grid(column=0, row=i + 1, padx=(20, 0), pady=(10, 5))
            quantity_label.grid(column=3, row=i + 1, padx=(10, 10), pady=(10, 5))
            price_label.grid(column=2, row=i + 1, padx=(10, 10), pady=(10, 5))
            amount_label.grid(column=4, row=i + 1, padx=(0, 0), pady=(10, 5))
            TotalAmount += list_of_items[i][2]
        ItemLabel = customtkinter.CTkLabel(secondaryFrame, text='ITEM NAME', anchor='center', bg_color='#343638')
        PriceLabel = customtkinter.CTkLabel(secondaryFrame, text='PRICE', anchor='center', bg_color='#343638')
        QuantityLabel = customtkinter.CTkLabel(secondaryFrame, text='QUANTITY', anchor='center', bg_color='#343638')
        AmountLabel = customtkinter.CTkLabel(secondaryFrame, text='AMOUNT', anchor='center', bg_color='#343638')
        total_amount_Label = customtkinter.CTkLabel(BillWindow, text='TOTAL AMOUNT', anchor='center',
                                                    font=customtkinter.CTkFont(size=25))
        TotalAmount_Label = customtkinter.CTkLabel(BillWindow, text='$ ' + str(TotalAmount), anchor='center',
                                                   font=customtkinter.CTkFont(family='roman', size=30))
        submit_btn.configure(text='PAY', height=35, command=lambda: BillPaid(TotalAmount, TABLE_NUMBER))
        MainLabel.configure(text='PAYMENT')

        MainLabel.grid(row=0, column=0, columnspan=3, pady=(20, 0))
        ItemLabel.grid(row=0, column=0, columnspan=2, ipadx=95)
        PriceLabel.grid(row=0, column=2, ipadx=20, padx=(10, 10))
        QuantityLabel.grid(row=0, column=3, ipadx=10, padx=(10, 10))
        AmountLabel.grid(row=0, column=4, ipadx=10, padx=(0, 0))
        total_amount_Label.grid(row=3, column=0, pady=(0, 20), rowspan=2)
        TotalAmount_Label.grid(row=3, column=2)
        submit_btn.grid(row=4, column=2, pady=(20, 0))

def TableSelected(TableNumber2):
    global TableNumber
    TableNumber = TableNumber2
    PlaceOrder_btn.configure(state=NORMAL)
    Bill_btn.configure(state=NORMAL)

def LogOut():
    ans = CTkMessagebox.CTkMessagebox(title=ENAME, message="Do you want to Log Out", icon='question', option_1="Ok", option_2="Cancel")
    if ans.get() == "Ok":
        login()

def WAITER():
    Id_Entry.place_forget()
    Pass_Entry.place_forget()
    mainFrame.place_forget()
    submit_btn.place_forget()
    MainLabel.place_forget()
    Left_arrow_btn.place_forget()

    a.geometry('1000x600')
    LogOut_btn.configure(command=lambda: LogOut())
    PlaceOrder_btn.configure(command=lambda: course(), state=DISABLED)
    Bill_btn.configure(command=lambda: PayBills(TableNumberOptionMenu.get()), state=DISABLED)
    TableNumberOptionMenu.configure(command=TableSelected)
    TableNumberOptionMenu.set('TABLE NUMBER')

    TableNumberOptionMenu.place(rely=0.2, relx=0.5, anchor='center')
    PlaceOrder_btn.place(relx=0.25, rely=0.5, anchor='center')
    Bill_btn.place(relx=0.45, rely=0.5, anchor='center')
    LogOut_btn.place(relx=0.65, rely=0.5, anchor='center')

def MANAGER():
    frame.destroy()
    Id_Entry.place_forget()
    Pass_Entry.place_forget()
    submit_btn.place_forget()
    MainLabel.place_forget()
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Edit_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Left_arrow_btn.place_forget()
    Add_Menu_btn.place_forget()
    Remove_Menu_btn.place_forget()
    Info_Menu_btn.place_forget()

    Employee_btn.configure(command=lambda: EMPLOYEE())
    LogOut_btn.configure(command=lambda: LogOut())
    Order_history_btn.configure(command=lambda: OrderHistory())
    Menu_btn.configure(command=lambda: FOOD())

    Employee_btn.place(relx=0.65, rely=0.3, anchor='center')
    Menu_btn.place(relx=0.35, rely=0.3, anchor='center')
    Order_history_btn.place(relx=0.35, rely=0.725, anchor='center')
    LogOut_btn.place(relx=0.65, rely=0.725, anchor='center')

def id_format_error():
    try:
        entered_id = int(Id_OptionMenu.get())
        return entered_id
    except:
        CTkMessagebox.CTkMessagebox(title='Try Again', message='INVALID FORMAT FOR AN ID', icon="cancel")

def verify_id():
    global ENAME
    global entered_pass
    a.unbind('<Return>')

    cursor.execute('select EID,PASS,DEPT,ENAME from employee')
    entered_id = id_format_error()
    entered_pass = Pass_Entry.get()

    for i in cursor:
        if i[0] == int(entered_id):
            if i[1] == entered_pass:
                ENAME = i[3]
                Id_OptionMenu.place_forget()
                Pass_Entry.place_forget()
                submit_btn.place_forget()
                MainLabel.place_forget()
                if i[2] == "WAITER":
                    CTkMessagebox.CTkMessagebox(title=ENAME, message="Welcome "+ENAME, icon='check')
                    WAITER()
                if i[2] == "MANAGER":
                    CTkMessagebox.CTkMessagebox(title=i[3], message="Welcome " + i[3], icon='check')
                    MANAGER()
            else:
                print('\nIncorrect PASSWORD\nTry Again')
                ans = CTkMessagebox.CTkMessagebox(title='Try Again', message="Incorrect PASSWORD", icon='warning')
                a.bind('<Return>', lambda event: verify_id())
            break
    else:
        CTkMessagebox.CTkMessagebox(title='Try Again', message="An user with this ID doesn't exist", icon="cancel")
        a.bind('<Return>', lambda event: verify_id())

def LoginIdMenu(ID):
    Pass_Entry.configure(state=NORMAL)
    Pass_Entry.delete(0, END)
    Pass_Entry.configure(show='*')
    Pass_Entry.icursor(0)
    submit_btn.configure(state=NORMAL)
    Name_Entry.configure(placeholder_text='ENTER EMPLOYEE NAME')

def login():
    Left_arrow_btn.place_forget()
    Employee_btn.place_forget()
    Menu_btn.place_forget()
    LogOut_btn.place_forget()
    Order_history_btn.place_forget()
    TableNumberOptionMenu.place_forget()
    PlaceOrder_btn.place_forget()
    Bill_btn.place_forget()
    #Id_Entry.delete(0, END)
    Pass_Entry.delete(0, END)

    data = []
    Id_list = []

    cursor.execute('SELECT EID,ENAME,DEPT,salary,DOJ,PASS FROM employee')
    for tuple in cursor:
        data.append(list(tuple))
    for list1 in data:
        Id_list.append(str(list1[0]))

    MainLabel.configure(text="Enter Login credentials")
    Id_OptionMenu.configure(values=Id_list, command=LoginIdMenu)
    Id_OptionMenu.set('EMPLOYEE ID')
    Pass_Entry.configure(show='')
    Pass_Entry.configure(placeholder_text='PASSWORD', height=50,
                         font=customtkinter.CTkFont(size=15), width=300)
    Pass_Entry.configure(state=DISABLED)
    submit_btn.configure(text='SUBMIT', command=lambda: verify_id())
    submit_btn.configure(state=DISABLED)

    Id_OptionMenu.place(relx=0.5, rely=0.4, anchor='center')
    Pass_Entry.place(relx=0.5, rely=0.52, anchor='center')
    submit_btn.place(relx=0.5, rely=0.7, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')

    a.bind('<Return>', lambda event: verify_id())


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
#BillWindow.minsize(900,600)
#BillWindow.maxsize(1000,700)
#BillWindow.resizable(0,0)

#DATABASE CONNECTION
db = mysql.connector.connect(host='localhost', user='root', passwd='1234', auth_plugin='mysql_native_password')
#db = mysql.connector.connect(host='localhost', user='root', passwd='mes123@tirur')
#db = mysql.connector.connect(host='localhost', user='root', passwd='')
cursor = db.cursor(buffered=True)
cursor.execute('create DATABASE IF NOT EXISTS rms')
cursor.execute('use rms')

#TABLE CREATION
cursor.execute('create table IF NOT EXISTS MENU(MCODE int(3) primary key,ITEM varchar(50),\
                COURSE varchar(20),VEG varchar(3),PRICE int(5),\
                CONSTRAINT CHECK_VEG CHECK (VEG = "YES" OR VEG = "NO"))')
cursor.execute('create table IF NOT EXISTS employee(EID int primary key,ENAME varchar(50),\
                DEPT varchar(50),SALARY int,PASS varchar(8) DEFAULT "0",\
                DOJ DATE DEFAULT (DATE_FORMAT(NOW(), "%Y-%m-%d")))')
cursor.execute('create table IF NOT EXISTS ORDERS(ORDER_NO INT,TABLE_NO INT,\
                QUANTITY INT,MCODE INT,DATE_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,\
                FOREIGN KEY(MCODE) REFERENCES MENU(MCODE))')
cursor.execute('create table IF NOT EXISTS ORDERHISTORY(ORDER_NO INT,TABLE_NO INT,\
                QUANTITY INT,MCODE INT,DATE_TIME DATETIME DEFAULT CURRENT_TIMESTAMP,\
                STATE VARCHAR(20) DEFAULT ("ORDERED"),\
                FOREIGN KEY(MCODE) REFERENCES MENU(MCODE))')


#INSERTING VALUES TO MENU TABLE
try:
    cursor.execute("insert into menu values (101,'BUFFALO CHICKEN MEATBALLS','APPETIZER','NO',199),\
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
except:
    pass
#INSERTING VALUES TO EMPLOYEE TABLE
try:
    cursor.execute('insert into EMPLOYEE(EID,ENAME,DEPT,SALARY,PASS) values\
                    (1,"AMAN","MANAGER",4569,"1234"),\
                    (2,"IBADH","WAITER",3464,"0")')
    db.commit()
except:
    pass

courses = ['APPETIZER', 'MAIN', 'DESSERT', 'BEVERAGE']
dept = ['WAITER', 'MANAGER']

MainLabel = customtkinter.CTkLabel(a, text="Main Label", font=customtkinter.CTkFont(size=40),
                                   text_color='#2fa572')
mainFrame = customtkinter.CTkScrollableFrame(a,width=1284,height=500,corner_radius=0,fg_color='transparent')
Info_Employee_Frame = customtkinter.CTkScrollableFrame(a, width=960, height=430, corner_radius=0,
                                                       fg_color='transparent')
TableNumberOptionMenu = customtkinter.CTkComboBox(a, values=list(str(i) for i in range(1,11)), command=None, height=50,
                                                  font=customtkinter.CTkFont(size=16), width=300)
Id_Entry = customtkinter.CTkEntry(a, placeholder_text='EMPLOYEE ID', height=50,
                                  font=customtkinter.CTkFont(size=16), width=300)
Id_OptionMenu = customtkinter.CTkComboBox(a, values=None, command=None, height=50,
                                          font=customtkinter.CTkFont(size=15), width=300)
DeptOptionMenu = customtkinter.CTkComboBox(a, values=dept, height=50,
                                           font=customtkinter.CTkFont(size=15), width=300)
CoursesOptionMenu = customtkinter.CTkComboBox(a, values=courses, height=50,
                                              font=customtkinter.CTkFont(size=15), width=300)
VegOptionMenu = customtkinter.CTkComboBox(a, values=['YES','NO'], height=50,
                                          font=customtkinter.CTkFont(size=15), width=300)
Pass_Entry = customtkinter.CTkEntry(a, placeholder_text='PASSWORD', height=50,
                                    font=customtkinter.CTkFont(size=15), width=300, show='*')
submit_btn = customtkinter.CTkButton(a, text='SUBMIT', height=50, font=customtkinter.CTkFont(size=15, weight='bold'))
frame = Frame(Info_Employee_Frame, height=400, width=800)

Manager_img = Image.open('images/Manager_img.png')
Employee_img = Image.open('images/Employee_img.png')
Order_history_img = Image.open('images/Order_history.png')
LogOut_img = Image.open('images/logout.png')
Menu_img = Image.open('images/platter.png')
PlaceOrder_img = Image.open('images/menu.png')
Bill_img = Image.open('images/invoice.png')
Left_arrow_img = Image.open('images/left-arrow2.png')
Add_Employee_img = Image.open('images/add_employee.png')
Dismiss_Employee_img = Image.open('images/dismiss_employee.png')
Info_Employee_img = Image.open('images/info_employee.png')
Edit_Employee_img = Image.open('Images/Edit_employee.png')
Add_Menu_img = Image.open('Images/add_menu.png')
Remove_Menu_img = Image.open('Images/remove_menu.png')
Info_Menu_img = Image.open('Images/edit_menu.png')

Manager_icon = customtkinter.CTkImage(dark_image=Manager_img, size=(120,120))
Employee_icon = customtkinter.CTkImage(dark_image=Employee_img, size=(120,120))
Order_history_icon = customtkinter.CTkImage(dark_image=Order_history_img, size=(120,120))
LogOut_icon = customtkinter.CTkImage(dark_image=LogOut_img, size=(120,120))
Menu_icon = customtkinter.CTkImage(dark_image=Menu_img, size=(120,120))
PlaceOrder_icon = customtkinter.CTkImage(dark_image=PlaceOrder_img, size=(120,120))
Bill_icon = customtkinter.CTkImage(dark_image=Bill_img, size=(120,120))
Left_arrow_icon = customtkinter.CTkImage(dark_image=Left_arrow_img, size=(20,20))
Add_Employee_icon = customtkinter.CTkImage(dark_image=Add_Employee_img, size=(120,120))
Dismiss_Employee_icon = customtkinter.CTkImage(dark_image=Dismiss_Employee_img, size=(120,120))
Info_Employee_icon = customtkinter.CTkImage(dark_image=Info_Employee_img, size=(120,120))
Edit_Employee_icon = customtkinter.CTkImage(dark_image=Edit_Employee_img, size=(120,120))
Add_Menu_icon = customtkinter.CTkImage(dark_image=Add_Menu_img, size=(120,120))
Remove_Menu_icon = customtkinter.CTkImage(dark_image=Remove_Menu_img, size=(120,120))
Info_Menu_icon = customtkinter.CTkImage(dark_image=Info_Menu_img, size=(120,120))

Manager_btn = customtkinter.CTkButton(a, text='Manager', image=Manager_icon, height=170, width=150,
                                      compound='top', command=None, text_color='silver')
Employee_btn = customtkinter.CTkButton(a, text='EMPLOYEE', image=Employee_icon, height=170, width=150,
                                       compound='top', command=None)
Order_history_btn = customtkinter.CTkButton(a, image=Order_history_icon, text='Order History', height=170,
                                            width=150, compound='top')
LogOut_btn = customtkinter.CTkButton(a, image=LogOut_icon, text='Log Out', compound='top', height=170,width=150,
                                     command=None)
Menu_btn = customtkinter.CTkButton(a, text='MENU', image=Menu_icon, compound='top', height=170, width=150,)
PlaceOrder_btn = customtkinter.CTkButton(a, text='PLACE ORDER', image=PlaceOrder_icon, compound='top', height=170, width=150)
Bill_btn = customtkinter.CTkButton(a, text='PAY BILL', image=Bill_icon, compound='top', height=170, width=150)
Left_arrow_btn = customtkinter.CTkButton(a, image=Left_arrow_icon, text='', width=40, height=20,
                                         corner_radius=1000, command=None)
Add_Employee_btn = customtkinter.CTkButton(a, image=Add_Employee_icon, text='RECRUIT EMPLOYEE', compound='top',
                                           height=170, width=150, command=lambda: Add_employee())
Dismiss_Employee_btn = customtkinter.CTkButton(a, image=Dismiss_Employee_icon, text='DISMISS EMPLOYEE',
                                               compound='top', height=170, width=150,
                                               command=lambda: Dismiss_employee())
Info_Employee_btn = customtkinter.CTkButton(a, image=Info_Employee_icon, text='EMPLOYEE INFO', compound='top',
                                            height=170, width=150, command=None)
Edit_Employee_btn = customtkinter.CTkButton(a, image=Edit_Employee_icon, text='EDIT EMPLOYEE', compound='top',
                                            height=170, width=150, command=None)
Add_Menu_btn = customtkinter.CTkButton(a, image=Add_Menu_icon, text='ADD ITEM', compound='top',
                                            height=170, width=150, command=None)
Remove_Menu_btn = customtkinter.CTkButton(a, image=Remove_Menu_icon, text='REMOVE ITEM', compound='top',
                                            height=170, width=150, command=None)
Info_Menu_btn = customtkinter.CTkButton(a, image=Info_Menu_icon, text='ITEM INFO', compound='top',
                                            height=170, width=150, command=None)
Name_Entry = customtkinter.CTkEntry(a, placeholder_text='EMPLOYEE NAME', height=50,
                                  font=('halvatica', 16), width=300)
Dept_Entry = customtkinter.CTkEntry(a, placeholder_text='DEPARTMENT', height=50,
                                  font=('halvatica', 16), width=300)
Sal_Entry = customtkinter.CTkEntry(a, placeholder_text='SALARY', height=50,
                                  font=('halvatica', 16), width=300)
DOJ_Entry = customtkinter.CTkEntry(a, placeholder_text='DOJ', height=50,
                                  font=('halvatica', 16), width=300)

st = ttk.Style()
st.element_create("Custom.TreeHeading.border", "from", "default")
st.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.Border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
            ("Custom.Treeheading.text", {'sticky': 'nswe'})
        ]})
    ]})
])
st.configure("Treeview", background="#4A4D50", foreground="#F9F9FA", bordercolor="red")
st.configure("Custom.Treeview.Heading", background="#343638", foreground="gray98", border='gray28', borderwidth=234)
st.map("Custom.Treeview.Heading", relief=[('active', 'groove'), ('pressed', 'flat')])
# 343638
# 979DA2

#login()
OrderHistory()
a.protocol("WM_DELETE_WINDOW", QUIT)
a.mainloop()
