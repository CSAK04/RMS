from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import mysql.connector
#import employee as e


def QUIT():
    ans = messagebox.askokcancel('rms', 'Do you want to Quit')
    if ans == True:
        a.destroy()


def Add_employee():
    Name_Entry.delete(0, END)
    Sal_Entry.delete(0, END)
    Dept_Entry.delete(0, END)
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Edit_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()

    MainLabel.configure(text='EMPLOYEE RECRUITMENT')
    Name_Entry.configure(placeholder_text='EMPLOYEE NAME')
    Dept_Entry.configure(placeholder_text='DEPARTMENT')
    Sal_Entry.configure(placeholder_text='SALARY')
    Left_arrow_btn.configure(command=lambda: EMPLOYEE())

    Name_Entry.place(relx=0.5, rely=0.45, anchor='center')
    Dept_Entry.place(relx=0.5, rely=0.58, anchor='center')
    Sal_Entry.place(relx=0.5, rely=0.71, anchor='center')
    MainLabel.place(relx=0.5, rely=0.2, anchor='center')

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
    MainLabel.configure(text='EMPLOYEE DISMISSAL')

    Id_Entry.place(relx=0.5, rely=0.4, anchor='center')
    Pass_Entry.place(relx=0.5, rely=0.52, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')

def Edit_employee():
    return
def Info_employee():
    Info_Employee_Frame = customtkinter.CTkFrame(a,width=984,height=440,corner_radius=0,fg_color='transparent')
    Info_Employee_Frame.place(relx= 0,rely=0.1)
    cursor.execute('SELECT ORDER_NO,ITEM,COURSE,PRICE,DATE_TIME FROM ORDERS O,MENU M WHERE O.MCODE = M.MCODE')
    table = list()
    header = ['ORDER NUMBER', 'ITEM', 'COURSE', 'PRICE', 'DATE/TIME']
    for tuple in cursor:
        empList = list(tuple)
        table.append(empList)

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
    LogOut_btn.place_forget()

    Left_arrow_btn.configure(command=lambda: MANAGER())

    Add_Employee_btn.place(relx=0.35, rely=0.3, anchor='center')
    Dismiss_Employee_btn.place(relx=0.65, rely=0.3, anchor='center')
    Info_Employee_btn.place(relx=0.35, rely=0.725, anchor='center')
    Edit_Employee_btn.place(relx=0.65, rely=0.725, anchor='center')
    Left_arrow_btn.place(relx=0.025, rely=0.03)


def LogOut():
    ans = messagebox.askokcancel(title=ENAME, message="Do you want to Log Out")
    if ans == True:
        login()


def WAITER(ENAME):
    Id_Entry.place_forget()
    Pass_Entry.place_forget()

    messagebox.showinfo(title=ENAME, message="Welcome "+ENAME)


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

    Employee_btn.configure(command=lambda: EMPLOYEE())
    LogOut_btn.configure(command=lambda: LogOut())
    Order_history_btn.configure(command=lambda: History())
    Menu_btn.configure(command=lambda: FoodMenu())

    Employee_btn.place(relx=0.65, rely=0.3, anchor='center')
    Menu_btn.place(relx=0.35, rely=0.3, anchor='center')
    Order_history_btn.place(relx=0.35, rely=0.725, anchor='center')
    LogOut_btn.place(relx=0.65, rely=0.725, anchor='center')


def id_format_error():
    try:
        entered_id = int(Id_Entry.get())
        return entered_id
    except:
        messagebox.showerror(title='Try Again', message='INVALID FORMAT FOR AN ID')


def verify_id():
    global ENAME
    global entered_pass
    cursor.execute('select EID,PASS,DEPT,ENAME from employee')
    entered_id = id_format_error()
    entered_pass = Pass_Entry.get()

    for i in cursor:
        if i[0] == int(entered_id):
            if i[1] == entered_pass:
                ENAME = i[3]
                if i[2] == "WAITER":
                    WAITER(i[3])
                if i[2] == "MANAGER":
                    messagebox.showinfo(title=i[3], message="Welcome " + i[3])
                    MANAGER()
            else:
                print('\nIncorrect PASSWORD\nTry Again')
                ans = messagebox.showwarning(title='Try Again', message="Incorrect PASSWORD")
            break
    else:
        messagebox.showerror(title='Try Again', message="An user with this ID doesn't exist")


def login():
    Left_arrow_btn.place_forget()
    Employee_btn.place_forget()
    Menu_btn.place_forget()
    LogOut_btn.place_forget()
    Order_history_btn.place_forget()
    Id_Entry.delete(0, END)
    Pass_Entry.delete(0, END)

    MainLabel.configure(text="Enter Login credentials")
    Id_Entry.configure(placeholder_text='ENTER YOUR EMPLOYEE ID')
    Pass_Entry.configure(placeholder_text='ENTER YOUR PASSWORD')
    submit_btn.configure(command=lambda: verify_id())

    Id_Entry.place(relx=0.5, rely=0.4, anchor='center')
    Pass_Entry.place(relx=0.5, rely=0.52, anchor='center')
    submit_btn.place(relx=0.5, rely=0.7, anchor='center')
    MainLabel.place(rely=0.2, relx=0.5, anchor='center')

    a.bind('<Return>', lambda event: verify_id())
    return


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
Id_Entry = customtkinter.CTkEntry(a, placeholder_text='EMPLOYEE ID', height=50,
                                  font=('halvatica', 16), width=300)

Pass_Entry = customtkinter.CTkEntry(a, placeholder_text='PASSWORD', height=50,
                                    font=('halvatica', 15), width=300, show='*')
submit_btn = customtkinter.CTkButton(a, text='SUBMIT', height=50, font=('halvatica', 16, 'bold'))

Manager_img = Image.open('images/Manager_img.png')
Manager_img = Manager_img.resize((120, 120))
Employee_img = Image.open('images/Employee_img.png')
Employee_img = Employee_img.resize((120, 120))
Order_history_img = Image.open('images/Order_history.png')
LogOut_img = Image.open('images/logout.png')
Order_history_img = Order_history_img.resize((120,120))
LogOut_img = LogOut_img.resize((120,120))
Menu_img = Image.open('images/menu.png')
Menu_img = Menu_img.resize((120,120))
Left_arrow_img = Image.open('images/left-arrow2.png')
Left_arrow_img = Left_arrow_img.resize((30,30))
Add_Employee_img = Image.open('images/add_employee.png')
Dismiss_Employee_img = Image.open('images/dismiss_employee.png')
Info_Employee_img = Image.open('images/info_employee.png')
Add_Employee_img = Add_Employee_img.resize((120,120))
Dismiss_Employee_img = Dismiss_Employee_img.resize((120,120))
Info_Employee_img = Info_Employee_img.resize((120,120))
Edit_Employee_img = Image.open('Images/Edit_employee.png')
Edit_Employee_img = Edit_Employee_img.resize((120, 120))

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
Name_Entry = customtkinter.CTkEntry(a, placeholder_text='EMPLOYEE NAME', height=50,
                                  font=('halvatica', 16), width=300)
Dept_Entry = customtkinter.CTkEntry(a, placeholder_text='DEPARTMENT', height=50,
                                  font=('halvatica', 16), width=300)
Sal_Entry = customtkinter.CTkEntry(a, placeholder_text='SALARY', height=50,
                                  font=('halvatica', 16), width=300)
login()
a.protocol("WM_DELETE_WINDOW", QUIT)
a.mainloop()
