from tkinter import *
from tkinter import Menu
import customtkinter
import employee as e
from PIL import ImageTk,Image

'''def l():
    n = event.width
    k = event.height
    home = hc.resize((n,k))
    home_icon = ImageTk.PhotoImage(home)
    m.configure(image = home_icon)'''
    

a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
#a.resizable(0,0)

home = Image.open('images/home.png')
home = home.resize((40,40))
home_icon = ImageTk.PhotoImage(home)

bill = Image.open('images/invoice.png')
bill = bill.resize((40,40))
bill_icon = ImageTk.PhotoImage(bill)


sideBarLeft = Frame(a,bg = "black")
sideBarRight = Frame(a,bg = "red")
upperBar = Frame(a,bg = "yellow")

sideBarLeft.place(relx=0,rely=0.11,relwidth = 0.05,relheight = 1)
upperBar.place(relx=0,rely=0,relwidth = 2,relheight = 0.11)
sideBarRight.place(relx=0.9,rely=0.11,relwidth=1,relheight=1)

home_btn = customtkinter.CTkButton(a,text = 'home',image = home_icon, fg_color = '#fa7954'
                                   ,text_color='#ffffff',hover_color='#ba2000')
bill_btn = customtkinter.CTkButton(a,text = 'invoice',image = bill_icon,fg_color = '#fa7954'
                                   ,hover_color='#ba2000',text_color='#ffffff')
home_btn.place(in_=upperBar,relx = 0.125)
bill_btn.place(in_=upperBar,relx = 0.2)

#print(home_btn.configure())

'''m = Menu(a)
f = Menu(m,tearoff = 0)
m.add_cascade(label = "home",image= home_icon,menu = f)
f.add_command(label='Exit',command = a.destroy)'''



'''m=Menubutton(a,text = "home",image = home_icon)
m.place(relx=0.5,rely = 0.5)


h = Menu(m)
m.config(menu=h)
#Menu(a).add_cascade(label = 'file',menu = f)
#a.config(menu = m)'''


a.mainloop()
