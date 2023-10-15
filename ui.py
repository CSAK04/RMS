from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import mysql.connector
state = None

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')



def Menu():
    return

def MANAGER():
    id_entry.place_forget()
    pass_entry.place_forget()
    MainLabel.place_forget()
    submit_btn.place_forget()
    
    Salesman_btn.configure(command = None)
    Salesman_btn.place(relx = 0.65,rely = 0.6,anchor = 'center')
    Menu_btn.place(relx= 0.35,rely= 0.6, anchor= 'center')
    return

def EMPLOYEE():
    id_entry.place_forget()
    pass_entry.place_forget()
    MainLabel.place_forget()
    submit_btn.place_forget()
    
    UpperFrame = customtkinter.CTkFrame(a,width = 100, height = 100)
    
    UpperFrame.place(relx=0,rely=0,relwidth = 2,relheight = 0.11)


def submit():
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
        
    MainLabel.configure(text = "Enter Login credentials")
    
    id_entry.place(relx = 0.5,rely = 0.4,anchor = 'center')
    pass_entry.place(relx = 0.5,rely = 0.52,anchor = 'center')
    submit_btn.place(relx = 0.5,rely = 0.7,anchor = 'center')
    
    a.bind('<Return>',lambda event:submit())


def login():
    global MainLabel
    global Manager_btn
    global Salesman_btn
    
    Manager_btn.place(relx = 0.35,rely = 0.6,anchor = 'center')
    Salesman_btn.place(relx = 0.65,rely = 0.6,anchor = 'center')
    MainLabel.place(rely = 0.2,relx = 0.5,anchor = 'center')
     
    
a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
a.minsize(900,600)
a.maxsize(1000,700)
#a.resizable(0,0)

db = mysql.connector.connect(host = 'localhost', user='root',\
                             passwd='1234',\
                             auth_plugin = 'mysql_native_password')

cursor = db.cursor()
cursor.execute('use rms')


Manager_img = Image.open('images/Manager_img.png')
Salesman_img = Image.open('images/Salesman_img.png')
Menu_img = Image.open('images/menu.png')

Manager_img = Manager_img.resize((120,120))
Salesman_img = Salesman_img.resize((120,120))
Menu_img = Menu_img.resize((120,120))

Manager_icon = ImageTk.PhotoImage(Manager_img)
Salesman_icon = ImageTk.PhotoImage(Salesman_img)
Menu_icon = ImageTk.PhotoImage(Menu_img)

Manager_btn = customtkinter.CTkButton(a,text = 'Manager',image = Manager_icon,height= 170,width= 150,
                                    compound='top',command=lambda:login_btn(),text_color= 'silver')
                                    
Salesman_btn = customtkinter.CTkButton(a,text = 'Salesman',image = Salesman_icon,height= 170,width= 150,
                                        compound='top',command=lambda:login_btn())

Menu_btn = customtkinter.CTkButton(a,text='MENU',image=Menu_icon,compound='top',height= 170,width= 150,
                                   command = lambda:Menu)

MainLabel = customtkinter.CTkLabel(a,text="Welcome to Restaurant Management System",
                                font=customtkinter.CTkFont(size = 40),
                                text_color='#2fa572')


id_entry = customtkinter.CTkEntry(a,placeholder_text='ENTER YOUR EMPLOYEE ID',height=50,
                                    font=('halvatica',16),width=300)
pass_entry = customtkinter.CTkEntry(a,placeholder_text='ENTER YOUR PASSWORD',height=50,
                                    font=('halvatica',15),width=300)
submit_btn = customtkinter.CTkButton(a,text='SUBMIT',height=50,font = ('halvatica',16,'bold'),
                                        command=lambda:submit())
            
login()
a.mainloop()
