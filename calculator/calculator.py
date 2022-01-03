# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: calculator.py
# @Date: 2021-12-30 21:57:59
# @Last Modified by: franc
# @Last Modified time: 2022-01-03 21:14:16
# @Project: calculator
# @Use: The main function of Calculator

from tkinter import Tk
from tkinter import Label, Button, messagebox
from tkinter import StringVar
from tkinter.font import Font
import os, sys, math

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

        self.font = Font(family="Consolas", size=20)

        # set the properties of window
        self.root_window.title(self.settings.win_title)
        self.root_window.maxsize(self.settings.win_width,
                self.settings.win_height)
        self.root_window.minsize(self.settings.win_width,
                self.settings.win_height)
        #set the icon for the window
        self.root_window.iconbitmap(self._resource_path("images/win.ico"))


        self.record = StringVar()
        self.record.set("0")
        self.result = StringVar()
        self.result.set("")


    def _resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)



    def clear_ce(self):
        self.record.set("0")
        self.result.set("")


    def clear(self):
        self.record.set("0")
        self.result.set("")

    def show(self, button_string):
        content = self.record.get()
        if content == "0":
            content = ""
        self.record.set(content + button_string)


    def backspace(self):
        self.record.set(self.record.get()[:-1])


    def reciprocal(self):
        try:
            res = eval("1"+"/" + self.record.get())
        except Exception:
            messagebox.showwarning("Warning",
                    "illegal operation, Please check your input")
        else:
            self.record.set(str(res))


    def square(self):
        try:
             res = eval(self.record.get() + "**" + "2")
        except Exception:
            messagebox.showwarning("Warning",
                    "illegal operation, Please check your input")
        else:
            self.result.set(str(res))

    def sqrt2(self):
        try:
            res = math.sqrt(int(self.record.get()))
        except Exception:
            messagebox.showwarning("Warning",
                    "illegal operation, Please check your input")
        else:
            self.record.set(str(res))

    def calculate(self):
        try:
            res = eval(self.record.get())
        except Exception:
            messagebox.showwarning("Warning",
                    "illegal operation, Please check your input")
        else:
            self.result.set(str(res))

    def pos_neg(self):
        try:
            res = eval(self.record.get())
        except Exception:
            messagebox.showwarning("Warning",
                    "illegal operation, Please check your input")
        else:
            if res >= 0:
                self.record.set("-"+ self.record.get())
            else:
                res_neg = abs(res)
                self.record.set(str(abs(res)))


    def cal_result_and_button(self):
        ''' Display the result and button '''

        # Display the result of calculation
        Label(self.root_window, width=self.settings.win_width,
             height=2, font=self.font, fg=self.settings.color_num_fg,
             bg=self.settings.color_input_bg, anchor="se",
             textvariable=self.record).place(width=self.settings.win_width,
             height=70)

        Label(self.root_window, width=self.settings.win_width,
             height=2, font=self.font, fg=self.settings.color_num_fg,
             bg=self.settings.color_input_bg, anchor="se",
             textvariable=self.result).place(y=70,width=self.settings.win_width,
             height=70)

        # Display the button of calculator
        Button(self.root_window, text="%", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda: self.show("%")).place(
                    x=self.settings.widget_width * 0,
                    y=140 + self.settings.widget_height * 0,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="CE", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.clear_ce).place(
                    x=self.settings.widget_width * 1,
                    y=140 + self.settings.widget_height * 0,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="C", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.clear).place(
                    x=self.settings.widget_width * 2,
                    y=140 + self.settings.widget_height * 0,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="DEL", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.backspace).place(
                    x=self.settings.widget_width * 3,
                    y=140 + self.settings.widget_height * 0,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)

         # row = 2
        Button(self.root_window, text="1/x", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.reciprocal).place(
                    x=self.settings.widget_width * 0,
                    y=140 + self.settings.widget_height * 1,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="x^2", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.square).place(
                    x=self.settings.widget_width * 1,
                    y=140 + self.settings.widget_height * 1,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="sqrt2", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.sqrt2).place(
                    x=self.settings.widget_width * 2,
                    y=140 + self.settings.widget_height * 1,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="/", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("/")).place(
                    x=self.settings.widget_width * 3,
                    y=140 + self.settings.widget_height * 1,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)

        # row = 3
        Button(self.root_window, text="7", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("7")).place(
                    x=self.settings.widget_width * 0,
                    y=140 + self.settings.widget_height * 2,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="8", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("8")).place(
                    x=self.settings.widget_width * 1,
                    y=140 + self.settings.widget_height * 2,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="9", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("9")).place(
                    x=self.settings.widget_width * 2,
                    y=140 + self.settings.widget_height * 2,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="*", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("*")).place(
                    x=self.settings.widget_width * 3,
                    y=140 + self.settings.widget_height * 2,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)

        # row = 4
        Button(self.root_window, text="4", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("4")).place(
                    x=self.settings.widget_width * 0,
                    y=140 + self.settings.widget_height * 3,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="5", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("5")).place(
                    x=self.settings.widget_width * 1,
                    y=140 + self.settings.widget_height * 3,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="6", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("6")).place(
                    x=self.settings.widget_width * 2,
                    y=140 + self.settings.widget_height * 3,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="-", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("-")).place(
                    x=self.settings.widget_width * 3,
                    y=140 + self.settings.widget_height * 3,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)

        # row = 5
        Button(self.root_window, text="1", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("1")).place(
                    x=self.settings.widget_width * 0,
                    y=140 + self.settings.widget_height * 4,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="2", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("2")).place(
                    x=self.settings.widget_width * 1,
                    y=140 + self.settings.widget_height * 4,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="3", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("3")).place(
                    x=self.settings.widget_width * 2,
                    y=140 + self.settings.widget_height * 4,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="+", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("+")).place(
                    x=self.settings.widget_width * 3,
                    y=140 + self.settings.widget_height * 4,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)

        # row = 6
        Button(self.root_window, text="+/-", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=self.pos_neg).place(
                    x=self.settings.widget_width * 0,
                    y=140 + self.settings.widget_height * 5,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="0", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show("0")).place(
                    x=self.settings.widget_width * 1,
                    y=140 + self.settings.widget_height * 5,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text=".", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg=self.settings.color_btn_bg,
                    font=self.font,bd=0,command=lambda:self.show(".")).place(
                    x=self.settings.widget_width * 2,
                    y=140 + self.settings.widget_height * 5,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)
        Button(self.root_window, text="=", width=self.settings.widget_width,
                    fg=self.settings.color_btn_fg, bg="red",
                    font=self.font,bd=0,command=self.calculate).place(
                    x=self.settings.widget_width * 3,
                    y=140 + self.settings.widget_height * 5,
                    width=self.settings.widget_width,
                    height=self.settings.widget_height)

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
