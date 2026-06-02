from tkinter import *
import sqlite3

con = sqlite3.connect("db1.db")
# con.execute("create table student(name varchar(20),email varchar(50),phone varchar(15))")

root = Tk()
root.geometry("600x600")
root.title("MY APP")
root.configure(bg="#f0f4f8")

def create():
    name = t1.get()
    email = t2.get()
    phone = t3.get()
    con.execute(f"insert into student values('{name}','{email}','{phone}')")
    con.commit()
    print("data inserted")

# Heading
title = Label(
    root,
    text="Registration Form",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
title.pack(pady=20)

# Username
name = Label(
    root,
    text="Username",
    font=("Arial", 11),
    bg="#f0f4f8"
)
name.place(x=100, y=100)

t1 = Entry(
    root,
    font=("Arial", 11),
    width=25,
    bd=2,
    relief="groove"
)
t1.place(x=200, y=100)

# Email
email = Label(
    root,
    text="Email",
    font=("Arial", 11),
    bg="#f0f4f8"
)
email.place(x=100, y=150)

t2 = Entry(
    root,
    font=("Arial", 11),
    width=25,
    bd=2,
    relief="groove"
)
t2.place(x=200, y=150)

# Phone
phone = Label(
    root,
    text="Phone",
    font=("Arial", 11),
    bg="#f0f4f8"
)
phone.place(x=100, y=200)

t3 = Entry(
    root,
    font=("Arial", 11),
    width=25,
    bd=2,
    relief="groove"
)
t3.place(x=200, y=200)

# Submit Button
b = Button(
    root,
    text="Submit",
    width=20,
    font=("Arial", 11, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    cursor="hand2",
    relief="flat",
    command=create
)
b.place(x=200, y=250)

root.mainloop()
