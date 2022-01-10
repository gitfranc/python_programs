# -*- coding: utf-8 -*-
# @Author: franc
# @File: paint.py
# @Date: 2022/1/8 23:00
# @Project: paint
# @Used: Implement a simple drawing tool

from tkinter import Tk
from tkinter import Canvas, Button, colorchooser
from tkinter import PhotoImage

from settings import Settings


class Paint(Tk):
    """ The main class of draw tools """

    def __init__(self):
        """ Initialize the draw tools """
        super().__init__()

        # Create the object of settings
        self.settings = Settings()

        # Last draw id
        self.last_draw = 0
        self.start_x = 0
        self.start_y = 0
        self.draw_first_flag = False
        self.draw_enable = True

        # Set the window info for draw tools, such as width and height
        self.set_window()

        # Create the widgets for draw tools
        self.create_widgets()

    def set_window(self):
        """ Set the window of draw tools """
        self.title("The Sample Paint")
        self.iconbitmap("images/win.ico")
        max_width, max_height = self.maxsize()
        self.geometry("%dx%d+%d+%d" %
                      (self.settings.win_width,
                       self.settings.win_height,
                       (max_width - self.settings.win_width) / 2,
                       (max_height - self.settings.win_height) / 2))

    def create_widgets(self):
        """ Create the widgets for draw tools """

        # Create the Canvas for the draw tools
        self.draw_canvas = Canvas(self, width=self.settings.win_width,
                                  height=self.settings.win_height,
                                  bg=self.settings.bg_color, )
        self.draw_canvas.pack(fill="both",expand=True)

        # Create the function button for draw tools
        btn_start = Button(self.draw_canvas, text="Start",name="start",
                           border=0)
        btn_start.pack(pady=10,padx=10, anchor="w", expand=True)
        btn_pen = Button(self.draw_canvas, text="Pen", name="pen",border=0)
        btn_pen.pack(pady=10,padx=10,anchor="w", expand=True)
        btn_rect = Button(self.draw_canvas, text="Rect", name="rect",border=0)
        btn_rect.pack(pady=10,padx=10,anchor="w",expand=True)
        btn_oval = Button(self.draw_canvas, text="Oval", name="oval",border=0)
        btn_oval.pack(pady=10,padx=10,anchor="w",expand=True)
        btn_clear = Button(self.draw_canvas, text="Clear", name="clear",border=0)
        btn_clear.pack(pady=10,padx=10,anchor="w",expand=True)
        btn_eraser = Button(self.draw_canvas, text="Eraser", name="eraser",
                            border=0)
        btn_eraser.pack(pady=10,padx=10,anchor="w",expand=True)
        btn_line = Button(self.draw_canvas, text="Line", name="line",border=0)
        btn_line.pack(pady=10,padx=10,anchor="w",expand=True)
        btn_line_arrow = Button(self.draw_canvas, text="Line Arrow",
                                name="line_arrow",border=0)
        btn_line_arrow.pack(pady=10,padx=10,anchor="w",expand=True)
        btn_color = Button(self.draw_canvas, text="Color", name="color",
                           border=0)
        btn_color.pack(pady=10,padx=10,anchor="w",expand=True)

        # Bind the event
        btn_pen.bind_class("Button", "<1>", self.event_manager)
        self.bind_event()

    def bind_event(self):
        """ Bind the event """
        self.draw_canvas.bind("<ButtonRelease-1>", self.stop_draw)
        self.draw_canvas.bind("<Button-3>", self.change_bg_color)
        self.bind("<KeyPress-r>", self.choose_color)
        self.bind("<KeyPress-g>", self.choose_color)
        self.bind("<KeyPress-y>", self.choose_color)

    def change_bg_color(self, event):
        """ Change the background color when mouse left key press """
        print("change_bg_color")
        bg_color = colorchooser.askcolor(color=self.settings.bg_color,
                                         title="Select the color")
        self.settings.bg_color = bg_color[1]
        if not self.settings.bg_color:
            self.settings.bg_color = self.settings.BLACK
        # Change the bg color
        self.draw_canvas.config(bg=self.settings.bg_color)
        print(bg_color)

    def choose_color(self, event):
        """ Choose the fg color as red, green and yellow when key press r/g/y"""
        print("choose_color")
        if event.char == "r":
            self.settings.fg_color = self.settings.RED
        elif event.char == "g":
            self.settings.fg_color = self.settings.GREEN
        elif event.char == "y":
            self.settings.fg_color = self.settings.YELLOW

    def stop_draw(self, event):
        """ Deal with the mouse left button release """
        self.draw_first_flag = False
        self.last_draw = 0

    def event_manager(self, event):
        """ Deal with the event things """
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.draw_canvas.bind("<B1-Motion>", self.draw_line)
        elif name == "line_arrow":
            self.draw_canvas.bind("<B1-Motion>", self.draw_line_arrow)
        elif name == "rect":
            self.draw_canvas.bind("<B1-Motion>", self.draw_rect)
        elif name == "oval":
            self.draw_canvas.bind("<B1-Motion>", self.draw_oval)
        elif name == "pen":
            self.draw_canvas.bind("<B1-Motion>", self.draw_pen)
        elif name == "eraser":
            self.draw_canvas.bind("<B1-Motion>", self.eraser)
        elif name == "clear":
            self.draw_canvas.delete("all")
        elif name == "color":
            color = colorchooser.askcolor(color=self.settings.fg_color,
                                          title="Select the fg color")
            self.settings.fg_color = color[1]
        elif name == "start":
            self.draw_enable = True

    def start_draw(self, event):
        """ Start the draw """
        if not self.draw_first_flag:
            self.start_x = event.x
            self.start_y = event.y
            self.draw_first_flag = True

        # Delete the last draw id
        self.draw_canvas.delete(self.last_draw)

    def eraser(self, event):
        """ Eraser the last draw """
        if self.draw_enable:
            self.start_draw(event)
            self.draw_canvas.create_rectangle(event.x - 4, event.y - 4,
                                              event.x + 4, event.y + 4,
                                              fill=self.settings.bg_color)
            self.start_x = event.x
            self.start_y = event.y

    def draw_pen(self, event):
        """ Draw the rect """
        if self.draw_enable:
            self.start_draw(event)
            self.draw_canvas.create_line(self.start_x, self.start_y, event.x,
                                         event.y, fill=self.settings.fg_color)
            self.start_x = event.x
            self.start_y = event.y

    def draw_oval(self, event):
        """ Draw the rect """
        if self.draw_enable:
            self.start_draw(event)
            self.last_draw = \
                self.draw_canvas.create_oval(self.start_x, self.start_y,
                                             event.x, event.y,
                                             outline=self.settings.fg_color)

    def draw_rect(self, event):
        """ Draw the rect """
        if self.draw_enable:
            self.start_draw(event)
            self.last_draw = \
                self.draw_canvas.create_rectangle(self.start_x, self.start_y,
                                                  event.x, event.y,
                                                  outline=self.settings.fg_color)

    def draw_line_arrow(self, event):
        """ Draw the line arrow """
        if self.draw_enable:
            self.start_draw(event)
            self.last_draw = \
                self.draw_canvas.create_line(self.start_x, self.start_y,
                                             event.x, event.y, arrow="last",
                                             fill=self.settings.fg_color)

    def draw_line(self, event):
        """ Draw the line """
        if self.draw_enable:
            self.start_draw(event)
            self.last_draw = \
                self.draw_canvas.create_line(self.start_x, self.start_y,
                                             event.x,event.y,
                                             fill=self.settings.fg_color)


if __name__ == '__main__':
    paint = Paint()
    paint.mainloop()
