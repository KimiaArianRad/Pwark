from tkinter import *
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import pathlib, os
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import csv


win = Tk()
win.geometry("1000x680")
win.resizable(False,False)
win.title('Pwark')
##picon=PhotoImage(Image.open("C:/Users/kimia/Picture/imagePwark/123.png"))
##win.iconphoto(False,picon)
title=Frame(win,bg='coral4')
win.configure(bg='black')
img_file_logo="Pwarklogo2.png"
current_dir=pathlib.Path(__file__).parent.resolve()
img_path=os.path.join(current_dir, img_file_logo)
##canvas=tk.Canvas(win)
##canvas.pack()
##img = ImageTk.PhotoImage(file="Pwarklogo2.jpg")
##canvas.create_image(200,300,image=img)
##l=Label(image=img)
##l.config(bg='black')

##l.place(relx=0.29,rely=0.045)

img1 = ImageTk.PhotoImage(Image.open("C:/Users/kimia/Pictures/imagePwark/1.jpg"))
l1=Label(image=img1)
l1.place(relx=0.43,rely=0.92)

img2 = ImageTk.PhotoImage(Image.open("C:/Users/kimia/Pictures/imagePwark/2.jpg"))
l2=Label(image=img2)
l2.place(relx=0.52,rely=0.92)

img3 = ImageTk.PhotoImage(Image.open("C:/Users/kimia/Pictures/imagePwark/line.jpg"))
l3=Label(image=img3)
l3.place(relx=0.28,rely=0.38)
l3.config(bg='black')



def addyear():
   enteryear=Toplevel()
   enteryear.geometry("400x200")
   enteryear.configure(bg='white')
   enteryear.resizable(False,False)
   enteryear.title('ويرايش سال')
   lebel1=Label(enteryear,text='سال جديد را وارد کنيد',bg='white', fg='black')
   lebel1.place(relx=0.34, rely=0.25)
   entry1=Entry(enteryear,width=18)
   entry1.place(relx=0.34,rely=0.4)
   def insertvalue1():
       if entry1.get() not in  data['value']:
          data['value']+=(entry1.get(),)
   b_product=ttk.Button(enterproduct,text='اضافه',command=lambda:insertvalue1())
   b_product.place(relx=0.38,rely=0.6)
    

def addproduct():
   enterproduct=Toplevel()
   enterproduct.geometry("400x200")
   enterproduct.configure(bg='white')
   enterproduct.resizable(False,False)
   enterproduct.title('ويرايش محصولات')
   lebel1=Label(enterproduct,text='محصول جديد را وارد کنيد',bg='white', fg='black')
   lebel1.place(relx=0.34, rely=0.25)
   entry1=Entry(enterproduct,width=18)
   entry1.place(relx=0.34,rely=0.4)
   def insertvalue2():
       if entry1.get() not in  data['value']:
          data['value']+=(entry1.get(),)
   b_product=ttk.Button(enterproduct,text='اضافه',command=lambda:insertvalue2())
   b_product.place(relx=0.38,rely=0.6)
   



menubar= Menu(win)
win.config(menu=menubar)
file_menu=Menu(menubar, tearoff=0)

menubar.add_cascade(label="ويرايش", menu=file_menu)


sub_menu1=Menu(file_menu,tearoff=0)
sub_menu1.add_command(label='اضافه')
sub_menu1.add_command(label='حذف')
file_menu.add_cascade(label="محصول",menu=sub_menu1)

sub_menu2=Menu(file_menu,tearoff=0)
sub_menu2.add_command(label='اضافه')
sub_menu2.add_command(label='حذف')
file_menu.add_cascade(label="سال",menu=sub_menu2)






lyear=Label(win, text='سال مورد نظر را انتخاب کنيد',fg='white', bg='black')
lyear.place(relx=0.7,rely=0.3)

selected_year=tk.StringVar()
yearlist= ttk.Combobox(win, textvariable=selected_year, values=['1400', '1401'], state="reandomly", width=10)
yearlist.place(relx=0.74,rely=0.34)


lmonth=Label(win,text='ماه مورد نظر را انتخاب کنيد', fg='white', bg='black')
lmonth.place(relx=0.40, rely=0.3)

selected_month=tk.StringVar()
monthlist= ttk.Combobox(win, textvariable=selected_month, values=['فروردين', 'ارديبهشت', 'خرداد', 'تير', 'مرداد', 'شهريور', 'مهر', 'آبان', 'آذر', 'دي', 'بهمن', 'اسفند'], state="reandomly", width=15)
monthlist.place(relx=0.42,rely=0.34)


lday=Label(win,text='روز مورد نظر را انتخاب کنيد', fg='white', bg='black')
lday.place(relx=0.13, rely=0.3)

selected_day=tk.StringVar()
daylist= ttk.Combobox(win, textvariable=selected_day, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'                                                              , '27', '28', '29', '30', '31'], state="reandomly", width=10)
daylist.place(relx=0.15,rely=0.34)


ltype=Label(win, text='نوع داده ',fg='white', bg='black')
ltype.place(relx=0.76,rely=0.48)

selected_type=tk.StringVar()
typelist= ttk.Combobox(win, textvariable=selected_type, values=['اضافه کاري', 'دوباره کاري'], state="reandomly", width=15)
typelist.place(relx=0.73,rely=0.52)


lproduct=Label(win, text='انتخاب محصول ',fg='white', bg='black')
lproduct.place(relx=0.74,rely=0.64)

with open ("C:/Users/kimia/Downloads/ListOfProduct.csv", encoding="utf8") as csv_file:
    csv_reader=csv.reader(csv_file)
    data= list(csv_reader)

selected_product=tk.StringVar()
productlist= ttk.Combobox(win, textvariable=selected_product, values=data, state="reandomly", width=31)
productlist.place(relx=0.68,rely=0.68)



l4=Label(win,text='نوع ' ,fg='white', bg='black')
l4.config(text=typelist.get())
l4.place(relx=0.7,rely=0.3)

def page2():    
    secondpage=Toplevel(win)
    secondpage.geometry("600x600")
    secondpage.resizable(False,False)
    secondpage.configure(bg='black')
    secondpage.title('Pwark')
    title=Frame(secondpage,bg='coral4')
    

style=ttk.Style()
style.configure('TButton', background='blue', foreground='black')
style.map('TButton',background=[('active', 'darkorange')], foreground=[('active','darkorange')])
openbutton=ttk.Button(win,text='ورود', command=page2)
openbutton.place(relx=0.46,rely=0.81)
