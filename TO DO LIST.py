#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      91850
#
# Created:     04-10-2023
# Copyright:   (c) 91850 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
add_button.pack()
delete_button.pack()

root.mainloop()