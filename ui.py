from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import mysql.connector

import employee as e

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


def add_emp_submitbtn():
    MainLabel.place_forget()
    SecondaryLabel.place_forget()
    Name_entry.place_forget()
    Dept_entry.place_forget()
    Salary_entry.place_forget()
    submit_btn.place_forget()
    
    emp_name = Name_entry.get()
    emp_dept = Dept_entry.get()
    emp_sal = Salary_entry.get()
    
    e.add_emp(emp_name,emp_dept,emp_sal)
    MANAGER_EMP()

def add_employee():

    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Name_entry.delete(0, END)
    Dept_entry.delete(0, END)
    Salary_entry.delete(0, END)
    
    MainLabel.configure(text='EMPLOYEE RECRUITMENT')
    SecondaryLabel.configure(text='ENTER EMPLOYEE DETAILS')
    submit_btn.configure(command=lambda: add_emp_submitbtn())
    Left_arrow_btn.configure(command=lambda: MANAGER_EMP())
    Name_entry.configure(placeholder_text="ENTER EMPLOYEE NAME")
    Dept_entry.configure(placeholder_text="ENTER EMPLOYEE DEPARTMENT")
    Salary_entry.configure(placeholder_text="ENTER EMPLOYEE SALARY")
    
    MainLabel.place(relx = 0.5,rely = 0.2,anchor = 'center')
    SecondaryLabel.place(relx = 0.5,rely = 0.3,anchor = 'center')
    Name_entry.place(relx = 0.5,rely = 0.45,anchor = 'center')
    Dept_entry.place(relx = 0.5,rely = 0.58,anchor = 'center')
    Salary_entry.place(relx =0.5,rely = 0.71,anchor = 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)
    submit_btn.place(relx = 0.5,rely=0.85 ,anchor='center')
    
    a.bind('<Return>',lambda event:add_emp_submitbtn())
    
def dismiss_emp_submitbtn():
    EID = EID_entry.get()
    confirm = confirm_entry.get()
    print(EID)
    MainLabel.place_forget()
    SecondaryLabel.place_forget()
    EID_entry.place_forget()
    confirm_entry.place_forget()
    submit_btn.place_forget()
    
    if confirm == 'CONFIRM':
        e.del_emp(EID)
        
    MANAGER_EMP()
        
def dismiss_employee():

    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Left_arrow_btn.place_forget()
    EID_entry.delete(0,END)
    confirm_entry.delete(0,END)
    
    MainLabel.configure(text='EMPLOYEE DISMISSAL')
    SecondaryLabel.configure(text = 'ENTER EMPLOYEE ID TO DISMISS')
    EID_entry.configure(placeholder_text= 'ENTER EID')
    confirm_entry.configure(placeholder_text= 'CONFIRM')
    submit_btn.configure(command= lambda:dismiss_emp_submitbtn())
    Left_arrow_btn.configure(command=lambda:MANAGER_EMP())
    
    MainLabel.place(relx = 0.5,rely = 0.2,anchor = 'center')
    SecondaryLabel.place(relx = 0.5,rely = 0.3,anchor = 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)
    submit_btn.place(relx = 0.5,rely=0.85 ,anchor='center')
    EID_entry.place(relx= 0.5, rely= 0.5,anchor= 'center')
    confirm_entry.place(relx= 0.5,rely= 0.7,anchor= 'center')
    
    a.bind('<Return>',lambda event:dismiss_emp_submitbtn())

def MANAGER_EMP():
    Menu_btn.place_forget()
    Salesman_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()
    MainLabel.place_forget()
    SecondaryLabel.place_forget()
    Name_entry.place_forget()
    Dept_entry.place_forget()
    Salary_entry.place_forget()
    EID_entry.place_forget()
    confirm_entry.place_forget()
    Left_arrow_btn.place_forget()
    submit_btn.place_forget()
    
    Left_arrow_btn.configure(command=lambda:MANAGER())
    
    Add_Employee_btn.place(relx= 0.35,rely= 0.3, anchor= 'center')
    Dismiss_Employee_btn.place(relx = 0.65,rely = 0.3,anchor = 'center')
    Info_Employee_btn.place(relx= 0.35,rely= 0.725, anchor= 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)

