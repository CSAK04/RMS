from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("learn pop up messages")
#root.iconbitmap('images/download.ico')


# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel

def showinfo_pop():
    ans = messagebox.showinfo("hello", "does this work")
    print(ans)


def showwarning_pop():
    ans = messagebox.showwarning("hello", "does this work")
    print(ans)


def showerror_pop():
    ans = messagebox.showerror("hello", "does this work")
    print(ans)


def askquestion_pop():
    ans = messagebox.askquestion("hello", "does this work")
    print(ans)


def askyesno_pop():
    ans = messagebox.askyesno("hello", "does this work")
    print(ans)


def askokcancel_pop():
    ans = messagebox.askokcancel("hello", "does this work")
    print(ans)


Button(root, command=showinfo_pop, text="Display A show info Popup Message").pack()
Button(root, command=showwarning_pop, text="Display A show warning Popup Message").pack()
Button(root, command=showerror_pop, text="Display A show error Popup Message").pack()
Button(root, command=askquestion_pop, text="Display A ask question Popup Message").pack()
Button(root, command=askyesno_pop, text="Display A ask yes no Popup Message").pack()
Button(root, command=askokcancel_pop, text="Display A ask ok cancel Popup Message").pack()

root.mainloop()