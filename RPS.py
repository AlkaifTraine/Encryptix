import tkinter as tk
from tkinter import messagebox
import random
# LOGIC OF GAME
choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
# to make GUI
class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side='left', padx=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side='left', padx=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side='left', padx=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="User: 0  Computer: 0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

    def reset(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="User: 0  Computer: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
