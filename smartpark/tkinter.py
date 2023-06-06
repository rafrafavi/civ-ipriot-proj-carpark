
import tkinter as tk

class TkinterDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="", width=50, height=5)
        self.label.pack()

    def show_message(self, message):
        self.label.config(text=message)
        self.root.update()

