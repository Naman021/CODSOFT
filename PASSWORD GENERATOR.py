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
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 8:
        result_label.config(text="Password length should be at least 8 characters")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    result_label.config(text="Password generated successfully")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root)
password_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()