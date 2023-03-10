import tkinter as tk
from tkinter import *

# Initialize tkinter
root = tk.Tk()
# Set system window size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
# Set title name
root.title("Pratik Python Pathshala")
# Add ico file
root.iconbitmap("my_logo-new.ico")


# Show frame if we need to make multiple page
def show_frame(frame):
    frame.tkraise()


# frame 1 code
frame1_title = tk.Label(root, text="Pratik Python "
                        "Pathshala",
                        font=("Helvetica", 52, "bold"),
                        fg="gray").pack()
# Add background image file
img = PhotoImage(file='Login-rafiki.png')

canvas = Canvas(root, width=1200, height=600)
canvas.pack()
canvas.create_image(600, 80, image=img, anchor=NW)

Frame1_login = Frame(root, bg='black')
Frame1_login.place(x=200, y=300, height=340, width=500)
Frame1_title = Label(Frame1_login, text="Login Account",
                     font=("Impact", 35), fg="grey",
                     bg="black")

Frame1_title.place(x=90, y=30)
user = Label(Frame1_login, text="Username",
             fg="gray", font=("Goudy old style",
                        15, "bold"), bg="black")
user.place(x=90, y=120)
txt_user = Entry(Frame1_login, bg="lightgray"
                 , font=("times new roman", 15))
txt_user.place(x=90, y=150, width=350, height=35)
sec_key = Label(Frame1_login, text="Password",
                font=("Goudy old style", 15, "bold"),
                fg="gray", bg="black")
sec_key.place(x=90, y=185)
txt_pass = Entry(Frame1_login, font=("times new roman",
                15), bg="lightgray", show="*")
txt_pass.place(x=90, y=215, width=350, height=35)

Login_btn = tk.Button(Frame1_login, text="Login",
                      fg="black", bg="white",
                      font=("Goudy old style",15,"bold"))
Login_btn.place(x=210, y=280)
root.mainloop()
