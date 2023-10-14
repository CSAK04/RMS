from tkinter import *
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')



def login_btn(user):
    Manager_btn.destroy()
    Employee_btn.destroy()
        
    if user == 'manager':
            MainLabel.configure(text = "Enter Login credentials")
            id_entry = customtkinter.CTkEntry(a,placeholder_text='Enter your id',height=40,width=300)
            pass_entry = customtkinter.CTkEntry(a,placeholder_text='Enter your id',height=40,width=300)
            
            id_entry.place(relx = 0.5,rely = 0.4,anchor = 'center')


def login():
    global MainLabel
    global Manager_btn
    global Employee_btn
    
    Manager_img = Image.open('images/Manager_img.png')
    Manager_img = Manager_img.resize((120,120))
    Manager_icon = ImageTk.PhotoImage(Manager_img)
    
    Employee_img = Image.open('images/Employee_img.png')
    Employee_img = Employee_img.resize((120,120))
    Employee_icon = ImageTk.PhotoImage(Employee_img)
    
    
    Manager_btn = customtkinter.CTkButton(a,text = 'Manager',image = Manager_icon
                                          #,text_color='#ffffff',fg_color = '#fa7954',hover_color='#ba2000'
                                          ,compound='top',command=lambda:login_btn('manager'))
                                          
    Employee_btn = customtkinter.CTkButton(a,text = 'Employee',image = Employee_icon
                                            #,hover_color='#ba2000',fg_color = '#fa7954',text_color='#ffffff'
                                            ,compound='top',command=lambda:login_btn('manager'))
    
    MainLabel = customtkinter.CTkLabel(a,text="Welcome to Restaurant Management System",
                                       font=customtkinter.CTkFont(size = 40),
                                       text_color='#2fa572')
    
    Manager_btn.place(relx = 0.35,rely = 0.6,anchor = 'center')
    Employee_btn.place(relx = 0.65,rely = 0.6,anchor = 'center')
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

login()
a.mainloop()
