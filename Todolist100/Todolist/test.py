
from boxdb import *

# info={'name':'time'}
# create_project(info)
# create_columns('time',['Date'])
# get_table('todo_users')
# print(specific_auth('todo_users',['username','password'],['yashraj',"1234"]))
# print(auth_details('todo_users',['kshitij',"lucky12","kshitijjathar7@gmail.com"]))
info = {'name':'todo_user'}

# final =get_elements('todo_users','username')
# for i in final:
    # print(create_project({'name':f'{i}'}))
    # create_columns(i,['Task','Date','Status'])

# print(remove_rows('yash','Task','amke'))
get_table("yash")
# update_row("yash","Task","maggie","Status","True")
get_table("yash")
# print(final)
# from tkcalendar import DateEntry
# import tkinter as tk

# root = tk.Tk()

# class CustomDateEntry(DateEntry):

#     def _select(self, event=None):
#         date = self._calendar.selection_get()
#         print(date)
#         if date is not None:
#             print(type(date))
#             self._set_text(date.strftime('%m/%d/%Y'))

#             self.event_generate('<<DateEntrySelected>>')
#         self._top_cal.withdraw()
#         if 'readonly' not in self.state():
#             self.focus_set()

# entry = CustomDateEntry(root)
# entry._set_text(entry._date.strftime('%m/%d/%Y'))
# entry.pack()

# root.mainloop()
# Import Required Library
# coding:utf-8


def write_specific_line(filename,line,content):
    with open(filename, 'r') as file:
        data = file.readlines()

# now change the 2nd line, note that you have to add a newline
    data[line] = content

# and write everything back
    with open(filename, 'w') as file:
        file.writelines( data )
