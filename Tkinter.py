import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("App")
root.geometry("400x400")

Label=tk.Label(root,text="Hello, I am Mirage", font=("Arial",18))
Label.pack(padx=20, pady=20)

textbox=tk.Text(root, height=3, font=("Arial", 14))
textbox.pack(padx=20)


root.mainloop()