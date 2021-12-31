# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: calculator.py
# @Date: 2021-12-30 21:57:59
# @Last Modified by: franc
# @Last Modified time: 2021-12-31 19:30:23
# @Project: calculator
# @Use: The main function of Calculator

from tkinter import Tk
from tkinter import Label, Button
from tkinter import StringVar
import math

from settings import Settings


class Calculator:
    ''' The class for calculator main function '''

    def __init__(self):
        ''' Initialize the calculator '''

        # Step1 create root of window, Tk
        # Initialize root window and the variable of result
        self.root_window = Tk()
        # Tnitialize the settings
        self.settings = Settings(self)
        self.root_window.config(bg=self.settings.color_btn_bg)

        self.result = StringVar()
        self.result.set("0")



        # Initialize the label of result
        self.result_label = Label(self.root_window, width=30, height=2,
            fg=self.settings.color_num_fg, bg=self.settings.color_input_bg,
            relief="sunken", anchor="se",textvariable=self.result)

        # set the title of window
        self.root_window.title(self.settings.cal_win_title)

    def clear_ce(self):
        self.result.set("0")


    def clear(self):
        self.result.set("0")

    def show(self, button_string):
        content = self.result.get()
        if content == "0":
            content = ""
        self.result.set(content + button_string)


    def backspace(self):
        self.result.set(self.result.get()[:-1])


    def reciprocal(self):
        res = eval("1"+"/" + self.result.get())
        self.result.set(str(res))


    def square(self):
        res = eval(self.result.get() + "**" + "2")
        self.result.set(str(res))

    def sqrt2(self):
        res = math.sqrt(int(self.result.get()))
        self.result.set(str(res))

    def calculate(self):
        res = eval(self.result.get())
        self.result.set(self.result.get() + " = \n" + str(res))

    def pos_neg(self):
        res = eval(self.result.get())
        if res >= 0:
            self.result.set("-"+ self.result.get())
        else:
            res_neg = abs(res)
            self.result.set(str(abs(res)))


    def cal_result_and_button(self):
        ''' Display the result and button '''

        # Display the result of calculation
        self.result_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Display the button of calculator
        Button(self.root_window, text="%", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg
                    ,command=lambda: self.show("%")).grid(row=1, column=0)
        Button(self.root_window, text="CE", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=self.clear_ce).grid(row=1, column=1)
        Button(self.root_window, text="C", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=self.clear).grid(row=1, column=2)
        Button(self.root_window, text="DEL", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=self.backspace).grid(row=1, column=3)

         # row = 2
        Button(self.root_window, text="1/x", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=self.reciprocal).grid(row=2, column=0)
        Button(self.root_window, text="x^2", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=self.square).grid(row=2, column=1)
        Button(self.root_window, text="sqrt2", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=self.sqrt2).grid(row=2, column=2)
        Button(self.root_window, text="/", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("/")).grid(row=2, column=3)

        # row = 3
        Button(self.root_window, text="7", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("7")).grid(row=3, column=0)
        Button(self.root_window, text="8", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("8")).grid(row=3, column=1)
        Button(self.root_window, text="9", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("9")).grid(row=3, column=2)
        Button(self.root_window, text="*", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("*")).grid(row=3, column=3)

        # row = 4
        Button(self.root_window, text="4", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("4")).grid(row=4, column=0)
        Button(self.root_window, text="5", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("5")).grid(row=4, column=1)
        Button(self.root_window, text="6", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("6")).grid(row=4, column=2)
        Button(self.root_window, text="-", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("-")).grid(row=4, column=3)

        # row = 5
        Button(self.root_window, text="1", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("1")).grid(row=5, column=0)
        Button(self.root_window, text="2", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                     command=lambda:self.show("2")).grid(row=5, column=1)
        Button(self.root_window, text="3", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("3")).grid(row=5, column=2)
        Button(self.root_window, text="+", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("+")).grid(row=5, column=3)

        # row = 6
        Button(self.root_window, text="+/-", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                     command=self.pos_neg).grid(row=6, column=0)
        Button(self.root_window, text="0", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show("0")).grid(row=6, column=1)
        Button(self.root_window, text=".", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    command=lambda:self.show(".")).grid(row=6, column=2)
        Button(self.root_window, text="=", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg="red",
                    command=self.calculate).grid(row=6, column=3)

    def run_main(self):
        ''' The main function of calculator '''

        # Step2 create the widges and set them property
        self.cal_result_and_button()

        # Step3 the tkinter main loop, wait for keyevent and so on
        self.root_window.mainloop()


# Into main function
if __name__ == '__main__':
    calculator = Calculator()
    calculator.run_main()
