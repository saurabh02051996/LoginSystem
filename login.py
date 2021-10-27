from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

root=Tk()
root.title("Login System")
root.geometry("1199x600+100+50")
root.resizable(False,False)


### BG image ##
my_image=ImageTk.PhotoImage(file="images\image.jpg.jpg")
my_image_label=Label(root,image=my_image)
my_image_label.place(x=0,y=0,relwidth=1,relheight=1)

##Login Frame ##
login_frame=Frame(root,bg="sky blue")
login_frame.place(x=150,y=150,height=340,width=500)

## create login function here ##
def login():
    global login
    
    if frame_label2_entry.get()=="" or frame_label3_entry.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif frame_label2_entry.get()!="saurabh" or frame_label3_entry.get()!="kumar":
        messagebox.showerror("Error","Invalid Username/Password",parent=root)
    

    else:
        messagebox.showinfo("Welcome",f"Welcome  {frame_label2_entry.get()}\nYour Password:{ frame_label3_entry.get()}  ",parent=root)


## set label in frame ##
frame_label=Label(login_frame,text="Login Here",font=("Impact",34,"bold"),fg="grey",bg="skyblue")
frame_label.place(x=90,y=30)

frame_label1=Label(login_frame,text="Employee Login Area",font=("Goudy",20,"bold"),fg="grey",bg="skyblue")
frame_label1.place(x=90,y=100)

frame_label2=Label(login_frame,text="Username",font=("goudy",15),fg="grey",bg="skyblue")
frame_label2.place(x=90,y=140)

frame_label2_entry=Entry(login_frame,width=40,bg='lightgrey')
frame_label2_entry.place(x=90,y=170,height=30)


frame_label3=Label(login_frame,text="Password",font=("goudy",15),fg="grey",bg="skyblue")
frame_label3.place(x=90,y=210)

frame_label3_entry=Entry(login_frame,width=40,bg='lightgrey')
frame_label3_entry.place(x=90,y=240,height=30)

## create button for forget password ##
forget_button=Button(login_frame,text="Forget Password ?",cursor="hand2",bd=0,fg="blue",bg="skyblue",width=15)
forget_button.place(x=90,y=280)

## create login button ##
login_button=Button(root,text="Login",command=login,cursor="hand2",fg="grey",bd=0,font=(20),bg="pink",width=15)
login_button.place(x=300,y=470,height=40)


root.mainloop()