def History():
    return

def TABLE():
    global tablelist
    tablelist = list()
    r = -1
    mainFrame = customtkinter.CTkScrollableFrame(a,width=984,height=440,corner_radius=0,fg_color='transparent')
    secondaryFrame = customtkinter.CTkFrame(master= mainFrame,width= 974,fg_color='transparent',height=230)
    
    mainFrame.place(relx= 0,rely=0.1)
    secondaryFrame.grid(pady= (20,0))
    
    for i in range(10):
        if i % 3 == 0:
            r += 1
            frame = customtkinter.CTkFrame(secondaryFrame)
            frame.grid(column=0,row=r,ipadx = 70)
        table_btn = customtkinter.CTkButton(frame,text=str(i+1),height=170,width=150)
        table_btn.grid(column= i%3,row= r,padx = 30,pady= 30)
        tablelist.append(table_btn)
    
def course():
    global mainFrame

    def itemincrement(course, index):
        if course == 'APPETIZER':
            if list_of_entry_APPETIZER[index][1].get() == '':
                if list_of_entry_APPETIZER[index][4] == 0:
                    list_of_entry_APPETIZER[index][1].configure(placeholder_text=str(1))
                    list_of_entry_APPETIZER[index][4] = 1
                else:
                    print(4)
                    list_of_entry_APPETIZER[index][1].configure(placeholder_text=str(list_of_entry_APPETIZER[index][4] + 1))
                    list_of_entry_APPETIZER[index][4] += 1
            else:
                n = int(list_of_entry_APPETIZER[index][1].get())
                list_of_entry_APPETIZER[index][1].delete(0, END)
                list_of_entry_APPETIZER[index][1].configure(placeholder_text=str(n+1))
                list_of_entry_APPETIZER[index][4] = n + 1

        elif course == 'MAIN':
            if list_of_entry_MAIN[index][1].get() == '':
                if list_of_entry_MAIN[index][4] == 0:
                    list_of_entry_MAIN[index][1].configure(placeholder_text=str(1))
                    list_of_entry_MAIN[index][4] = 1
                else:
                    list_of_entry_MAIN[index][1].configure(placeholder_text=str(list_of_entry_MAIN[index][4] + 1))
                    list_of_entry_MAIN[index][4] += 1
            else:
                n = int(list_of_entry_MAIN[index][1].get())
                list_of_entry_MAIN[index][1].delete(0, END)
                list_of_entry_MAIN[index][1].configure(placeholder_text=str(n+1))
                list_of_entry_MAIN[index][4] = n + 1

        elif course == 'DESSERT':
            if list_of_entry_DESSERT[index][1].get() == '':
                if list_of_entry_DESSERT[index][4] == 0:
                    list_of_entry_DESSERT[index][1].configure(placeholder_text=str(1))
                    list_of_entry_DESSERT[index][4] = 1
                else:
                    list_of_entry_DESSERT[index][1].configure(placeholder_text=str(list_of_entry_DESSERT[index][4] + 1))
                    list_of_entry_DESSERT[index][4] += 1
            else:
                n = int(list_of_entry_DESSERT[index][1].get())
                list_of_entry_DESSERT[index][1].delete(0, END)
                list_of_entry_DESSERT[index][1].configure(placeholder_text=str(n+1))
                list_of_entry_DESSERT[index][4] = n + 1

    def itemdecrement(course, index):
        if course == 'APPETIZER':
            if list_of_entry_APPETIZER[index][1].get() == '':
                if list_of_entry_APPETIZER[index][4] == 0:
                    pass
                else:
                    list_of_entry_APPETIZER[index][1].configure(placeholder_text=str(list_of_entry_APPETIZER[index][4] - 1))
                    list_of_entry_APPETIZER[index][4] -= 1
            else:
                if list_of_entry_APPETIZER[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_entry_APPETIZER[index][1].get())
                    list_of_entry_APPETIZER[index][1].delete(0,END)
                    list_of_entry_APPETIZER[index][1].configure(placeholder_text=str(n-1))
                    list_of_entry_APPETIZER[index][4] = n - 1

        elif course == 'MAIN':
            if list_of_entry_MAIN[index][1].get() == '':
                if list_of_entry_MAIN[index][4] == 0:
                    pass
                else:
                    list_of_entry_MAIN[index][1].configure(placeholder_text=str(list_of_entry_MAIN[index][4] - 1))
                    list_of_entry_MAIN[index][4] -= 1
            else:
                if list_of_entry_APPETIZER[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_entry_MAIN[index][1].get())
                    list_of_entry_MAIN[index][1].delete(0, END)
                    list_of_entry_MAIN[index][1].configure(placeholder_text=str(n-1))
                    list_of_entry_MAIN[index][4] = n - 1

        elif course == 'DESSERT':
            if list_of_entry_DESSERT[index][1].get() == '':
                if list_of_entry_DESSERT[index][4] == 0:
                    pass
                else:
                    list_of_entry_DESSERT[index][1].configure(placeholder_text=str(list_of_entry_DESSERT[index][4] - 1))
                    list_of_entry_DESSERT[index][4] -= 1
            else:
                if list_of_entry_APPETIZER[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_entry_DESSERT[index][1].get())
                    list_of_entry_DESSERT[index][1].delete(0, END)
                    list_of_entry_DESSERT[index][1].configure(placeholder_text=str(n-1))
                    list_of_entry_DESSERT[index][4] = n - 1

            
    appetizer_btn.place_forget()
    mainCourse_btn.place_forget()
    dessert_btn.place_forget()
    beverages_btn.place_forget()
    

    list_of_entry_APPETIZER = list()
    list_of_entry_MAIN = list()
    list_of_entry_DESSERT = list()
    list_of_entry_BEVERAGE = list()

    mainFrame = customtkinter.CTkScrollableFrame(a, width=984, height=440, corner_radius=0, fg_color='transparent')
    mainFrame.place(relx= 0,rely=0.1)

    courses = ['APPETIZER', 'MAIN', 'DESSERT', 'BEVERAGE']

    for index in range(len(courses)):
        cursor.execute('select * from menu where course = %s', (courses[index],))
        list_of_items = list()
        for record in cursor:
            list_of_items.append(record)
        secondaryFrame = customtkinter.CTkScrollableFrame(master=mainFrame, label_text=courses[index], width=974, fg_color='transparent', height=230,orientation='horizontal')
        secondaryFrame.grid(row=index, pady=(20, 0))
        Left_arrow_btn.configure(command=lambda: FoodMenu())

        for i in range(len(list_of_items)):
            try:
                menu_frame = customtkinter.CTkFrame(secondaryFrame)

                name=list_of_items[i][1]
                name = name.split()
                tempName=''
                for j in range(len(name)) :
                    tempName += '_' + name[j]
                name = tempName
                try:
                    menu_img = Image.open('images/{}.png'.format(name))
                except:
                    menu_img = Image.open('images/{}.jpg'.format(name))
                menu_icon = customtkinter.CTkImage(light_image= menu_img, size= ((120,120)))

                menu_label = customtkinter.CTkLabel(menu_frame,text=list_of_items[i][1]
                                                    ,anchor= 'center')
                img_label = customtkinter.CTkLabel(menu_frame,image=menu_icon,text= None)
                QuantityFrame = customtkinter.CTkFrame(menu_frame,fg_color='transparent')
                quantityLabel = customtkinter.CTkLabel(QuantityFrame,text = 'QUANTITY',corner_radius= 0)
                quantityEntry = customtkinter.CTkEntry(QuantityFrame,placeholder_text='0',width= 80,corner_radius= 0)
                incrementButton = customtkinter.CTkButton(QuantityFrame,text='+',width= 30,corner_radius= 0)
                decrementButton = customtkinter.CTkButton(QuantityFrame,text='-',width= 30,corner_radius= 0)

                menu_frame.grid(column= i,row= 0,padx= (20,20))
                menu_label.grid(column= 0,row= 0,padx = (20,20))
                img_label.grid(column= 0, row= 1)
                QuantityFrame.grid(column= 0,row= 2,padx = (20,20),pady= 20)
                quantityLabel.grid(column= 0, row= 0,padx= (0,10))
                decrementButton.grid(column= 1,row= 0)
                quantityEntry.grid(column= 2,row= 0)
                incrementButton.grid(column= 3,row= 0)

                if courses[index] == 'APPETIZER':
                    list_of_entry_APPETIZER.append([i, quantityEntry, incrementButton, decrementButton, 0])
                elif courses[index] == 'MAIN':
                    list_of_entry_MAIN.append([i, quantityEntry, incrementButton, decrementButton, 0])
                elif courses[index] == 'DESSERT':
                    list_of_entry_DESSERT.append([i, quantityEntry, incrementButton, decrementButton, 0])
                elif courses[index] == 'BEVERAGE':
                    list_of_entry_BEVERAGE.append([i, quantityEntry, incrementButton, decrementButton, 0])

            except:
                pass
    try:
        list_of_entry_APPETIZER[0][2].configure(command=lambda: itemincrement('APPETIZER', 0))
        list_of_entry_APPETIZER[0][3].configure(command=lambda: itemdecrement('APPETIZER', 0))
        list_of_entry_APPETIZER[1][2].configure(command=lambda: itemincrement('APPETIZER', 1))
        list_of_entry_APPETIZER[1][3].configure(command=lambda: itemdecrement('APPETIZER', 1))
        list_of_entry_APPETIZER[2][2].configure(command=lambda: itemincrement('APPETIZER', 2))
        list_of_entry_APPETIZER[2][3].configure(command=lambda: itemdecrement('APPETIZER', 2))
        list_of_entry_APPETIZER[3][2].configure(command=lambda: itemincrement('APPETIZER', 3))
        list_of_entry_APPETIZER[3][3].configure(command=lambda: itemdecrement('APPETIZER', 3))
        list_of_entry_APPETIZER[4][2].configure(command=lambda: itemincrement('APPETIZER', 4))
        list_of_entry_APPETIZER[4][3].configure(command=lambda: itemdecrement('APPETIZER', 4))
        list_of_entry_APPETIZER[5][2].configure(command=lambda: itemincrement('APPETIZER', 5))
        list_of_entry_APPETIZER[5][3].configure(command=lambda: itemdecrement('APPETIZER', 5))
        list_of_entry_APPETIZER[6][2].configure(command=lambda: itemincrement('APPETIZER', 6))
        list_of_entry_APPETIZER[6][3].configure(command=lambda: itemdecrement('APPETIZER', 6))
        list_of_entry_APPETIZER[7][2].configure(command=lambda: itemincrement('APPETIZER', 7))
        list_of_entry_APPETIZER[7][3].configure(command=lambda: itemdecrement('APPETIZER', 7))
    except:
        pass
    try:
        list_of_entry_MAIN[0][2].configure(command=lambda: itemincrement('MAIN', 0))
        list_of_entry_MAIN[0][3].configure(command=lambda: itemdecrement('MAIN', 0))
        list_of_entry_MAIN[1][2].configure(command=lambda: itemincrement('MAIN', 1))
        list_of_entry_MAIN[1][3].configure(command=lambda: itemdecrement('MAIN', 1))
        list_of_entry_MAIN[2][2].configure(command=lambda: itemincrement('MAIN', 2))
        list_of_entry_MAIN[2][3].configure(command=lambda: itemdecrement('MAIN', 2))
        list_of_entry_MAIN[3][2].configure(command=lambda: itemincrement('MAIN', 3))
        list_of_entry_MAIN[3][3].configure(command=lambda: itemdecrement('MAIN', 3))
        list_of_entry_MAIN[4][2].configure(command=lambda: itemincrement('MAIN', 4))
        list_of_entry_MAIN[4][3].configure(command=lambda: itemdecrement('MAIN', 4))
        list_of_entry_MAIN[5][2].configure(command=lambda: itemincrement('MAIN', 5))
        list_of_entry_MAIN[5][3].configure(command=lambda: itemdecrement('MAIN', 5))
        list_of_entry_MAIN[6][2].configure(command=lambda: itemincrement('MAIN', 6))
        list_of_entry_MAIN[6][3].configure(command=lambda: itemdecrement('MAIN', 6))
        list_of_entry_MAIN[7][2].configure(command=lambda: itemincrement('MAIN', 7))
        list_of_entry_MAIN[7][3].configure(command=lambda: itemdecrement('MAIN', 7))
    except:
        pass
    try:
        list_of_entry_DESSERT[0][2].configure(command=lambda: itemincrement('DESSERT', 0))
        list_of_entry_DESSERT[0][3].configure(command=lambda: itemdecrement('DESSERT', 0))
        list_of_entry_DESSERT[1][2].configure(command=lambda: itemincrement('DESSERT', 1))
        list_of_entry_DESSERT[1][3].configure(command=lambda: itemdecrement('DESSERT', 1))
        list_of_entry_DESSERT[2][2].configure(command=lambda: itemincrement('DESSERT', 2))
        list_of_entry_DESSERT[2][3].configure(command=lambda: itemdecrement('DESSERT', 2))
        list_of_entry_DESSERT[3][2].configure(command=lambda: itemincrement('DESSERT', 3))
        list_of_entry_DESSERT[3][3].configure(command=lambda: itemdecrement('DESSERT', 3))
        list_of_entry_DESSERT[4][2].configure(command=lambda: itemincrement('DESSERT', 4))
        list_of_entry_DESSERT[4][3].configure(command=lambda: itemdecrement('DESSERT', 4))
        list_of_entry_DESSERT[5][2].configure(command=lambda: itemincrement('DESSERT', 5))
        list_of_entry_DESSERT[5][3].configure(command=lambda: itemdecrement('DESSERT', 5))
        list_of_entry_DESSERT[6][2].configure(command=lambda: itemincrement('DESSERT', 6))
        list_of_entry_DESSERT[6][3].configure(command=lambda: itemdecrement('DESSERT', 6))
        list_of_entry_DESSERT[7][2].configure(command=lambda: itemincrement('DESSERT', 7))
        list_of_entry_DESSERT[7][3].configure(command=lambda: itemdecrement('DESSERT', 7))
    except:
        pass
    try:
        list_of_entry_BEVERAGE[0][2].configure(command=lambda: itemincrement('BEVERAGE', 0))
        list_of_entry_BEVERAGE[0][3].configure(command=lambda: itemdecrement('BEVERAGE', 0))
        list_of_entry_BEVERAGE[1][2].configure(command=lambda: itemincrement('BEVERAGE', 1))
        list_of_entry_BEVERAGE[1][3].configure(command=lambda: itemdecrement('BEVERAGE', 1))
        list_of_entry_BEVERAGE[2][2].configure(command=lambda: itemincrement('BEVERAGE', 2))
        list_of_entry_BEVERAGE[2][3].configure(command=lambda: itemdecrement('BEVERAGE', 2))
        list_of_entry_BEVERAGE[3][2].configure(command=lambda: itemincrement('BEVERAGE', 3))
        list_of_entry_BEVERAGE[3][3].configure(command=lambda: itemdecrement('BEVERAGE', 3))
        list_of_entry_BEVERAGE[4][2].configure(command=lambda: itemincrement('BEVERAGE', 4))
        list_of_entry_BEVERAGE[4][3].configure(command=lambda: itemdecrement('BEVERAGE', 4))
        list_of_entry_BEVERAGE[5][2].configure(command=lambda: itemincrement('BEVERAGE', 5))
        list_of_entry_BEVERAGE[5][3].configure(command=lambda: itemdecrement('BEVERAGE', 5))
        list_of_entry_BEVERAGE[6][2].configure(command=lambda: itemincrement('BEVERAGE', 6))
        list_of_entry_BEVERAGE[6][3].configure(command=lambda: itemdecrement('BEVERAGE', 6))
        list_of_entry_BEVERAGE[7][2].configure(command=lambda: itemincrement('BEVERAGE', 7))
        list_of_entry_BEVERAGE[7][3].configure(command=lambda: itemdecrement('BEVERAGE', 7))
    except:
        pass

