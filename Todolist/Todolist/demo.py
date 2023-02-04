import tkinter as tk
from tkinter import ttk, Grid, Label, Button
from tkinter import ttk
from tkinter.font import BOLD
from boxdb.basic_commands import add_row

class REGwindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the self window
        self.title('SIGN IN')
        # self.geometry('300x230')

        self.geometry("300x230")
        Grid.rowconfigure(self,10,weight=2)
        Grid.columnconfigure(self,10,weight=1)

        SignInLabel=Label(self,
            text='SIGN IN ',
            font=("Helvetica",20, BOLD),
            foreground="Black",)
        SignInLabel.grid(row=0, column=1, sticky="w")

        ttk.Label(text='Username : ').grid(row=7,column=0,sticky='w')
        ttk.Label(text='Email : ').grid(row=8,column=0,sticky='w')
        ttk.Label(text='Password : ').grid(row=9,column=0,sticky='w')
        username = ttk.Entry(self)
        username.grid(row=7,column=1,sticky='w')
        Email = ttk.Entry(self)
        Email.grid(row=8,column=1,sticky='w')
        password = ttk.Entry(self, show='*')
        password .grid(row=9,column=1,sticky='w')
        submit_button=Button(self, text="show",command=lambda: REGwindow.register_users(self,username.get(),password.get(),Email.get(),submit_button))
        submit_button.grid(row=10,column=1,sticky='w')

    def register_users(self,username,password,Email,submit_button):
        try:
            add_row('todo_users',[username,password,Email])
            submit_button.config(bg='green')
        except Exception:
            submit_button.config(bg='red')
    
def Reg_runner():
    app = REGwindow()
    app.mainloop()