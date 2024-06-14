import tkinter as tk
from tkinter import messagebox
import random
import string

# generating password
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# to make GUI
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        # Label for password length input
        self.length_label = tk.Label(self.root, text="Enter password length:")
        self.length_label.pack(pady=5)

        # Entry for password length
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.pack(pady=5)

        # Button to generate password
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Label to display the generated password
        self.password_label = tk.Label(self.root, text="")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive")
            if length <8:
                raise ValueError('Password must be of atleast 8 characters')
            password = gen_pass(length)
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
