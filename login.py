import tkinter as tk
from tkinter import ttk

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Here you would normally perform your login validation
    if username == "user" and password == "password":
        result_label.config(text="Login successful!", fg="green")
    else:
        result_label.config(text="Invalid credentials", fg="red")

window = tk.Tk()
window.title("Bank 4 The Future")
window.geometry("350x150")

frame = tk.Frame(window, padx=20, pady=20)
frame.pack()

username_label = tk.Label(frame, text="Username:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(frame, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
