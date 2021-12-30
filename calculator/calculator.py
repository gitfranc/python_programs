# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: calculator.py
# @Date: 2021-12-30 21:57:59
# @Last Modified by: franc
# @Last Modified time: 2021-12-31 00:30:11
# @Project: calculator
# @Use: The main function of Calculator

from tkinter import Tk
from tkinter import Label, Button
from tkinter import StringVar
import math

from settings import Settings


def show(button_string):
    content = result.get()
    if content == "0":
        content = ""
    result.set(content + button_string)

def clear_ce():
    result.set("0")

def clear():
    result.set("0")


def backspace():
    result.set(result.get()[:-1])

def reciprocal():

    res = eval("1"+"/"+ result.get())
    result.set(str(res))

def square():
    res = eval(result.get() + "**" + "2")
    result.set(str(res))

def sqrt2():
    res = math.sqrt(int(result.get()))
    result.set(str(res))

def calculate():
    res = eval(result.get())
    result.set(result.get()+ " = \n" + str(res))

def pos_neg():
    global msg_on
    res = eval(result.get())
    if res >= 0:
        result.set("-"+result.get())
    else:
        res_neg = abs(res)
        result.set(str(abs(res)))






def cal_result_and_button(root, result):

    # Display the result of calculation
    result_label = Label(root, width=30, height=2, relief="sunken", anchor="se",
                         textvariable=result)
    result_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    # Display the button of calculator
    Button(root, text="%", width=settings.widget_width,
            command=lambda:show("%")).grid(row=1,column=0)
    Button(root, text="CE", width=settings.widget_width,
            command=clear_ce).grid(row=1, column=1)
    Button(root, text="C", width=settings.widget_width,
            command=clear).grid(row=1, column=2)
    Button(root, text="DEL", width=settings.widget_width,
            command=backspace).grid(row=1, column=3)

    # row = 2
    Button(root, text="1/x", width=settings.widget_width,
            command=reciprocal).grid(row=2, column=0)
    Button(root, text="x^2", width=settings.widget_width,
            command=square).grid(row=2, column=1)
    Button(root, text="sqrt2", width=settings.widget_width,
            command=sqrt2).grid(row=2, column=2)
    Button(root, text="/", width=settings.widget_width,
            command=lambda:show("/")).grid(row=2, column=3)

    # row = 3
    Button(root, text="7", width=settings.widget_width,
            command=lambda:show("7")).grid(row=3, column=0)
    Button(root, text="8", width=settings.widget_width,
            command=lambda:show("8")).grid(row=3, column=1)
    Button(root, text="9", width=settings.widget_width,
            command=lambda:show("9")).grid(row=3, column=2)
    Button(root, text="*", width=settings.widget_width,
            command=lambda:show("*")).grid(row=3, column=3)

    # row = 4
    Button(root, text="4", width=settings.widget_width,
            command=lambda:show("4")).grid(row=4, column=0)
    Button(root, text="5", width=settings.widget_width,
            command=lambda:show("5")).grid(row=4, column=1)
    Button(root, text="6", width=settings.widget_width,
            command=lambda:show("6")).grid(row=4, column=2)
    Button(root, text="-", width=settings.widget_width,
            command=lambda:show("-")).grid(row=4, column=3)

    # row = 5
    Button(root, text="1", width=settings.widget_width,
            command=lambda:show("1")).grid(row=5, column=0)
    Button(root, text="2", width=settings.widget_width,
            command=lambda:show("2")).grid(row=5, column=1)
    Button(root, text="3", width=settings.widget_width,
            command=lambda:show("3")).grid(row=5, column=2)
    Button(root, text="+", width=settings.widget_width,
            command=lambda:show("+")).grid(row=5, column=3)

     # row = 6
    Button(root, text="+/-", width=settings.widget_width,
            command=pos_neg).grid(row=6, column=0)
    Button(root, text="0", width=settings.widget_width,
            command=lambda:show("0")).grid(row=6, column=1)
    Button(root, text=".", width=settings.widget_width,
            command=lambda:show(".")).grid(row=6, column=2)
    Button(root, text="=", width=settings.widget_width,
            command=calculate).grid(row=6, column=3)




# Step1 create root of window, Tk
cal_root_win = Tk()
cal_root_win.title("Calculator")

# Create the settings of calculator
settings = Settings()

msg_on = False

# Step2 create the widges and set them property
result = StringVar()
result.set("2")
cal_result_and_button(cal_root_win, result)

# Step3 the tkinter main loop, wait for keyevent and so on
cal_root_win.mainloop()


# def run_main():
#     ''' The main function of calculator '''
#     # Step1 create root of window, Tk
#     cal_root_win = Tk()
#     cal_root_win.title("Calculator")

#     # Step2 create the widges and set them property
#     result = StringVar()
#     result.set("2")
#     cal_result_and_button(cal_root_win, result)

#     # Step3 the tkinter main loop, wait for keyevent and so on
#     cal_root_win.mainloop()


# Into main function
# if __name__ == '__main__':
#     run_main()