def FoodMenu():
    try:
        Menu_btn.place_forget()
        Salesman_btn.place_forget()
        Order_history_btn.place_forget()
        LogOut_btn.place_forget()
        mainFrame.place_forget()
    except:
        pass
    
    mainCourse_btn.configure(command= lambda:course('MAIN'))
    appetizer_btn.configure(command= lambda:course('APPETIZER'))
    dessert_btn.configure(command= lambda:course('DESSERT'))
    beverages_btn.configure(command= lambda:course('BEVERAGE'))
    Left_arrow_btn.configure(command= lambda:MANAGER())
    
    mainCourse_btn.place(relx = 0.65,rely = 0.3,anchor = 'center')
    appetizer_btn.place(relx= 0.35,rely= 0.3, anchor= 'center')
    dessert_btn.place(relx= 0.35,rely= 0.725, anchor= 'center')
    beverages_btn.place(relx= 0.65,rely= 0.725, anchor= 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)

def MANAGER():
    id_entry.place_forget()
    pass_entry.place_forget()
    MainLabel.place_forget()
    Left_arrow_btn.place_forget()
    submit_btn.place_forget()
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Left_arrow_btn.place_forget()
    appetizer_btn.place_forget()
    mainCourse_btn.place_forget()
    dessert_btn.place_forget()
    beverages_btn.place_forget()
    
    Salesman_btn.configure(command = lambda:MANAGER_EMP())
    LogOut_btn.configure(command= lambda:login())
    
    Salesman_btn.place(relx = 0.65,rely = 0.3,anchor = 'center')
    Menu_btn.place(relx= 0.35,rely= 0.3, anchor= 'center')
    Order_history_btn.place(relx= 0.35,rely= 0.725, anchor= 'center')
    LogOut_btn.place(relx= 0.65,rely= 0.725, anchor= 'center')

