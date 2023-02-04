"""
TODO 
LOG IN SYSTEM
"""
import tkinter as tk
from tkinter import ttk, Grid, Label, Button
from tkinter.font import BOLD
from boxdb import specific_auth
from TodoWindow import runner

class App(tk.Tk):
    '''
    Log in class
    1)ui -> __init__
    2)supporting function -> login_system
    '''
    def __init__(self):
        super().__init__()

        self.title('LOG IN')
        self.geometry('300x230')
        # label
        Grid.rowconfigure(self, 10, weight=2)
        Grid.columnconfigure(self, 10, weight=1)
        sign_in_label = Label(self,
                            text='Login',
                            font=("Courier New", 20),
                            foreground="Black",)
        sign_in_label.grid(row=0, column=1, sticky="w")

        ttk.Label(self, text='Username : ').grid(row=7, column=0, sticky='w')
        ttk.Label(self, text='Password : ').grid(row=9, column=0, sticky='w')
        
        username = ttk.Entry(self)
        username.grid(row=7, column=1, sticky='w')
        password = ttk.Entry(self, show='*')
        password .grid(row=9, column=1, sticky='w')
        
        submit_button = Button(self, text="Login", command=lambda: App.login_system(self,username.get(),password.get(),submit_button))
        submit_button.grid(row=10, column=1, sticky='w')
        
        reg_button = Button(self, text="SignUp", command=lambda: App.reg_launch(self))
        reg_button.grid(row=10, column=2, sticky='w')

        self.bind('<Return>', lambda event: App.login_system(self,username.get(),password.get(),submit_button))

    def login_system(self,username,password,button):
        """
        log in system funtion
        """
        if username and password != "":
            if specific_auth('todo_users', ['username', 'password'], [username, password]):
                button.config(bg='green')
                self.destroy()
                runner(username)
            else:
                button.config(bg='red')
        else:
            button.config(bg='red')

    def reg_launch(self):
        from signup_sys import Reg_runner
        self.destroy()
        Reg_runner()
    
def launch_Appwindow():
    '''
    This launch the main page
    '''
    app = App()
    app.mainloop()
