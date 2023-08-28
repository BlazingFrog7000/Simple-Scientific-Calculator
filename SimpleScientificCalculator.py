import math
import tkinter as tk
from tkinter import ttk

# Create a Calculator class
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Scientific Calculator 𓆏")
        self.resizable(False, False)
        self.configure(bg="#15362c")
        
        # Create the display entry widget
        self.display = ttk.Entry(self, width=30, font=("Helvetica", 16), justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        
        # Create the buttons
        buttons = [ 
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("^", 5, 3),
            ("(", 6, 0), (")", 6, 1), ("sqrt", 6, 2), ("C", 6, 3)
        ]
          
        self.buttons = []
        for button in buttons:
            text, row, col = button
            btn = ttk.Button(self, text=text, command=lambda text=text: self.button_click(text))
            btn.grid(row=row, column=col, pady=5, padx=5)
            self.buttons.append(btn)
        
    # Button click event handler
    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        elif text == "sqrt":
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, text)
    
# Create an instance of the Calculator class
calculator = Calculator()

# Run the main event loop
calculator.mainloop()