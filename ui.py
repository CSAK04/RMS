from tkinter import *
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

def login():
    Manager_img = Image.open('images/Manager_img.png')
    Manager_img = Manager_img.resize((100,100))
    Manager_icon = ImageTk.PhotoImage(Manager_img)
    
    Employee_img = Image.open('images/Employee_img.png')
    Employee_img = Employee_img.resize((100,100))
    Employee_icon = ImageTk.PhotoImage(Employee_img)
    
    
    Manager_btn = customtkinter.CTkButton(a,text = 'Manager',image = Manager_icon
                                          #,text_color='#ffffff',fg_color = '#fa7954',hover_color='#ba2000'
                                          ,compound='top')
                                          
    Employee_btn = customtkinter.CTkButton(a,text = 'Employee',image = Employee_icon
                                            #,hover_color='#ba2000',fg_color = '#fa7954'
                                            ,text_color='#ffffff',compound='top')
    
    MainLabel = customtkinter.CTkLabel(a,text="Welcome to Restaurant Management System")
    
    Manager_btn.place(relx = 0.3,rely = 0.4)
    Employee_btn.place(relx = 0.6,rely = 0.4)
    MainLabel.place(rely = 0.2,)
    
    
a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
#a.resizable(0,0)

login()
a.mainloop()
