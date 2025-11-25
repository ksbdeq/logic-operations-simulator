import tkinter as tk
from tkinter import ttk

switches = []
operation = "И"
num_switches = 2

def update_lamp():
    global switches, operation
    if operation == "И":
        lamp_on = all(switches)
    else:
        lamp_on = any(switches)

    if lamp_on:
        lamp_label.config(text="💡 Лампочка: ВКЛ", foreground="#FFD700")
    else:
        lamp_label.config(text="💡 Лампочка: ВЫКЛ", foreground="#AA0000")

def toggle_switch(index):
    switches[index] = not switches[index]
    btn_list[index].config(text=f"Выключатель {index+1}: {'ON' if switches[index] else 'OFF'}")
    update_lamp()

def create_switches():
    global switches, btn_list, num_switches
    for b in btn_list:
        b.destroy()

    switches = [False] * num_switches
    btn_list = []

    for i in range(num_switches):
        b = tk.Button(window, text=f"Выключатель {i+1}: OFF", width=20, command=lambda i=i: toggle_switch(i))
        b.pack(pady=2)
        btn_list.append(b)

    update_lamp()

def change_operation(event=None):
    global operation
    operation = combo_oper.get()
    update_lamp()

def change_count(event=None):
    global num_switches
    num_switches = int(combo_count.get())
    create_switches()

window = tk.Tk()
window.title("Логические операции И / ИЛИ")
window.geometry("350x450")
window.resizable(False, False)
window.configure(bg="white")

title = tk.Label(window, text="Симуляция логики", font=("Arial", 14), bg="white")
title.pack(pady=10)

lamp_label = tk.Label(window, text="💡 Лампочка: ВЫКЛ", font=("Arial", 16), foreground="#AA0000", bg="white")
lamp_label.pack(pady=10)

combo_count = ttk.Combobox(window, values=[2, 3, 4, 5, 6, 7, 8], state="readonly", width=10)
combo_count.current(0)
combo_count.pack(pady=10)
combo_count.bind("<<ComboboxSelected>>", change_count)

btn_list = []
create_switches()

combo_oper = ttk.Combobox(window, values=["И", "ИЛИ"], state="readonly", width=10)
combo_oper.current(0)
combo_oper.pack(pady=15)
combo_oper.bind("<<ComboboxSelected>>", change_operation)

window.mainloop()