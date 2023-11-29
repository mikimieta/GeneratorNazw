import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

root = Tk()
root.title("Generator nazw")
root.geometry('300x560')

with open('miasta.json', encoding='utf-8') as f:
    a_list = json.load(f)


def pokaz():
    skopiowane1 = (random.choice(a_list))
    PrzyciskPok1.config(text=skopiowane1, state='active', command=lambda: skop(skopiowane1))
    PrzyciskPok1.pack()
    skopiowane2 = (random.choice(a_list))
    PrzyciskPok2.config(text=skopiowane2, state='active', command=lambda: skop(skopiowane2))
    PrzyciskPok2.pack()
    skopiowane3 = (random.choice(a_list))
    PrzyciskPok3.config(text=skopiowane3, state='active', command=lambda: skop(skopiowane3))
    PrzyciskPok3.pack()
    skopiowane4 = (random.choice(a_list))
    PrzyciskPok4.config(text=skopiowane4, state='active', command=lambda: skop(skopiowane4))
    PrzyciskPok4.pack()
    skopiowane5 = (random.choice(a_list))
    PrzyciskPok5.config(text=skopiowane5, state='active', command=lambda: skop(skopiowane5))
    PrzyciskPok5.pack()
    skopiowane6 = (random.choice(a_list))
    PrzyciskPok6.config(text=skopiowane6, state='active', command=lambda: skop(skopiowane6))
    PrzyciskPok6.pack()
    skopiowane7 = (random.choice(a_list))
    PrzyciskPok7.config(text=skopiowane7, state='active', command=lambda: skop(skopiowane7))
    PrzyciskPok7.pack()
    skopiowane8 = (random.choice(a_list))
    PrzyciskPok8.config(text=skopiowane8, state='active', command=lambda: skop(skopiowane8))
    PrzyciskPok8.pack()
    skopiowane9 = (random.choice(a_list))
    PrzyciskPok9.config(text=skopiowane9, state='active', command=lambda: skop(skopiowane9))
    PrzyciskPok9.pack()
    skopiowane10 = (random.choice(a_list))
    PrzyciskPok10.config(text=skopiowane10, state='active', command=lambda: skop(skopiowane10))
    PrzyciskPok10.pack()

def skop(nazwa):
    pyperclip.copy(nazwa)
    messagebox.showinfo('Skopiowano', nazwa)

# print(random.choice(a_list))
Przycisk1 = Button(root, text="Generuj", padx=300, pady=20, command=pokaz)
Spacja = Label(root, text=" ", padx=300, pady=5)
Lab1 = Label(root, text="Output:", padx=300, pady=5)

PrzyciskPok1 = Button(root, padx=350, pady=10, state='disabled')
PrzyciskPok2 = Button(root, padx=350, pady=10, state='disabled', background='grey')
PrzyciskPok3 = Button(root, padx=350, pady=10, state='disabled')
PrzyciskPok4 = Button(root, padx=350, pady=10, state='disabled', background='grey')
PrzyciskPok5 = Button(root, padx=350, pady=10, state='disabled')
PrzyciskPok6 = Button(root, padx=350, pady=10, state='disabled', background='grey')
PrzyciskPok7 = Button(root, padx=350, pady=10, state='disabled')
PrzyciskPok8 = Button(root, padx=350, pady=10, state='disabled', background='grey')
PrzyciskPok9 = Button(root, padx=350, pady=10, state='disabled')
PrzyciskPok10 = Button(root, padx=350, pady=10, state='disabled', background='grey')

Przycisk1.pack()
Spacja.pack()
Lab1.pack()

PrzyciskPok1.pack()
PrzyciskPok2.pack()
PrzyciskPok3.pack()
PrzyciskPok4.pack()
PrzyciskPok5.pack()
PrzyciskPok6.pack()
PrzyciskPok7.pack()
PrzyciskPok8.pack()
PrzyciskPok9.pack()
PrzyciskPok10.pack()


root.mainloop()