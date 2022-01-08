# -*- coding: utf-8 -*-
# @Author: franc
# @File: paint.py
# @Date: 2022/1/8 23:00
# @Project: paint
# @Used: Implement a simple drawing tool

from tkinter import Tk
from tkinter import Canvas, Button

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
        self.start_draw_flag = False

        # Set the window info for draw tools, such as width and height
        self.set_window()

        # Create the widgets for draw tools
        self.create_widgets()

    def set_window(self):
        """ Set the window of draw tools """
        self.title("The Sample Paint")
        max_width, max_height = self.maxsize()
        self.geometry("%dx%d+%d+%d" % (self.settings.win_width,
                                       self.settings.win_height,
                                       (max_width-self.settings.win_width)/2,
                                       (max_height-self.settings.win_height)/2))

    def create_widgets(self):
        """ Create the widgets for draw tools """

        # Create the Canvas for the draw tools
        self.draw_canvas = Canvas(self, width=self.settings.win_width,
                        height=self.settings.win_height*0.9, bg="black")
        self.draw_canvas.pack()

        # Create the function button for draw tools
        btn_start = Button(self, text="Start", name="start")
        btn_start.pack(side="left", padx=20)
        btn_pen= Button(self, text="Pen", name="pen")
        btn_pen.pack(side="left", padx=20)
        btn_rect = Button(self, text="Rect", name="rect")
        btn_rect.pack(side="left", padx=20)
        btn_clear = Button(self, text="Clear", name="clear")
        btn_clear.pack(side="left", padx=20)
        btn_erasor = Button(self, text="Erasor", name="erasor")
        btn_erasor.pack(side="left", padx=20)
        btn_line = Button(self, text="Line", name="line")
        btn_line.pack(side="left", padx=20)
        btn_line_arrow = Button(self, text="Line Arrow", name="line_arrow")
        btn_line_arrow.pack(side="left", padx=20)
        btn_color = Button(self, text="Color", name="color")
        btn_color.pack(side="left", padx=20)

        # Bind the event
        btn_pen.bind_class("Button","<1>", self.event_manager)
        self.draw_canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def stop_draw(self, event):
        """ Deal with the mouse left button release """
        self.start_draw_flag = False
        self.last_draw = 0


    def event_manager(self, event):
        """ Deal with the event things """
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.draw_canvas.bind("<B1-Motion>", self.draw_line)

    def draw_line(self,event):

        if not self.start_draw_flag:
            self.start_x = event.x
            self.start_y = event.y
            self.start_draw_flag = True

        self.draw_canvas.delete(self.last_draw)
        self.last_draw = self.draw_canvas.create_line(self.start_x,self.start_y,
                                                      event.x, event.y,
                                                      fill="red")




if __name__ == '__main__':
    paint = Paint()
    paint.mainloop()
