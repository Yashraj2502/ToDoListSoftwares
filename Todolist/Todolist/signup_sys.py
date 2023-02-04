'''
REGISTER PAGE
'''
from asyncio import tasks
import tkinter as tk
from tkinter import  ttk, Grid, Label, Button
from tkinter.font import BOLD
from boxdb.basic_commands import add_row
from boxdb import create_project,create_columns

class REGwindow(tk.Tk):
    """
    SIGNUP UI
    """
    def __init__(self):
        super().__init__()

        # configure the self window
        self.title('SIGN IN')
        # self.geometry('300x230')

        self.geometry("300x230")
        Grid.rowconfigure(self,10,weight=2)
        Grid.columnconfigure(self,10,weight=1)

        sign_in_label=Label(self,
            text='SIGN IN ',
            font=("Helvetica",20, BOLD),
            foreground="Black",)
        sign_in_label.grid(row=0, column=1, sticky="w")

        ttk.Label(text='Username : ').grid(row=7,column=0,sticky='w')
        ttk.Label(text='Email : ').grid(row=8,column=0,sticky='w')
        ttk.Label(text='Password : ').grid(row=9,column=0,sticky='w')
        username = ttk.Entry(self)
        username.grid(row=7,column=1,sticky='w')
        email = ttk.Entry(self)
        email.grid(row=8,column=1,sticky='w')
        password = ttk.Entry(self, show='*')
        password .grid(row=9,column=1,sticky='w')
        submit_button=Button(self, text="Submit",command=lambda: REGwindow.register_users(self,username.get(),password.get(),email.get(),submit_button))
        submit_button.grid(row=10,column=1,sticky='w')
        
        sign_in_button=Button(self, text="Sign in",command=lambda: REGwindow.Appwindow_launch(self))
        sign_in_button.grid(row=10,column=2,sticky='w')

    def register_users(self,username,password,email,submit_button):
        """
        This function add values to the database
        """
        try:
            add_row('todo_users',[username,password,email])
            create_project({'name':username})
            create_columns(username,["Task"],unique=True)
            create_columns(username,["Date","Status"],unique=False)
            submit_button.config(bg='green')
        except Exception:
            submit_button.config(bg='red')

    def Appwindow_launch(self):
        """
        This window take us to main page
        """
        from log_in_sys import launch_Appwindow
        self.destroy()
        launch_Appwindow()


def Reg_runner():
    """
    Runs the register page
    """
    app = REGwindow()
    app.mainloop()