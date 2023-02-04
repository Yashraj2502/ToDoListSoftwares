from tkinter import ttk,END
import tkinter as tk
import tkinter.messagebox
import threading

from setuptools import Command
from boxdb import get_elements,remove_rows,update_row
from boxdb.auth_boxdb import chech_rows
from boxdb.basic_commands import add_row
from refresh_sys import refresh_reminders
from tkcalendar import Calendar
from datetime import date
from searching import searching_for_todo

class Todowindow(tk.Tk):
    """
    TODO Todowindow
    """

    def __init__(self,user):
        super().__init__()
        # configure the self window
        self.title('TODO LIST')
        # self.geometry('300x230')
        check_list = get_elements(user,"Task")
        frame_tasks = tkinter.Frame(self)
        frame_tasks.pack()

        listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
        listbox_tasks.pack(side=tkinter.LEFT)

        scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
        scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        ttk.Label(self,text="Tasks : ").place(x=0,y=170)       
        listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=listbox_tasks.yview)

        entry_task = tkinter.Entry(self, width=40,background="light green")
        entry_task.place(x=40,y=170)
        

        # search_ = tkinter.Entry(self, width=20,background="pink")
        # search_.place(x=100,y=150)
        

        today=str(date.today())
        year_,month_,day_=today.split("-")

        cal = Calendar(self, selectmode='day', year=int(year_), month=int(month_), day=int(day_), date_pattern="y-mm-dd")
 
        cal.pack(pady=40)

        button_add_task = tkinter.Button(
            self, text="Add", width=3, command=lambda: Todowindow.add_task(entry_task, listbox_tasks,
            user,cal.get_date()))
        button_add_task.place(x=300,y=170)

        button_delete_task = tkinter.Button(
            self, text="Delete Task", width=48, command=lambda: Todowindow.delete_task(listbox_tasks,user))
        button_delete_task.pack()
        
        complete_task = tkinter.Button(
            self, text="Complete Task", width=48, command=lambda: Todowindow.complete_task(listbox_tasks,user))
        complete_task.pack()
        
        # button_delete_task = tkinter.Button(self, text="Search", width=48,command= lambda: searching_for_todo(check_list))
        # button_delete_task.pack()

        Todowindow.load_tasks(listbox_tasks,user)
        threading.Thread(target=lambda: refresh_reminders(user)).start()



    def add_task(self, listbox_tasks,user,date_):
        """
        Add a task in the list
        """
        task = self.get()
        if task != "":
            print(date_)
            add_row(user,[task,date_,"False"])
            listbox_tasks.insert(tkinter.END, task)
            self.delete(0, tkinter.END)
            task=get_elements(user,'Task')
            Todowindow.load_tasks(listbox_tasks,user)
        else:
            tkinter.messagebox.showwarning(
                title="Warning!", message="You must enter a task.")

    def delete_task(self,user):
        """
        Delete a specific task from the list
        """
        ele=get_elements(user,'Task')
        task_index = self.curselection()[0]
        print(remove_rows(user,'Task',ele[task_index]))
        self.delete(task_index)

  
    def complete_task(self,user):
        ele=get_elements(user,'Task')
        task_index = self.curselection()[0]
        print(task_index)
        print(update_row(user,"Task",ele[task_index],"Status","True\n"))
        Todowindow.load_tasks(self,user)

    def load_tasks(self,user):
        """
        load the user specific task from the file
        """
        self.delete(0,END)
        tasks=get_elements(user,'Task')
        date=get_elements(user,'Date')
        status=get_elements(user,'Status')
        
        showing = [f"{work}     {time}" for work,time in zip(tasks,date)]
        for task in showing:
            self.insert(1,task)
        for i in range(len(status)):
            if status[i]=="True":
                self.itemconfig(i, bg='gray')
        return True

    


  

def runner(user):
    e = Todowindow(user)
    e.mainloop()

# runner("priyanuj")