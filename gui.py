from tkinter import *
from tkinter import Menu
import employee as e
from PIL import ImageTk,Image

'''def l():
    n = event.width
    k = event.height
    home = hc.resize((n,k))
    home_icon = ImageTk.PhotoImage(home)
    m.configure(image = home_icon)'''
    

a = Tk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
a.resizable(0,0)

home = Image.open('images/home.png')
home = home.resize((50,50))
home_icon = ImageTk.PhotoImage(home)



sideBarLeft = Frame(a,bg = "black")
sideBarRight = Frame(a,bg = "red")
upperBar = Frame(a,bg = "yellow")

sideBarLeft.place(relx=0,rely=0.11,relwidth = 0.225,relheight = 1)
upperBar.place(relx=0,rely=0,relwidth = 2,relheight = 0.11)
sideBarRight.place(relx=0.9,rely=0.11,relwidth=1,relheight=1)

home_btn = Button(a,image = home_icon)
home_btn.pack()

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