def EMPLOYEE():
    id_entry.place_forget()
    pass_entry.place_forget()
    MainLabel.place_forget()
    submit_btn.place_forget()
    Left_arrow_btn.place_forget()
    Menu_btn.place_forget()
    
    #UpperFrame = customtkinter.CTkFrame(a,width = 100, height = 100)
    Left_arrow_btn.configure(command= lambda:login_btn())
    
    #UpperFrame.place(relx=0,rely=0,relwidth = 2,relheight = 0.11)
    Left_arrow_btn.place(relx=0.025,rely=0.03)

def submitbtn():
    global incorrectIdLabel
    global incorrectPassLabel
    
    ID_ENTERED = id_entry.get()
    PASS_ENTERED = pass_entry.get()
    
    cursor.execute('select EID,PASS,USER from employee')
    for record in cursor:
        if str(record[0]) == ID_ENTERED:
            if record[2] == 'MANAGER':
                MANAGER()
            elif record[2] == 'EMPLOYEE':
                EMPLOYEE()
    
def login_btn():
    global id_entry
    global pass_entry
    global submit_btn
    
    Manager_btn.place_forget()
    Salesman_btn.place_forget()
    Menu_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()
    MainLabel.place_forget()
    id_entry.delete(0,END)
    pass_entry.delete(0,END)
        
    MainLabel.configure(text = "Enter Login credentials")
    Left_arrow_btn.configure(command= lambda:login())
    id_entry.configure(placeholder_text='ENTER YOUR EMPLOYEE ID')
    pass_entry.configure(placeholder_text='ENTER YOUR PASSWORD')
    
    id_entry.place(relx=0.5, rely=0.4, anchor='center')
    pass_entry.place(relx=0.5, rely=0.52, anchor='center')
    submit_btn.place(relx=0.5, rely=0.7, anchor='center')
    Left_arrow_btn.place(relx=0.025, rely=0.03)
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')
    
    a.bind('<Return>',lambda event:submitbtn())

