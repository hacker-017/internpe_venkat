import time
import tkinter as tk
import random
from tkinter import ttk

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time,foreground=f"#{random.randint(0, 0xFFFFFF):06x}",background=f"#{random.randint(0, 0xFFFFFF):06x}")
    root.after(1000, update_time)

root = tk.Tk()
root.title("Clock")

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('DS-Digital', 40, 'bold'), background='black', foreground='cyan', anchor='center')
style.map('TLabel', foreground=[('!active', 'cyan'), ('active', 'red')])

label = ttk.Label(root)
label.pack(expand=True)

update_time()

root.mainloop()
