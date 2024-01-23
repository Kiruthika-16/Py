from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Kiruthika' and passwordEntry.get()=='1234':
        messagebox.showinfo('success','welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','please enter correct credentials')
window=Tk()
window.geometry('1280x700+0+0')
window.title('Login System of Student Management System')
window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg='white')
loginFrame.place(x=450,y=150)
logoImage=PhotoImage(file='school.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user1.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='passwords.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)
loginButton=Button(loginFrame,text='login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()