def login():
    
    id_entry.place_forget()
    pass_entry.place_forget()
    submit_btn.place_forget()
    Menu_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()
    Left_arrow_btn.place_forget()
    
    MainLabel.configure(text="Welcome to Restaurant Management System")
    Manager_btn.configure(command= lambda:login_btn())
    Salesman_btn.configure(command= lambda:TABLE())
    
    Manager_btn.place(relx = 0.35,rely = 0.6,anchor = 'center')
    Salesman_btn.place(relx = 0.65,rely = 0.6,anchor = 'center')
    MainLabel.place(rely = 0.2,relx = 0.5,anchor = 'center')
     
    
a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
#a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
#a.minsize(900,600)
#a.maxsize(1000,700)
a.resizable(0,0)

db = mysql.connector.connect(host = 'localhost', user='root',\
                             passwd='1234',\
                             auth_plugin = 'mysql_native_password')

cursor = db.cursor()
cursor.execute('use rms')


Manager_img = Image.open('images/Manager_img.png')
#Salesman_img = Image.open('images/Salesman_img.png')
Menu_img = Image.open('images/menu.png')
appetizer_img = Image.open('images/soup.png')
mainCourse_img = Image.open('images/platter.png')
dessert_img = Image.open('images/ice-cream.png')
beverages_img = Image.open('images/tea-cup.png')
Order_history_img = Image.open('images/Order_history.png')
LogOut_img = Image.open('images/logout.png')
Add_Employee_img = Image.open('images/add_employee.png')
Dismiss_Employee_img = Image.open('images/dismiss_employee.png')
Info_Employee_img = Image.open('images/info_employee.png')
Left_arrow_img = Image.open('images/left-arrow2.png')

