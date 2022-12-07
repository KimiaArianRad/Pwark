from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image


win = Tk()
win.geometry("400x400")
win.resizable(False,False)
win.title('Pwark')
win.configure(bg='white')

##def opensignin():
##   login = Toplevel(win)
##    login.title('ورود')
##    login.geometry("400x200")
##    login.resizable(False,False)
##    login.configure(bg='white')
##    
##
##    entry_username = Entry(login,width = 40) 
##    entry_username.place(relx = 0.3,rely = 0.05)
##    lb_username = Label(login,text = 'username : ')
##    lb_username.place(relx = 0.1,rely = 0.05)
##
##    entry_password = Entry(login,width = 40 ,show = '*')
##    entry_password.place(relx = 0.3,rely = 0.25)
##    lb_password = Label(login,text = 'Password : ')
##    lb_password.place(relx = 0.1 , rely = 0.25)



def mainpage():
   year=Toplevel(win)
   year.title('سال اطلاعات')
   year.geometry('600x400')
   year.resizable(False,False)
   year.configure(bg='white')
   lb=Label(year,text='سال مورد نظر را انتخاب کنيد')
   lb.config(bg='white')
   lb.place(relx=0.7, rely = 0.2)
   win.withdraw()

   def selecttype1400():
       selecttype1400=Toplevel(year)
       selecttype1400.title('انتخاب نوع')
       selecttype1400.geometry('400x300')
       selecttype1400.resizable(False,False)
       selecttype1400.configure(bg='white')
       year.withdraw()


       def selectmonth():            
           selectmonth1400=Toplevel(year)
           selectmonth1400.title('انتخاب نوع')
           selectmonth400.geometry('400x300')
           selectmonth1400.resizable(False,False)
           selectmonth1400.configure(bg='white')
           year.withdraw()           
       
       btn_type1=ttk.Button(selecttype1400, text='ضايعات',command=selectmonth)
       selecttype1400.grid(ipadx=10,ipady=5)
       btn_type1.place(relx=0.3 , rely=0.7)

       btn_type2=ttk.Button(selecttype1400, text='دوباره کاري',command=selectmonth)
       selecttype1400.grid(ipadx=10,ipady=5)
       btn_type2.place(relx=0.3 , rely=0.7)


       btn_backtomainpage=ttk.Button(selecttype1400, text='برگشت به صفحه اصلي',command=mainpage)
       btn_backtomainpage.place(relx=0.3 , rely=0.7)

   def selecttype1401():
       selecttype1401=Toplevel(year)
       selecttype1401.title('انتخاب نوع')
       selecttype1401.grid(ipadx=10,ipady=5)
       selecttype1401.resizable(False,False)
       selecttype1401.configure(bg='white')
       year.withdraw()

       btn_backtomainpage=ttk.Button(selecttype1401, text='برگشت به صفحه اصلي',command=mainpage)
       btn_backtomainpage.place(relx=0.30 , rely=0.7)
       
        

       

   btn_login = ttk.Button(year,text = '1400',command =selecttype1400)
   btn_login.place(relx = 0.8 , rely = 0.3)

   btn_login2 = ttk.Button(year,text = '1401',command =selecttype1401)
   btn_login2.place(relx = 0.8 , rely = 0.4)   
     




##    def login1():
##        try:
##            connection=sqlite3.connect('C:/Users/kimia/Desktop/pu.db')
##            c=connection.cursor()
##            
##
##            db.execute("select username,password from tbllogin where username = '%s' and password = '%s'"
##                     %(entry_username.get(),entry_password.get()))
##
##            for username in c:
##                pass
##            connection.commit()
##            connection.close()
##
##            if userinput[0]==entry_username.get() and userinput[1]==entry_password.get():
##                login.withdraw()
##                profile=Toplevel(login,bg='white')
##                profile.title('صفحه اصلي')
##                profile.geometry("500x500")
##                profile.resizable(False,False)
##
##            else:
##                messagebox.showerror("ERROR" , "wrong username or password")
##                entry_usename.delete(0,End)
##                entry_password.delete(0,End)
##        except:
##            messagebox.showerror("ERROR","wrong username or password!")
##            entry_username.delete(0,End)
##            entry_username.delete(0,End)
            
    

##    btn_sigin=ttk.Button(login,text='Login',command=login1)
##    btn_sigin.place(relx=0.5,rely=0.60)
    #win.withdraw()

##def opensignup():
##    signup=Toplevel(win)
##    signup.title('ساخت حساب کاربري')
##    signup.geometry('400x300')
##    signup.resizable(False,False)
##
##    entry_username=Entry(signup,width=40)
##    entry_username.place(relx=0.3,rely=0.08)
##    lb_username=Label(signup,text='username :')
##    lb_username.place(relx=0.1,rely=0.08)
##
##    entry_password=Entry(signup,width=40,show='*')
##    entry_password.place(relx = 0.3 ,rely = 0.25)
##    lb_password = Label(signup,text = 'password : ')
##    lb_password.place(relx = 0.1 , rely = 0.25)
##
##    entry_rpassword = Entry(signup,width = 40,show = '*')
##    entry_rpassword.place(relx = 0.3,rely = 0.46)
##    lb_rpassword = Label(signup,text = 'Reenter pass :')
##    lb_rpassword.place(relx = 0.1,rely = 0.46)

##    def connectiondb():
##        try:
##            if entry_password.get()== entry_rpassword.get():
##                connection = sqlite3.connect('C:/Users/kimia/Desktop/pu.db')
##                c=connection.cursor()
##                c.execute("insert into tbllogin (username,password) value ('%s' , '%s')"
##                          %(entry_username.get(),entry_password.get()))
##                cinnection.commit()
##                connection.close()
##                messagebox.showinfo("موفق","حساب کاربري با موفقيت ايجاد شد")
##            else:
##                messagebox.showerror("خطا","رمز يکسان نيست")
##                entry_username.delete(0,END)
##                entry_password.delete(0,END)
##                entry_rpassword.delete(0,END)
##        except:
##            messagebox.showerror("خطا","اين حساب کاربري موجود ميباشد!")
##            entry_username.delete(0,END)
##            entry_password.delete(0,END)
##            entry_rpassword.delete(0,END)
##    
##    btn_signup=ttk.Button(signup,text='ايجاد حساب کاربري',command=connectiondb )
##    btn_signup.place(relx=0.37,rely=0.70)

    

##    
##btn_signup=ttk.Button(win,text='ايجاد حساب کاربري',command=opensignup)
##btn_signup.place(relx=0.37,rely=0.75)
    
    



btn_login = ttk.Button(win,text = 'ورود',command =mainpage)
btn_login.place(relx = 0.40,rely = 0.6)


img = ImageTk.PhotoImage(Image.open("C:/Users/kimia/Pictures/LOGO3.jpg"))  # PIL solution

l=Label(image=img)
l.place(relx=0.27,y=0.16)


    

    

win.mainloop()

git remote -v
orgin https://github.com/Kimiaar/Pwark.git

