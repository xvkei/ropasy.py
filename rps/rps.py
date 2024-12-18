import tkinter as tk
import random
import winsound

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 480
        window_height = 500 

        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        self.root.configure(bg="#ffffff")

        # Title
        self.title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 30, "bold"), bg="#ffffff", fg="#4CAF50")
        self.title_label.pack(pady=20)

        # Score Labels
        self.user_score = 0
        self.highest_streak = 0
        self.current_streak = 0
        self.score_label = tk.Label(root, text=f"Score: {self.user_score} | Highest Streak: {self.highest_streak}", font=("Arial", 18), bg="#ffffff")
        self.score_label.pack(pady=10)

        # Choices Frame
        self.choice_frame = tk.Frame(root, bg="#ffffff")
        self.choice_frame.pack(pady=30)

        # Load and resize images
        self.images = {
            "rock": tk.PhotoImage(file="fist.png").subsample(7, 7),  # Resize image by a factor of 3
            "paper": tk.PhotoImage(file="hand-palm.png").subsample(7, 7),  # Resize image by a factor of 3
            "scissors": tk.PhotoImage(file="scissors.png").subsample(7, 7),  # Resize image by a factor of 3
        }

        # Image Buttons
        self.button_rock = self.create_choice_button("rock")
        self.button_paper = self.create_choice_button("paper")
        self.button_scissors = self.create_choice_button("scissors")

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 20), bg="#ffffff", wraplength=450, anchor="center")
        self.result_label.pack(pady=30)

        # Play Again Button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED, width=15, relief=tk.RAISED, bg="#4CAF50", fg="white", font=("Arial", 18, "bold"))
        self.play_again_button.pack(pady=20)

    def create_choice_button(self, choice):
        image = self.images[choice]
        button = tk.Button(self.choice_frame, image=image, command=lambda: self.play_game(choice), relief=tk.FLAT)
        button.grid(row=0, column=self.choice_index(choice), padx=30)  # Use grid for positioning
        return button

    def play_game(self, user_choice):
        # Play a sound effect for choice
        winsound.PlaySound("click.wav", winsound.SND_FILENAME)

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Highlighting the choices with animation
        self.animate_choice(user_choice, "user")
        self.animate_choice(computer_choice, "computer")

        # Determine the outcome
        result_text = f"Computer chose: {computer_choice.capitalize()}\n"
        if user_choice == computer_choice:
            result_text += "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_score += 1
            self.current_streak += 1
            result_text += "You win!"
        else:
            self.current_streak = 0  # Reset the streak upon loss
            result_text += "Computer wins!"

        # Update highest streak
        if self.current_streak > self.highest_streak:
            self.highest_streak = self.current_streak

        self.score_label.config(text=f"Score: {self.user_score} | Highest Streak: {self.highest_streak}")
        self.result_label.config(text=result_text)
        self.play_again_button.config(state=tk.NORMAL)

        # Disable choice buttons if game has ended
        self.disable_buttons()

    def animate_choice(self, choice, who):
        image = self.images[choice]
        label = tk.Label(self.choice_frame, image=image, relief=tk.FLAT)
        label.place(x=self.choice_frame.winfo_x() + (0 if who == "user" else 170), y=self.choice_frame.winfo_y() + 70)

        # Animation effect
        label.after(400, label.destroy)

    def reset_game(self):
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)
        self.current_streak = 0  # Reset current streak after each game

        # Enable choice buttons
        self.enable_buttons()

    def disable_buttons(self):
        for button in [self.button_rock, self.button_paper, self.button_scissors]:
            button.config(state=tk.DISABLED)

    def enable_buttons(self):
        for button in [self.button_rock, self.button_paper, self.button_scissors]:
            button.config(state=tk.NORMAL)

    def choice_index(self, choice):
        return {"rock": 0, "paper": 1, "scissors": 2}[choice]

root = tk.Tk()
app = RockPaperScissorsGUI(root)
root.mainloop()