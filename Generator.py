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

# skopiowane1 = ('a')
# skopiowane2 = ('a')
# skopiowane3 = ('a')

def pokaz():
    global skopiowane1, skopiowane2, skopiowane3, skopiowane4, skopiowane5, skopiowane6, skopiowane7, skopiowane8, skopiowane9, skopiowane10
    skopiowane1 = (random.choice(a_list))
    PrzyciskPok1.config(text=skopiowane1, state='active')
    PrzyciskPok1.pack()
    skopiowane2 = (random.choice(a_list))
    PrzyciskPok2.config(text=skopiowane2, state='active', background='grey')
    PrzyciskPok2.pack()
    skopiowane3 = (random.choice(a_list))
    PrzyciskPok3.config(text=skopiowane3, state='active')
    PrzyciskPok3.pack()
    skopiowane4 = (random.choice(a_list))
    PrzyciskPok4.config(text=skopiowane4, state='active', background='grey')
    PrzyciskPok4.pack()
    skopiowane5 = (random.choice(a_list))
    PrzyciskPok5.config(text=skopiowane5, state='active')
    PrzyciskPok5.pack()
    skopiowane6 = (random.choice(a_list))
    PrzyciskPok6.config(text=skopiowane6, state='active', background='grey')
    PrzyciskPok6.pack()
    skopiowane7 = (random.choice(a_list))
    PrzyciskPok7.config(text=skopiowane7, state='active')
    PrzyciskPok7.pack()
    skopiowane8 = (random.choice(a_list))
    PrzyciskPok8.config(text=skopiowane8, state='active', background='grey')
    PrzyciskPok8.pack()
    skopiowane9 = (random.choice(a_list))
    PrzyciskPok9.config(text=skopiowane9, state='active')
    PrzyciskPok9.pack()
    skopiowane10 = (random.choice(a_list))
    PrzyciskPok10.config(text=skopiowane10, state='active', background='grey')
    PrzyciskPok10.pack()

def skop1():
    global skopiowane1
    pyperclip.copy(skopiowane1)
    messagebox.showinfo('Skopiowano',skopiowane1)
def skop2():
    global skopiowane2
    pyperclip.copy(skopiowane2)
    messagebox.showinfo('Skopiowano',skopiowane2)
def skop3():
    global skopiowane3
    pyperclip.copy(skopiowane3)
    messagebox.showinfo('Skopiowano',skopiowane3)
def skop4():
    global skopiowane4
    pyperclip.copy(skopiowane4)
    messagebox.showinfo('Skopiowano',skopiowane4)
def skop5():
    global skopiowane5
    pyperclip.copy(skopiowane5)
    messagebox.showinfo('Skopiowano',skopiowane5)
def skop6():
    global skopiowane6
    pyperclip.copy(skopiowane6)
    messagebox.showinfo('Skopiowano',skopiowane6)
def skop7():
    global skopiowane7
    pyperclip.copy(skopiowane7)
    messagebox.showinfo('Skopiowano',skopiowane7)
def skop8():
    global skopiowane8
    pyperclip.copy(skopiowane8)
    messagebox.showinfo('Skopiowano',skopiowane8)
def skop9():
    global skopiowane9
    pyperclip.copy(skopiowane9)
    messagebox.showinfo('Skopiowano',skopiowane9)
def skop10():
    global skopiowane10
    pyperclip.copy(skopiowane10)
    messagebox.showinfo('Skopiowano',skopiowane10)

# print(random.choice(a_list))
Przycisk1 = Button(root, text="Generuj", padx=300, pady=20, command=pokaz)
Spacja = Label(root, text=" ", padx=300, pady=5)
Lab1 = Label(root, text="Output:", padx=300, pady=5)

PrzyciskPok1 = Button(root, padx=350, pady=10, command=skop1, state='disabled')
PrzyciskPok2 = Button(root, padx=350, pady=10, command=skop2, state='disabled', background='grey')
PrzyciskPok3 = Button(root, padx=350, pady=10, command=skop3, state='disabled')
PrzyciskPok4 = Button(root, padx=350, pady=10, command=skop4, state='disabled', background='grey')
PrzyciskPok5 = Button(root, padx=350, pady=10, command=skop5, state='disabled')
PrzyciskPok6 = Button(root, padx=350, pady=10, command=skop6, state='disabled', background='grey')
PrzyciskPok7 = Button(root, padx=350, pady=10, command=skop7, state='disabled')
PrzyciskPok8 = Button(root, padx=350, pady=10, command=skop8, state='disabled', background='grey')
PrzyciskPok9 = Button(root, padx=350, pady=10, command=skop9, state='disabled')
PrzyciskPok10 = Button(root, padx=350, pady=10, command=skop10, state='disabled', background='grey')

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