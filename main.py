import tkinter
from tkinter import *
from tkinter import ttk
from typing import FrozenSet
from tkinter_custom_button import TkinterCustomButton


def button_function():
    valor = input_text.get()
    # nome_da_funcao(valor)
    print(valor)


app = tkinter.Tk()
app.geometry("1366x750")
app.title("ROBO DO LUISÃO")

C = tkinter.Canvas(app, bg="blue", height=750, width=1366)
filename = tkinter.PhotoImage(file = "C:\\Users\\Vitor Arakaki\\Pictures\\bgitau1.png")
background_label = tkinter.Label(app, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

valor = tkinter.IntVar()
input_text = IntVar()

style = ttk.Style()
style.configure('TEntry', foreground = 'black')

espaco1 = tkinter.Label(app, background="#2e2f37").grid(row=1, pady=150,padx=300,column=1) 
entry1 = ttk.Entry(app, width=9, textvariable = input_text, justify = CENTER, font = ('courier', 15, 'bold')).grid(row=2, padx=300, column=1)
ola = TkinterCustomButton(text="Enviar", bg_color="#181820",fg_color="darkorange", hover_color="orange", text_color="blue", corner_radius=10, command=button_function).grid(row=3, padx=300, pady=30,column=1)
espaco2 = tkinter.Label(app, background="#46474f").grid(row=20, padx=300,column=0)


app.resizable(width=False, height=False)
app.mainloop()
