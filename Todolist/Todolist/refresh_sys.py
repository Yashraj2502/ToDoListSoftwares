import datetime
from boxdb.basic_commands import get_elements
from datetime import date
from win10toast import ToastNotifier

notifier = ToastNotifier()

def refresh_reminders(user):
    today = str(date.today())
    today=today.replace("/","-")
    dates=get_elements(user,'Date')
    task=get_elements(user,'Task')
    print("todays date : ", today)
    for i in range(len(dates)):
        if today in dates[i]:
            notifier.show_toast("TODO", task[i], duration = 2)



# from tkcalendar import DateEntry
# import tkinter as tk

# root = tk.Tk()

# class CustomDateEntry(DateEntry):

#     def _select(self, event=None):
#         date = self._calendar.selection_get()
#         if date is not None:
#             self._set_text(date.strftime('%Y-%d-%m'))
#             self.event_generate('<<DateEntrySelected>>')
#         self._top_cal.withdraw()
#         if 'readonly' not in self.state():
#             self.focus_set()

# entry = CustomDateEntry(root)
# entry._set_text(entry._date.strftime('%Y-%d-%m'))
# entry.pack()

# root.mainloop()