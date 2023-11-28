from tkinter import *
import customtkinter
from PIL import Image
import mysql.connector

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

def PlaceOrder():
    TABLE_NUMBER = 0
    cursor.execute('select ORDER_NO from orders')
    if cursor.rowcount == 0:
        NewOrderNumber = 1
    else:
        listOfOrderNumber = list()
        for tuple in cursor:
            for orderNo in tuple:
                listOfOrderNumber.append(orderNo)
        NewOrderNumber = max(listOfOrderNumber) + 1
    for course in courses:
        if course == courses[0]:
            cursor.execute('select * from menu where course = %s',(courses[0],))
            data = cursor.fetchall()
            print(data)
            for APPETIZER in list_of_APPETIZER:
                QUANTITY = APPETIZER[1].get()
                if QUANTITY == '':
                    if APPETIZER[4] != 0:
                        QUANTITY = APPETIZER[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[APPETIZER[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
        elif course == courses[1]:
            cursor.execute('select * from menu where course = %s',(courses[1],))
            data = cursor.fetchall()
            print(data)
            for MAIN in list_of_MAIN:
                QUANTITY = MAIN[1].get()
                if QUANTITY == '':
                    if MAIN[4] != 0:
                        QUANTITY = MAIN[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[MAIN[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
        elif course == courses[2]:
            cursor.execute('select * from menu where course = %s',(courses[2],))
            data = cursor.fetchall()
            print(data)
            for DESSERT in list_of_DESSERT:
                QUANTITY = DESSERT[1].get()
                if QUANTITY == '':
                    if DESSERT[4] != 0:
                        QUANTITY = DESSERT[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[DESSERT[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()
        elif course == courses[3]:
            cursor.execute('select * from menu where course = %s',(courses[3],))
            data = cursor.fetchall()
            print(data)
            for BEVERAGE in list_of_BEVERAGE:
                QUANTITY = BEVERAGE[1].get()
                if QUANTITY == '':
                    if BEVERAGE[4] != 0:
                        QUANTITY = BEVERAGE[4]
                    else:
                        QUANTITY = 0
                        continue
                cursor.execute('INSERT INTO ORDERS(ORDER_NO,MCODE,TABLE_NO,QUANTITY) VALUES\
                        (%s,%s,%s,%s)', (NewOrderNumber, data[BEVERAGE[0]][0], TABLE_NUMBER, QUANTITY))
                db.commit()


def course():
    global list_of_APPETIZER
    global list_of_MAIN
    global list_of_DESSERT
    global list_of_BEVERAGE
    def itemincrement(index,course):
        if course == 'APPETIZER':
            if list_of_APPETIZER[index][1].get() == '':
                if list_of_APPETIZER[index][4] == 0:
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(1))
                    list_of_APPETIZER[index][4] = 1
                else:
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(list_of_APPETIZER[index][4] + 1))
                    list_of_APPETIZER[index][4] += 1
            else:
                n = int(list_of_APPETIZER[index][1].get())
                list_of_APPETIZER[index][1].delete(0,END)
                list_of_APPETIZER[index][1].configure(placeholder_text=str(n+1))
                list_of_APPETIZER[index][4] = n + 1
        elif course == 'MAIN':
            if list_of_MAIN[index][1].get() == '':
                if list_of_MAIN[index][4] == 0:
                    list_of_MAIN[index][1].configure(placeholder_text=str(1))
                    list_of_MAIN[index][4] = 1
                else:
                    list_of_MAIN[index][1].configure(placeholder_text=str(list_of_MAIN[index][4] + 1))
                    list_of_MAIN[index][4] += 1
            else:
                n = int(list_of_MAIN[index][1].get())
                list_of_MAIN[index][1].delete(0,END)
                list_of_MAIN[index][1].configure(placeholder_text=str(n+1))
                list_of_MAIN[index][4] = n + 1
        elif course == 'DESSERT':
            if list_of_DESSERT[index][1].get() == '':
                if list_of_DESSERT[index][4] == 0:
                    list_of_DESSERT[index][1].configure(placeholder_text=str(1))
                    list_of_DESSERT[index][4] = 1
                else:
                    list_of_DESSERT[index][1].configure(placeholder_text=str(list_of_DESSERT[index][4] + 1))
                    list_of_DESSERT[index][4] += 1
            else:
                n = int(list_of_DESSERT[index][1].get())
                list_of_DESSERT[index][1].delete(0,END)
                list_of_DESSERT[index][1].configure(placeholder_text=str(n+1))
                list_of_DESSERT[index][4] = n + 1
        elif course == 'BEVERAGE':
            if list_of_BEVERAGE[index][1].get() == '':
                if list_of_BEVERAGE[index][4] == 0:
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(1))
                    list_of_BEVERAGE[index][4] = 1
                else:
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(list_of_BEVERAGE[index][4] + 1))
                    list_of_BEVERAGE[index][4] += 1
            else:
                n = int(list_of_BEVERAGE[index][1].get())
                list_of_BEVERAGE[index][1].delete(0,END)
                list_of_BEVERAGE[index][1].configure(placeholder_text=str(n+1))
                list_of_BEVERAGE[index][4] = n + 1

    def itemdecrement(index, course):
        list_of_APPETIZER[index][1].configure(state=NORMAL)
        if course == 'APPETIZER':
            if list_of_APPETIZER[index][1].get() == '':
                if list_of_APPETIZER[index][4] == 0:
                    pass
                else:
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(list_of_APPETIZER[index][4] - 1))
                    list_of_APPETIZER[index][4] -= 1
            else:
                if list_of_APPETIZER[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_APPETIZER[index][1].get())
                    list_of_APPETIZER[index][1].delete(0,END)
                    list_of_APPETIZER[index][1].configure(placeholder_text=str(n-1))
                    list_of_APPETIZER[index][4] = n - 1
        elif course == 'MAIN':
            if list_of_MAIN[index][1].get() == '':
                if list_of_MAIN[index][4] == 0:
                    pass
                else:
                    list_of_MAIN[index][1].configure(placeholder_text=str(list_of_MAIN[index][4] - 1))
                    list_of_MAIN[index][4] -= 1
            else:
                if list_of_MAIN[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_MAIN[index][1].get())
                    list_of_MAIN[index][1].delete(0,END)
                    list_of_MAIN[index][1].configure(placeholder_text=str(n-1))
                    list_of_MAIN[index][4] = n - 1
        elif course == 'DESSERT':
            if list_of_DESSERT[index][1].get() == '':
                if list_of_DESSERT[index][4] == 0:
                    pass
                else:
                    list_of_DESSERT[index][1].configure(placeholder_text=str(list_of_DESSERT[index][4] - 1))
                    list_of_DESSERT[index][4] -= 1
            else:
                if list_of_DESSERT[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_DESSERT[index][1].get())
                    list_of_DESSERT[index][1].delete(0,END)
                    list_of_DESSERT[index][1].configure(placeholder_text=str(n-1))
                    list_of_DESSERT[index][4] = n - 1
        elif course == 'BEVERAGE':
            if list_of_BEVERAGE[index][1].get() == '':
                if list_of_BEVERAGE[index][4] == 0:
                    pass
                else:
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(list_of_BEVERAGE[index][4] - 1))
                    list_of_BEVERAGE[index][4] -= 1
            else:
                if list_of_BEVERAGE[index][1].get() == 0:
                    pass
                else:
                    n = int(list_of_BEVERAGE[index][1].get())
                    list_of_BEVERAGE[index][1].delete(0,END)
                    list_of_BEVERAGE[index][1].configure(placeholder_text=str(n-1))
                    list_of_BEVERAGE[index][4] = n - 1

    list_of_APPETIZER = []
    list_of_MAIN = []
    list_of_DESSERT = []
    list_of_BEVERAGE = []

    mainFrame = customtkinter.CTkScrollableFrame(a,width=1284,height=500,corner_radius=0,fg_color='transparent')
    '1284'
    mainFrame.place(relx=0, rely=0.1)
    MainLabel.configure(text="MENU")
    MainLabel.place(rely=0.05, relx=0.5, anchor='center')
    a.geometry('1300x650')
    a.resizable(0,0)
    submit_btn.configure(text='PLACE ORDER', command=lambda: PlaceOrder())
    submit_btn.place(relx=0.87, rely=0.90)

    for course in courses:
        list_of_items = list()
        cursor.execute('select * from menu where course=%s',(course,))
        for record in cursor:
            list_of_items.append(record)

        secondaryFrame = customtkinter.CTkScrollableFrame(master= mainFrame,width=1274,fg_color='transparent',
                                                          height=260,orientation='horizontal',label_text=course)
        secondaryFrame.grid(column=0, row=courses.index(course), pady=(20,0))

        for i in range(len(list_of_items)):
            menu_frame = customtkinter.CTkFrame(secondaryFrame)
            name = list_of_items[i][1]
            name = name.split()
            tempName = ''
            for j in range(len(name)):
                tempName += '_' + name[j]
            name = tempName
            try:
                menu_img = Image.open('images/{}.png'.format(name))
                menu_icon = customtkinter.CTkImage(light_image=menu_img, size=(120,120))
            except:
                try:
                    menu_img = Image.open('images/{}.jpg'.format(name))
                    menu_icon = customtkinter.CTkImage(light_image=menu_img, size=(120,120))
                except:
                    pass

            menu_label = customtkinter.CTkLabel(menu_frame, text=list_of_items[i][1], anchor='center')
            img_label = customtkinter.CTkLabel(menu_frame, image=menu_icon, text=None)
            QuantityFrame = customtkinter.CTkFrame(menu_frame, fg_color='transparent')
            quantityLabel = customtkinter.CTkLabel(QuantityFrame, text='QUANTITY')
            PriceLabel = customtkinter.CTkLabel(QuantityFrame, text='PRICE')
            priceLabel = customtkinter.CTkLabel(QuantityFrame, text='$ ' + str(list_of_items[i][4]))
            quantityEntry = customtkinter.CTkEntry(QuantityFrame, placeholder_text='0', width=80, corner_radius=0)
            incrementButton = customtkinter.CTkButton(QuantityFrame, text='+', width=30, corner_radius=0)
            decrementButton = customtkinter.CTkButton(QuantityFrame, text='-', width=30, corner_radius=0)

            menu_frame.grid(column=i, row=0, padx=(20,20))
            menu_label.grid(column=0, row=0, padx=(20,20),pady=(10,5))
            img_label.grid(column=0, row=1)
            QuantityFrame.grid(column=0, row=2, padx=(20,20), pady=(20,0))
            quantityLabel.grid(column=0, row=0, padx=(0,10))
            decrementButton.grid(column=1, row=0)
            quantityEntry.grid(column=2, row=0)
            incrementButton.grid(column=3, row=0)
            PriceLabel.grid(column=0, row=3, pady=(10,5))
            priceLabel.grid(column=1, row=3, columnspan=3, pady=(10,5))
            if course == courses[0]:
                list_of_APPETIZER.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
            elif course == courses[1]:
                list_of_MAIN.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
            elif course == courses[2]:
                list_of_DESSERT.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
            elif course == courses[3]:
                list_of_BEVERAGE.append([i,quantityEntry,incrementButton,decrementButton,0,list_of_items[i][4]])
    try:
        list_of_APPETIZER[0][2].configure(command=lambda: itemincrement(list_of_APPETIZER[0][0], courses[0]))
        list_of_APPETIZER[0][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[0][0], courses[0]))
        list_of_APPETIZER[1][2].configure(command=lambda: itemincrement(list_of_APPETIZER[1][0], courses[0]))
        list_of_APPETIZER[1][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[1][0], courses[0]))
        list_of_APPETIZER[2][2].configure(command=lambda: itemincrement(list_of_APPETIZER[2][0], courses[0]))
        list_of_APPETIZER[2][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[2][0], courses[0]))
        list_of_APPETIZER[3][2].configure(command=lambda: itemincrement(list_of_APPETIZER[3][0], courses[0]))
        list_of_APPETIZER[3][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[3][0], courses[0]))
        list_of_APPETIZER[4][2].configure(command=lambda: itemincrement(list_of_APPETIZER[4][0], courses[0]))
        list_of_APPETIZER[4][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[4][0], courses[0]))
        list_of_APPETIZER[5][2].configure(command=lambda: itemincrement(list_of_APPETIZER[5][0], courses[0]))
        list_of_APPETIZER[5][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[5][0], courses[0]))
        list_of_APPETIZER[6][2].configure(command=lambda: itemincrement(list_of_APPETIZER[6][0], courses[0]))
        list_of_APPETIZER[6][3].configure(command=lambda: itemdecrement(list_of_APPETIZER[6][0], courses[0]))
    except:
        pass
    try:
        list_of_MAIN[0][2].configure(command=lambda: itemincrement(list_of_MAIN[0][0], courses[1]))
        list_of_MAIN[0][3].configure(command=lambda: itemdecrement(list_of_MAIN[0][0], courses[1]))
        list_of_MAIN[1][2].configure(command=lambda: itemincrement(list_of_MAIN[1][0], courses[1]))
        list_of_MAIN[1][3].configure(command=lambda: itemdecrement(list_of_MAIN[1][0], courses[1]))
        list_of_MAIN[2][2].configure(command=lambda: itemincrement(list_of_MAIN[2][0], courses[1]))
        list_of_MAIN[2][3].configure(command=lambda: itemdecrement(list_of_MAIN[2][0], courses[1]))
        list_of_MAIN[3][2].configure(command=lambda: itemincrement(list_of_MAIN[3][0], courses[1]))
        list_of_MAIN[3][3].configure(command=lambda: itemdecrement(list_of_MAIN[3][0], courses[1]))
        list_of_MAIN[4][2].configure(command=lambda: itemincrement(list_of_MAIN[4][0], courses[1]))
        list_of_MAIN[4][3].configure(command=lambda: itemdecrement(list_of_MAIN[4][0], courses[1]))
        list_of_MAIN[5][2].configure(command=lambda: itemincrement(list_of_MAIN[5][0], courses[1]))
        list_of_MAIN[5][3].configure(command=lambda: itemdecrement(list_of_MAIN[5][0], courses[1]))
        list_of_MAIN[6][2].configure(command=lambda: itemincrement(list_of_MAIN[6][0], courses[1]))
        list_of_MAIN[6][3].configure(command=lambda: itemdecrement(list_of_MAIN[6][0], courses[1]))
    except:
        pass
    try:
        list_of_DESSERT[0][2].configure(command=lambda: itemincrement(list_of_DESSERT[0][0], courses[2]))
        list_of_DESSERT[0][3].configure(command=lambda: itemdecrement(list_of_DESSERT[0][0], courses[2]))
        list_of_DESSERT[1][2].configure(command=lambda: itemincrement(list_of_DESSERT[1][0], courses[2]))
        list_of_DESSERT[1][3].configure(command=lambda: itemdecrement(list_of_DESSERT[1][0], courses[2]))
        list_of_DESSERT[2][2].configure(command=lambda: itemincrement(list_of_DESSERT[2][0], courses[2]))
        list_of_DESSERT[2][3].configure(command=lambda: itemdecrement(list_of_DESSERT[2][0], courses[2]))
        list_of_DESSERT[3][2].configure(command=lambda: itemincrement(list_of_DESSERT[3][0], courses[2]))
        list_of_DESSERT[3][3].configure(command=lambda: itemdecrement(list_of_DESSERT[3][0], courses[2]))
        list_of_DESSERT[4][2].configure(command=lambda: itemincrement(list_of_DESSERT[4][0], courses[2]))
        list_of_DESSERT[4][3].configure(command=lambda: itemdecrement(list_of_DESSERT[4][0], courses[2]))
        list_of_DESSERT[5][2].configure(command=lambda: itemincrement(list_of_DESSERT[5][0], courses[2]))
        list_of_DESSERT[5][3].configure(command=lambda: itemdecrement(list_of_DESSERT[5][0], courses[2]))
        list_of_DESSERT[6][2].configure(command=lambda: itemincrement(list_of_DESSERT[6][0], courses[2]))
        list_of_DESSERT[6][3].configure(command=lambda: itemdecrement(list_of_DESSERT[6][0], courses[2]))
    except:
        pass
    try:
        list_of_BEVERAGE[0][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[0][0], courses[3]))
        list_of_BEVERAGE[0][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[0][0], courses[3]))
        list_of_BEVERAGE[1][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[1][0], courses[3]))
        list_of_BEVERAGE[1][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[1][0], courses[3]))
        list_of_BEVERAGE[2][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[2][0], courses[3]))
        list_of_BEVERAGE[2][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[2][0], courses[3]))
        list_of_BEVERAGE[3][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[3][0], courses[3]))
        list_of_BEVERAGE[3][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[3][0], courses[3]))
        list_of_BEVERAGE[4][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[4][0], courses[3]))
        list_of_BEVERAGE[4][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[4][0], courses[3]))
        list_of_BEVERAGE[5][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[5][0], courses[3]))
        list_of_BEVERAGE[5][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[5][0], courses[3]))
        list_of_BEVERAGE[6][2].configure(command=lambda: itemincrement(list_of_BEVERAGE[6][0], courses[3]))
        list_of_BEVERAGE[6][3].configure(command=lambda: itemdecrement(list_of_BEVERAGE[6][0], courses[3]))
    except:
        pass

a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
#BillWindow.minsize(900,600)
#BillWindow.maxsize(1000,700)
#BillWindow.resizable(0,0)

courses = ['APPETIZER', 'MAIN', 'DESSERT', 'BEVERAGE']

db = mysql.connector.connect(host='localhost', user='root', passwd='1234', auth_plugin='mysql_native_password')

cursor = db.cursor(buffered=True)
cursor.execute('use rms')

submit_btn = customtkinter.CTkButton(a, text='SUBMIT', height=50, font=customtkinter.CTkFont(size=16,weight='bold'))
MainLabel = customtkinter.CTkLabel(a, text="Main Label", font=customtkinter.CTkFont(size=40,),
                                   text_color='#2fa572')
course()
a.mainloop()
