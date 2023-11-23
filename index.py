import time
from tkinter import *
from tkinter import messagebox
import CTkMessagebox
import customtkinter
from PIL import ImageTk, Image
import mysql.connector

import MENU


class employee():
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
        cursor.execute("delete from employee where EID = (%s)",(EID,))
        db.commit()
        
def QUIT():
    ans = CTkMessagebox.CTkMessagebox(title='rms', message='Do you want to Quit', icon='question', option_1="Ok", option_2="Cancel")
    if ans.get() == "Ok":
        a.destroy()

def Emp_Update(item="basic"):
    if item == "basic":
        a.unbind('<Return>')
        NEWLIST = list()
        for i in entryList:
            rowList = list()
            for j in i:
                rowList.append(j[0].get())
            NEWLIST.append(tuple(rowList))
        print(NEWLIST)
        duplicate = False
        for i in NEWLIST:
            print(1)
            cursor.execute('select ENAME,DEPT,salary,PASS from employee where EID = %s',(i[0],))
            data = cursor.fetchall()
            print(data)

            if data[0][0] == i[1]:
                print(0)
                pass
            else:
                cursor.execute('update employee set ENAME = %s where EID = %s', (i[1].upper(), i[0]))
                db.commit()

            if data[0][1] == i[2]:
                print(1)
                pass
            else:
                cursor.execute('update employee set DEPT = %s where EID = %s', (i[2].upper(), i[0]))
                db.commit()

            if data[0][2] == i[3]:
                pass
            else:
                cursor.execute('update employee set salary = %s where EID = %s', (i[3], i[0]))
                db.commit()

            if data[0][3] == i[5]:
                pass
            else:
                cursor.execute('update employee set PASS = %s where EID = %s', (i[5], i[0]))
                db.commit()

        CTkMessagebox.CTkMessagebox(message="Employee Details Updated Successfully", title="RMS")
        EMPLOYEE()
    elif item == "ADD":
        a.unbind('<Return>')
        ENAME = Name_Entry.get()
        DEPT = DeptOptionMenu.get()
        print(DEPT)
        SAL = Sal_Entry.get()
        if DEPT == 'DEPARTMENT':
            CTkMessagebox.CTkMessagebox(title='RMS', message='Choose a Department')
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
    a.bind('<Return>', lambda: Emp_Update())'''

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

        cursor.execute('SELECT ITEM,COURSE,VEG,PRICE FROM menu where MCODE = %s', (MCODE,))
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

def LogOut():
    ans = CTkMessagebox.CTkMessagebox(title=ENAME, message="Do you want to Log Out", icon='question', option_1="Ok", option_2="Cancel")
    if ans.get() == "Ok":
        login()

def WAITER():
    Id_Entry.place_forget()
    Pass_Entry.place_forget()

    LogOut_btn.configure(command=lambda: LogOut())

def MANAGER():
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
    Order_history_btn.configure(command=lambda: History())
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
                ans = messagebox.showwarning(title='Try Again', message="Incorrect PASSWORD")
                a.bind('<Return>', lambda event: Emp_Update("ADD"))
            break
    else:
        CTkMessagebox.CTkMessagebox(title='Try Again', message="An user with this ID doesn't exist", icon="cancel")
        a.bind('<Return>', lambda event: Emp_Update("ADD"))

def LoginIdMenu(ID):
    Pass_Entry.configure(state=NORMAL, show='*')
    submit_btn.configure(state=NORMAL)
    Name_Entry.configure(placeholder_text='EMPLOYEE NAME')

def login():
    Left_arrow_btn.place_forget()
    Employee_btn.place_forget()
    Menu_btn.place_forget()
    LogOut_btn.place_forget()
    Order_history_btn.place_forget()
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
    Pass_Entry.configure(placeholder_text='PASSWORD')
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
#a.minsize(900,600)
#a.maxsize(1000,700)
#a.resizable(0,0)

db = mysql.connector.connect(host='localhost', user='root', passwd='1234', auth_plugin='mysql_native_password')
#db = mysql.connector.connect(host='localhost', user='root', passwd='mes123@tirur')
#db = mysql.connector.connect(host='localhost', user='root', passwd='')
cursor = db.cursor(buffered=True)

cursor.execute('use rms')

MainLabel = customtkinter.CTkLabel(a, text="Main Label", font=customtkinter.CTkFont(size=40),
                                   text_color='#2fa572')
Info_Employee_Frame = customtkinter.CTkScrollableFrame(a, width=960, height=430, corner_radius=0,
                                                       fg_color='transparent')
Id_Entry = customtkinter.CTkEntry(a, placeholder_text='EMPLOYEE ID', height=50,
                                  font=('halvatica', 16), width=300)
Id_OptionMenu = customtkinter.CTkComboBox(a, values=None, command=None, height=50,
                                            font=('halvatica', 15), width=300)
DeptOptionMenu = customtkinter.CTkComboBox(a, values=['WAITER', 'MANAGER'], height=50,
                                            font=('halvatica', 15), width=300)
CoursesOptionMenu = customtkinter.CTkComboBox(a, values=['APPETIZER','MAIN','DESSERT','BEVERAGE'], height=50,
                                            font=('halvatica', 15), width=300)
VegOptionMenu = customtkinter.CTkComboBox(a, values=['YES','NO'], height=50,
                                            font=('halvatica', 15), width=300)
Pass_Entry = customtkinter.CTkEntry(a, placeholder_text='PASSWORD', height=50,
                                    font=('halvatica', 15), width=300, show='*')
submit_btn = customtkinter.CTkButton(a, text='SUBMIT', height=50, font=('halvatica', 16, 'bold'))

Manager_img = Image.open('images/Manager_img.png')
Manager_img = Manager_img.resize((120, 120))
Employee_img = Image.open('images/Employee_img.png')
Employee_img = Employee_img.resize((120, 120))
Order_history_img = Image.open('images/Order_history.png')
Order_history_img = Order_history_img.resize((120,120))
LogOut_img = Image.open('images/logout.png')
LogOut_img = LogOut_img.resize((120,120))
Menu_img = Image.open('images/menu.png')
Menu_img = Menu_img.resize((120,120))
Left_arrow_img = Image.open('images/left-arrow2.png')
Left_arrow_img = Left_arrow_img.resize((30,30))
Add_Employee_img = Image.open('images/add_employee.png')
Add_Employee_img = Add_Employee_img.resize((120,120))
Dismiss_Employee_img = Image.open('images/dismiss_employee.png')
Dismiss_Employee_img = Dismiss_Employee_img.resize((120,120))
Info_Employee_img = Image.open('images/info_employee.png')
Info_Employee_img = Info_Employee_img.resize((120,120))
Edit_Employee_img = Image.open('Images/Edit_employee.png')
Edit_Employee_img = Edit_Employee_img.resize((120, 120))
Add_Menu_img = Image.open('Images/add_menu.png')
#Add_Menu_img.resize((60,120))
Remove_Menu_img = Image.open('Images/remove_menu.png')
print(0)
Remove_Menu_img.resize((120,120))
Info_Menu_img = Image.open('Images/edit_menu.png')
Info_Menu_img.resize((120,120))

Manager_icon = ImageTk.PhotoImage(Manager_img)
Employee_icon = ImageTk.PhotoImage(Employee_img)
Order_history_icon = ImageTk.PhotoImage(Order_history_img)
LogOut_icon = ImageTk.PhotoImage(LogOut_img)
Menu_icon = ImageTk.PhotoImage(Menu_img)
Left_arrow_icon = ImageTk.PhotoImage(Left_arrow_img)
Add_Employee_icon = ImageTk.PhotoImage(Add_Employee_img)
Dismiss_Employee_icon = ImageTk.PhotoImage(Dismiss_Employee_img)
Info_Employee_icon = ImageTk.PhotoImage(Info_Employee_img)
Edit_Employee_icon = ImageTk.PhotoImage(Edit_Employee_img)
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
Left_arrow_btn = customtkinter.CTkButton(a, image=Left_arrow_icon, text='', width=40, height=20,
                                         corner_radius=1000, command=None)
Add_Employee_btn = customtkinter.CTkButton(a, image=Add_Employee_icon, text='RECRUIT EMPLOYEE', compound='top',
                                           height=170, width=150, command=lambda: Add_employee())
Dismiss_Employee_btn = customtkinter.CTkButton(a, image=Dismiss_Employee_icon, text='DISMISS EMPLOYEE',
                                               compound='top', height=170, width=150,
                                               command=lambda: Dismiss_employee())
Info_Employee_btn = customtkinter.CTkButton(a, image=Info_Employee_icon, text='EMPLOYEE INFO', compound='top',
                                            height=170, width=150, command=lambda: Info_employee())
Edit_Employee_btn = customtkinter.CTkButton(a, image=Edit_Employee_icon, text='EDIT EMPLOYEE', compound='top',
                                            height=170, width=150, command=lambda: Edit_employee())
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

login()
a.protocol("WM_DELETE_WINDOW", QUIT)
a.mainloop()
