import CTkMessagebox
import customtkinter
import mysql.connector
from PIL import Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

def BillPaid(TOTAL):
    ans = CTkMessagebox.CTkMessagebox(title='RMS', message='Payment of $ '+str(TOTAL)+' successful',
                                      icon='check')
    if ans.get() == 'OK':
        BillWindow.destroy()


def PayBills(TABLE_NUMBER):
    BillWindow.geometry('600x500')
    MainLabel = customtkinter.CTkLabel(BillWindow, text="Main Label", font=customtkinter.CTkFont(size=40),
                                       text_color='#2fa572')
    list_of_items = list()
    cursor.execute('select ITEM,QUANTITY,PRICE,PRICE*QUANTITY from ORDERS natural join menu where TABLE_NO=%s',
                   (TABLE_NUMBER,))
    for record in cursor:
        list_of_items.append(record)
    print(list_of_items)
    if list_of_items == []:
        print('No orders')
    else:
        TotalAmount = 0
        secondaryFrame = customtkinter.CTkScrollableFrame(BillWindow, width=574, fg_color='transparent', height=300)
        secondaryFrame.grid(column=0, row=2, columnspan=3, pady=(20, 0))
        for i in range(len(list_of_items)):
            name = list_of_items[i][0]
            name = name.split()
            tempName = ''
            for j in range(len(name)):
                tempName += '_' + name[j]
            name = tempName
            try:
                img = Image.open('images/{}.png'.format(name))
                icon = customtkinter.CTkImage(dark_image=img, size=(50, 50))
            except:
                try:
                    img = Image.open('images/{}.jpg'.format(name))
                    icon = customtkinter.CTkImage(dark_image=img, size=(50, 50))
                except:
                    pass
            name_label = customtkinter.CTkLabel(secondaryFrame, text=list_of_items[i][0], anchor='center')
            img_label = customtkinter.CTkLabel(secondaryFrame, image=icon, text=None, compound='left')
            quantity_label = customtkinter.CTkLabel(secondaryFrame, text=list_of_items[i][1], anchor='center')
            price_label = customtkinter.CTkLabel(secondaryFrame, text='$ ' + str(list_of_items[i][2]), anchor='center')
            amount_label = customtkinter.CTkLabel(secondaryFrame, text='$ ' + str(list_of_items[i][3]), anchor='center')

            name_label.grid(column=1, row=i + 1, padx=(20, 0), pady=(10, 5))
            img_label.grid(column=0, row=i + 1, padx=(20, 0), pady=(10, 5))
            quantity_label.grid(column=3, row=i + 1, padx=(10, 10), pady=(10, 5))
            price_label.grid(column=2, row=i + 1, padx=(10, 10), pady=(10, 5))
            amount_label.grid(column=4, row=i + 1, padx=(0, 0), pady=(10, 5))
            print(name)
            TotalAmount += list_of_items[i][2]
        ItemLabel = customtkinter.CTkLabel(secondaryFrame, text='ITEM NAME', anchor='center', bg_color='#343638')
        PriceLabel = customtkinter.CTkLabel(secondaryFrame, text='PRICE', anchor='center', bg_color='#343638')
        QuantityLabel = customtkinter.CTkLabel(secondaryFrame, text='QUANTITY', anchor='center', bg_color='#343638')
        AmountLabel = customtkinter.CTkLabel(secondaryFrame, text='AMOUNT', anchor='center', bg_color='#343638')
        total_amount_Label = customtkinter.CTkLabel(BillWindow, text='TOTAL AMOUNT', anchor='center',
                                                    font=customtkinter.CTkFont(size=25))
        TotalAmount_Label = customtkinter.CTkLabel(BillWindow, text='$ ' + str(TotalAmount), anchor='center',
                                                   font=customtkinter.CTkFont(family='roman', size=30))
        submit_btn.configure(text='PAY', height=35, command=lambda: BillPaid(TotalAmount))
        MainLabel.configure(text='PAYMENT')

        MainLabel.grid(row=0, column=0, columnspan=3, pady=(20, 0))
        ItemLabel.grid(row=0, column=0, columnspan=2, ipadx=95)
        PriceLabel.grid(row=0, column=2, ipadx=20, padx=(10, 10))
        QuantityLabel.grid(row=0, column=3, ipadx=10, padx=(10, 10))
        AmountLabel.grid(row=0, column=4, ipadx=10, padx=(0, 0))
        total_amount_Label.grid(row=3, column=0, pady=(0, 20), rowspan=2)
        TotalAmount_Label.grid(row=3, column=2)
        submit_btn.grid(row=4, column=2, pady=(20, 0))


BillWindow = customtkinter.CTk()
BillWindow.title('RMS')
BillWindow.geometry('1300x600')
submit_btn = customtkinter.CTkButton(BillWindow, text='SUBMIT', height=50, font=customtkinter.CTkFont(size=15, weight='bold'))

db = mysql.connector.connect(host='localhost', user='root', passwd='1234', auth_plugin='mysql_native_password')
#db = mysql.connector.connect(host='localhost', user='root', passwd='mes123@tirur')
#db = mysql.connector.connect(host='localhost', user='root', passwd='')
cursor = db.cursor(buffered=True)
cursor.execute('create DATABASE IF NOT EXISTS rms')
cursor.execute('use rms')

PayBills(9)

BillWindow.mainloop()