Manager_img = Manager_img.resize((120,120))
#Salesman_img = Salesman_img.resize((120,120))
Menu_img = Menu_img.resize((120,120))
appetizer_img = appetizer_img.resize((120,120))
mainCourse_img = mainCourse_img.resize((120,120))
dessert_img = dessert_img.resize((120,120))
beverages_img = beverages_img.resize((120,120))
Order_history_img = Order_history_img.resize((120,120))
LogOut_img = LogOut_img.resize((120,120))
Add_Employee_img = Add_Employee_img.resize((120,120))
Dismiss_Employee_img = Dismiss_Employee_img.resize((120,120))
Info_Employee_img = Info_Employee_img.resize((120,120))
Left_arrow_img = Left_arrow_img.resize((30,30))

Manager_icon = ImageTk.PhotoImage(Manager_img)
#Salesman_icon = ImageTk.PhotoImage(Salesman_img)
Menu_icon = ImageTk.PhotoImage(Menu_img)
appetizer_icon = ImageTk.PhotoImage(appetizer_img)
mainCourse_icon = ImageTk.PhotoImage(mainCourse_img)
dessert_icon = ImageTk.PhotoImage(dessert_img)
beverages_icon = ImageTk.PhotoImage(beverages_img)
Order_history_icon = ImageTk.PhotoImage(Order_history_img)
LogOut_icon = ImageTk.PhotoImage(LogOut_img)
Add_Employee_icon = ImageTk.PhotoImage(Add_Employee_img)
Dismiss_Employee_icon = ImageTk.PhotoImage(Dismiss_Employee_img)
Info_Employee_icon = ImageTk.PhotoImage(Info_Employee_img)
Left_arrow_icon = ImageTk.PhotoImage(Left_arrow_img)


