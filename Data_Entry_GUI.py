#---------------------------------------------------------------#
#   A Simple data entry software made with python.
#   Takes some simple data such as name, city, country, etc.
#   By Malay @ 2020
#   This is the GUI File for the same.
#---------------------------------------------------------------#

# Imorting the modules.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

# Starting the application and adding a title.
win = tk.Tk()
win.title('Data Entry [Test]')

# Declaring the variables.
name = tk.StringVar()
city = tk.StringVar()
country = tk.StringVar()
gender = tk.IntVar()
age = tk.IntVar()

# Declaring the operating function.
def click_ok():
    if gender.get() == 1:
        gender_txt = "Male"
    elif gender.get() == 2:
        gendr_txt = "Female"
    print("---------- Submitted ----------")
    print("Name: " + name.get().upper())
    print("Age: " + str(age.get()))
    print("Gender: " + gender_txt)
    print("City: " + city.get().upper())
    print("Country: " + country.get().upper())
    print("-------------------------------")
    msg.showinfo('Message from Data Entry','Entry Submitted. Can be seen in Terminal')
    form_reset()

def click_cancel():
    msg.showerror('Message from Data Entry','Entry was not submitted!')
    print("### ____ Last Entry Not Submitted! ____ ###")
    form_reset()

def form_reset():
    name.set("")
    age.set("")
    gender = -1
    city.set("")
    country.set("")

# Declaring the GUI elements and placing them.
# <1> Adding labels
name_lb = ttk.Label(win,text = "Name")
name_lb.grid(column=1,row=0,padx=5,pady=5)
age_lb = ttk.Label(win,text = "Age")
age_lb.grid(column=1,row=1,padx=5,pady=5)
gender_lb = ttk.Label(win,text = "Gender")
gender_lb.grid(column=1,row=2,padx=5,pady=5)
city_lb = ttk.Label(win,text = "City")
city_lb.grid(column=1,row=3,padx=5,pady=5)
country_lb = ttk.Label(win,text = "Country")
country_lb.grid(column=1,row=4,padx=5,pady=5)
# <2> Adding textboxs
name_txt = ttk.Entry(win,width=30,textvariable=name)
name_txt.grid(column=3,row=0,padx=5,pady=5)
age_txt = ttk.Entry(win,width=30,textvariable=age)
age_txt.grid(column=3,row=1,padx=5,pady=5)
city_txt = ttk.Entry(win,width=30,textvariable=city)
city_txt.grid(column=3,row=3,padx=5,pady=5)
country_txt = ttk.Entry(win,width=30,textvariable=country)
country_txt.grid(column=3,row=4,padx=5,pady=5)
# <3> Adding the radio button
male_rad = tk.Radiobutton(win,text = "Male",variable=gender,value = 1)
male_rad.grid(column=2,row=2,padx=5,pady=5)
female_rad = tk.Radiobutton(win,text = "Female",variable=gender,value = 2)
female_rad.grid(column=3,row=2,padx=5,pady=5)
# <4> Adding the button
ok_btn = ttk.Button(win, text="Submit",command=click_ok)
ok_btn.grid(column=2,row=5,padx=5,pady=5)
cancel_btn = ttk.Button(win, text="Cancel",command=click_cancel)
cancel_btn.grid(column=3,row=5,padx=5,pady=5)

win.mainloop()