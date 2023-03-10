import tkinter as tk

def on_keyrelease(event,test_list,listbox):
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(test_list,listbox)
    
    
def listbox_update(data,listbox):
    # delete previous data
    listbox.delete(0, 'end')
    
    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')



def searching_for_todo(test_list):
	
	root = tk.Tk()
	listbox = tk.Listbox(root)
	listbox.pack()
	entry = tk.Entry(root)
	entry.pack()
	entry.bind('<KeyRelease>', lambda : on_keyrelease(test_list,listbox))

	#listbox.bind('<Double-Button-1>', on_select)
	listbox.bind('<<ListboxSelect>>', on_select)
	listbox_update(test_list,listbox)

	root.mainloop()

# searching_for_todo(test_list)