#Manager_btn = customtkinter.CTkButton(a,text = 'Manager',image = Manager_icon,height= 170,width= 150,
  #                                    compound='top',command=None,text_color= 'silver')
                                    
#Salesman_btn = customtkinter.CTkButton(a,text = 'Salesman',image = Salesman_icon,height= 170,width= 150,
 #                                      compound='top',command= None)

Menu_btn = customtkinter.CTkButton(a,text='MENU',image=Menu_icon,compound='top',height= 170,width= 150,
                                   command = lambda:FoodMenu())

appetizer_btn = customtkinter.CTkButton(a,text= 'APPETIZER',image= appetizer_icon,compound='top',height= 170,width= 150,
                                        command = None)

mainCourse_btn = customtkinter.CTkButton(a,text= 'MAIN COURSE',image= mainCourse_icon,compound='top',height= 170,width= 150,
                                         command = None)

dessert_btn = customtkinter.CTkButton(a,text= 'DESSERT',image= dessert_icon,compound='top',height= 170,width= 150,
                                      command = None)

beverages_btn = customtkinter.CTkButton(a,text= 'BEVERAGES',image= beverages_icon,compound='top',height= 170,width= 150,
                                        command = None)

Order_history_btn = customtkinter.CTkButton(a,image = Order_history_icon,text = 'Order History',height= 170,
                                            width= 150,compound='top',command=lambda:History())

