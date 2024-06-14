import tkinter as tk
from tkinter import messagebox

# Calculator Logic
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# GUI
class SimpleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.create_widgets()

    def create_widgets(self):
        # Entry for first number
        self.label1 = tk.Label(self.root, text="Enter first number:")
        self.label1.pack(pady=5)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack(pady=5)
        
        # Entry for second number
        self.label2 = tk.Label(self.root, text="Enter second number:")
        self.label2.pack(pady=5)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack(pady=5)
        
        # Operation buttons
        self.add_button = tk.Button(self.root, text="+", command=lambda: self.calculate('add'))
        self.add_button.pack(side='left', padx=10)
        
        self.subtract_button = tk.Button(self.root, text="-", command=lambda: self.calculate('subtract'))
        self.subtract_button.pack(side='left', padx=10)
        
        self.multiply_button = tk.Button(self.root, text="*", command=lambda: self.calculate('multiply'))
        self.multiply_button.pack(side='left', padx=10)
        
        self.divide_button = tk.Button(self.root, text="/", command=lambda: self.calculate('divide'))
        self.divide_button.pack(side='left', padx=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            
            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'subtract':
                result = subtract(num1, num2)
            elif operation == 'multiply':
                result = multiply(num1, num2)
            elif operation == 'divide':
                result = divide(num1, num2)
            
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculatorApp(root)
    root.mainloop()
