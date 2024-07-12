import re
import tkinter as tk
from tkinter import messagebox

class PasswordChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Complexity Checker")

        self.label = tk.Label(self.root, text="Enter Password:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(self.root, show="*", width=50)
        self.entry.pack(pady=5)

        self.check_button = tk.Button(self.root, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", wraplength=400)
        self.result_label.pack(pady=5)

        self.root.mainloop()

    def check_password(self):
        password = self.entry.get()
        strength, feedback = self.assess_password(password)
        self.result_label.config(text=f"Strength: {strength}\nFeedback: {feedback}")

    def assess_password(self, password):
        if len(password) < 8:
            return "Weak", "Password must be at least 8 characters long."

        strength_criteria = [
            (re.search(r'[A-Z]', password), "Include at least one uppercase letter."),
            (re.search(r'[a-z]', password), "Include at least one lowercase letter."),
            (re.search(r'[0-9]', password), "Include at least one number."),
            (re.search(r'[!@#$%^&*(),.?":{}|<>]', password), "Include at least one special character.")
        ]

        feedback = []
        for criterion, message in strength_criteria:
            if not criterion:
                feedback.append(message)

        if not feedback:
            return "Strong", "Your password is strong."
        elif len(feedback) == 1:
            return "Moderate", "Your password is good but could be improved. " + feedback[0]
        else:
            return "Weak", "Your password is weak. " + " ".join(feedback)

if __name__ == "__main__":
    PasswordChecker()
