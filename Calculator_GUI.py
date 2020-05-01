# This a script for Calculator with GUI in python.
# By Malay @ 2020
# Must have python installed!

# Importing the modules.
import tkinter as tk
from tkinter import ttk

# Declaring the global variable.
screen_v = ''


def press_num(num):
    global screen_v
    screen_v += str(num)
    screen_var.set(screen_v)


def press_equal():
    global screen_v
    try:
        total = eval(screen_v)
        screen_var.set(str(total))
    except:
        screen_var.set("Error")
    screen_v = str(total)


def clear_scr():
    screen_var.set("")
    global screen_v
    screen_v = ''


# Starting the GUI.
root = tk.Tk()
root.title("Calculator # Malay @ 2020 # (V.1)")
root.geometry("350x200")
root.resizable(False, False)

# Adding screen
screen_var = tk.StringVar()
screen = ttk.Entry(root, width=50, textvariable=screen_var, state="readonly")
screen.grid(column=1, row=1, padx=10, pady=10)

# Adding a frame for buttons.
key_pad = ttk.LabelFrame(root, text="")
key_pad.grid(column=1, row=2, padx=10, pady=10)

# Adding buttons.
btn_0 = ttk.Button(key_pad, text="0", command=lambda: press_num(0))
btn_0.grid(column=2, row=5, padx=2, pady=2)
btn_1 = ttk.Button(key_pad, text="1", command=lambda: press_num(1))
btn_1.grid(column=1, row=2, padx=2, pady=2)
btn_2 = ttk.Button(key_pad, text="2", command=lambda: press_num(2))
btn_2.grid(column=2, row=2, padx=2, pady=2)
btn_3 = ttk.Button(key_pad, text="3", command=lambda: press_num(3))
btn_3.grid(column=3, row=2, padx=2, pady=2)
btn_4 = ttk.Button(key_pad, text="4", command=lambda: press_num(4))
btn_4.grid(column=1, row=3, padx=2, pady=2)
btn_5 = ttk.Button(key_pad, text="5", command=lambda: press_num(5))
btn_5.grid(column=2, row=3, padx=2, pady=2)
btn_6 = ttk.Button(key_pad, text="6", command=lambda: press_num(6))
btn_6.grid(column=3, row=3, padx=2, pady=2)
btn_7 = ttk.Button(key_pad, text="7", command=lambda: press_num(7))
btn_7.grid(column=1, row=4, padx=2, pady=2)
btn_8 = ttk.Button(key_pad, text="8", command=lambda: press_num(8))
btn_8.grid(column=2, row=4, padx=2, pady=2)
btn_9 = ttk.Button(key_pad, text="9", command=lambda: press_num(9))
btn_9.grid(column=3, row=4, padx=2, pady=2)

btn_plus = ttk.Button(key_pad, text="+", command=lambda: press_num("+"))
btn_plus.grid(column=4, row=2)
btn_minus = ttk.Button(key_pad, text="-", command=lambda: press_num("-"))
btn_minus.grid(column=4, row=3)
btn_multiply = ttk.Button(key_pad, text="*", command=lambda: press_num("*"))
btn_multiply.grid(column=4, row=4)
btn_divide = ttk.Button(key_pad, text="/", command=lambda: press_num("/"))
btn_divide.grid(column=4, row=5)
btn_equal = ttk.Button(key_pad, text="=", command=press_equal)
btn_equal.grid(column=3, row=5)
btn_clear = ttk.Button(key_pad, text="<-", command=clear_scr)
btn_clear.grid(column=1, row=5)

root.mainloop()
