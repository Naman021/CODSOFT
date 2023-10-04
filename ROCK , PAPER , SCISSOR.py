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

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

window = tk.Tk()
window.title("Rock, Paper, Scissors")

title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18))
title_label.pack(pady=10)

instruction_label = tk.Label(
    window, text="Choose your move:", font=("Arial", 12)
)
instruction_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(
    window, text="Scissors", command=lambda: play_game("Scissors")
)

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(window, text="", font=("Arial", 14), pady=10)
result_label.pack()

window.mainloop()