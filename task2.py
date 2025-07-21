import tkinter as tk
import random

# Initial scores
user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper') or \
            (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win! wow!!!!!!!!"
        user_score += 1
    else:
        result = "Computer Wins! ohhhnooo!!!!"
        computer_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")


# GUI setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x350")
window.config(bg="#f0f0f0")

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Score label
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack()

# Buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result display
result_label = tk.Label(window, text="", font=("Arial", 14), bg="#f0f0f0", fg="black")
result_label.pack(pady=20)

window.mainloop()