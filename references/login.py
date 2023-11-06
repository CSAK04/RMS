from tkinter import *
data=[{"Id":"01","name":"AMAN_K","pass":"132"},{"id":"69","name":"goutham","pass":"9567377979"}]

def inp_id():
    try:
        in_Id = (e1.get())
        in_pass = int(e2.get())

        for i in range(len(data)):
            print(i)
            if (data[i].get("Id"))==in_Id :
                if int(data[i].get("pass"))==int(in_pass):
                    print("HELLO")
                    in_Id=0
                    l1.destroy()
                    l2.destroy()
                    f1.destroy()
                    f2.destroy()
                    bs.destroy()
            
                    log_in_text = Label(wn,text=data[0].get("name")+" you are logged in",font=("Elephant",23),bg="#7b1d52")
                    log_in_text.grid(column=0,row=0)
                    bl = Button(wn,text="LOG OUT",bg="#228cdc",command=log_out)
                    bl.grid(column=0,row=2,ipadx=50,ipady=10, pady=5)
                else:
                    in_Id=0
                    l1.destroy()
                    l2.destroy()
                    f1.destroy()
                    f2.destroy()
                    bs.destroy()
            
                    log_in_text = Label(wn,text="incorrect password",font=("Elephant",23),bg="#7b1d52")
                    log_in_text.grid(column=0,row=0)
                    bl = Button(wn,text="RETRY",bg="#228cdc",command=log_out)
                    bl.grid(column=0,row=2,ipadx=50,ipady=10, pady=5)
            
    except ValueError:
        l1.destroy()
        l2.destroy()
        f1.destroy()
        f2.destroy()
        bs.destroy()
            
        log_in_text = Label(wn,text="ENTER ID",font=("Elephant",23),bg="#7b1d52")
        log_in_text.grid(column=0,row=0)
        bl = Button(wn,text="RETRY",bg="#228cdc",command=log_out)
        bl.grid(column=0,row=2,ipadx=50,ipady=10, pady=5)
            
    
    
            
def log_out():
    wn.destroy()
    log_in()
    
def log_in():
    global f1
    global f2
    global e1
    global e2
    global l1
    global l2
    global bs
    global wn
    
    wn = Tk()
    wn.title("LOGIN PAGE")
    wn.iconbitmap("download.ico")
    wn.configure(bg="#7b1d52")

    f1 = Frame(wn,border=5)
    f1.grid(column=1,row=0,ipadx=3,padx=(0,5))
    f2 = Frame(wn,border=5)
    f2.grid(column=1,row=1,ipadx=3,padx=(0,5))

    l1 = Label(text="ENTER YOUR ID:",font=("Elephant",23),bg="#7b1d52")
    l1.grid(column=0,row=0)
    l2 = Label(text="ENTER YOUR PASSWORD:",font=("Elephant",23),bg="#7b1d52")
    l2.grid(column=0,row=1)

    e1 = Entry(f1)
    e1.grid(ipady=5)
    e2 = Entry(f2)
    e2.grid(ipady=5)

    bs = Button(wn,text="SUBMIT",command=inp_id,bg="#228cdc")
    bs.grid(column=0,row=2,ipadx=50,ipady=10, pady=5)

    b_quit = Button(wn,text="QUIT",command=wn.destroy,bg="#228cdc")
    b_quit.grid(column=1,row=2,ipadx=50,ipady=10, pady=5)

    wn.mainloop()

log_in()

