from tkinter import *


class Window:
    """Класс окна интерфейса"""
    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x400')
        self.photo = PhotoImage(file="pon.png")
        self.w = Label(self.window, image=self.photo)
        self.w.pack()
        self.window.title("TRANSLATOR PONYMAIKA alpha")
        self.window.resizable(width=False, height=False)