LogOut_btn = customtkinter.CTkButton(a,image=LogOut_icon,text='Log Out',compound='top',height= 170,width= 150,
                                     command = None)

Add_Employee_btn = customtkinter.CTkButton(a,image=Add_Employee_icon,text='RECRUIT EMPLOYEE',compound='top',
                                           height= 170,width= 150,command = lambda:add_employee())
Dismiss_Employee_btn = customtkinter.CTkButton(a,image=Dismiss_Employee_icon,text='DISMISS EMPLOYEE',
                                               compound='top',height= 170,width= 150,
                                               command = lambda:dismiss_employee())
Info_Employee_btn = customtkinter.CTkButton(a,image= Info_Employee_icon,text='EMPLOYEE INFO',compound='top',
                                            height= 170,width= 150,command = None)

Left_arrow_btn = customtkinter.CTkButton(a,image=Left_arrow_icon,text = '',width=40,height=20,
                                         corner_radius=1000,command=None)

MainLabel = customtkinter.CTkLabel(a,text="Main Label",font=customtkinter.CTkFont(size = 40),
                                   text_color='#2fa572')

SecondaryLabel = customtkinter.CTkLabel(a,text="Secondary Label",font=customtkinter.CTkFont(size = 30),
                                        text_color='#2fa572')

id_entry = customtkinter.CTkEntry(a,placeholder_text='ENTER YOUR EMPLOYEE ID',height=50,
                                  font=('halvatica',16),width=300)

pass_entry = customtkinter.CTkEntry(a,placeholder_text='ENTER YOUR PASSWORD',height=50,
                                    font=('halvatica',15),width=300,show= '*')

Name_entry = customtkinter.CTkEntry(a,placeholder_text="ENTER EMPLOYEE NAME",height=50,
                                  font=('halvatica',16),width=300)

Dept_entry = customtkinter.CTkEntry(a,placeholder_text="ENTER EMPLOYEE DEPARTMENT",height=50,
                                    font=('halvatica',16),width=300)

Salary_entry = customtkinter.CTkEntry(a,placeholder_text="ENTER EMPLOYEE SALARY",height=50,
                                      font=('halvatica',16),width=300)

EID_entry = customtkinter.CTkEntry(a,placeholder_text='EID',height=50,
                                   font=('halvatica',16),width=300)

confirm_entry = customtkinter.CTkEntry(a,placeholder_text= 'CONFIRM',height=50,
                                   font=('halvatica',16),width=300)
submit_btn = customtkinter.CTkButton(a,text='SUBMIT',height=50,font = ('halvatica',16,'bold'),
                                     command=lambda:submitbtn())
course()
#login()
a.mainloop()
