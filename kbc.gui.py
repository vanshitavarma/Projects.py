import tkinter as tk
from tkinter import messagebox, simpledialog
import random

questions = [
    "Who is the first Prime Minister of India?",
    "Who wrote the constitution?",
    "When did India get independence?"
]

options = [
    ['Nehru Ji', 'Mahatma Gandhi', 'Babasaheb Ambedkar', 'Lokmanya Tilak'],
    ['Nehru Ji', 'Mahatma Gandhi', 'Babasaheb Ambedkar', 'Lokmanya Tilak'],
    ['2019', '1945', '1967', '1947']
]

answers = ['Nehru Ji', 'Babasaheb Ambedkar', '1947']

lifeline_types = ['x2', 'Experts advice', 'Audience poll']

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("WELCOME TO KBC!!!!")
        self.root.geometry("500x400")
        
        self.q_index = 0
        self.score = 0
        self.used_lifelines = []

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=30, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.lifeline_button = tk.Button(root, text="Use Lifeline", command=self.choose_lifeline)
        self.lifeline_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=5)

        self.show_question()

    def show_question(self):
        if self.q_index >= len(questions):
            self.end_game()
            return

        self.question_label.config(text=questions[self.q_index])
        for i, btn in enumerate(self.buttons):
            btn.config(text=options[self.q_index][i], state=tk.NORMAL)

    def check_answer(self, index):
        selected = self.buttons[index].cget("text")
        correct = answers[self.q_index]

        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct", f"Correct! You've won Rs.{self.score * 10} LAKH")
            self.q_index += 1
            self.show_question()
        else:
            messagebox.showinfo("Wrong", "Galat jawab!!! You take home nothing.")
            self.root.destroy()

    def choose_lifeline(self):
        if len(self.used_lifelines) >= len(lifeline_types):
            messagebox.showwarning("Lifeline", "You have used all available lifelines!")
            return

        available = [ll for ll in lifeline_types if ll not in self.used_lifelines]
        lifeline = simpledialog.askstring("Lifeline", f"Choose a lifeline:\n{', '.join(available)}")

        if lifeline not in available:
            messagebox.showwarning("Invalid", "Invalid or already used lifeline.")
            return

        self.used_lifelines.append(lifeline)

        if lifeline == 'x2':
            self.use_x2()
        elif lifeline == 'Experts advice':
            self.expert_advice()
        elif lifeline == 'Audience poll':
            self.audience_poll()

    def use_x2(self):
        correct = answers[self.q_index]
        current_options = options[self.q_index]
        wrong_options = [opt for opt in current_options if opt != correct]
        to_disable = random.sample(wrong_options, 2)

        for btn in self.buttons:
            if btn.cget("text") in to_disable:
                btn.config(state=tk.DISABLED)
        
        messagebox.showinfo("x2", "Two wrong options removed!")

    def expert_advice(self):
        correct = answers[self.q_index]
        messagebox.showinfo("Expert Advice", f"The expert says: The correct answer is '{correct}'.")

    def audience_poll(self):
        correct = answers[self.q_index]
        poll_result = {}
        for opt in options[self.q_index]:
            if opt == correct:
                poll_result[opt] = random.randint(60, 80)
            else:
                poll_result[opt] = random.randint(5, 20)

        poll_message = "Audience Poll Results:\n\n"
        for opt, percent in poll_result.items():
            poll_message += f"{opt}: {percent}%\n"

        messagebox.showinfo("Audience Poll", poll_message)

    def quit_game(self):
        if self.score == 0:
            messagebox.showinfo("Quit", "You chose to quit. Unfortunately, you take home nothing.")
        else:
            messagebox.showinfo("Quit", f"You chose to quit. You take home Rs.{self.score * 10} LAKH")
        self.root.destroy()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Thanks for playing! You won Rs.{self.score * 10} LAKH")
        self.root.destroy()


# Run the game
root = tk.Tk()
app = KBCGame(root)
root.mainloop()
