##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: notepad.py
# @Date: 2022-01-03 11:28:55
# @Last Modified by: franc
# @Last Modified time: 2022-01-04 01:14:11
# @Project: python_programs
# @Use: The main function of Notepad

from os.path import basename
from tkinter import Tk
from tkinter import filedialog, messagebox, Menu, Frame, PhotoImage, Text
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button
from tkinter import IntVar, END
from PIL import Image, ImageTk

import os

class NotePad(Tk):

    # Self var of icons
    icons = ["new_file", "open_file", "save", "cut", "copy", "paste",
             "undo", "redo", "find"]
    # The all res of icons
    icon_res = []

    def __init__(self):
        ''' Initialize the notepad '''
        super().__init__()

        self.file_name = None


        # Set the window
        self.set_window()

        # Create the menu bar
        self.create_menu_bar()

        # Create the tool bar
        self.create_tool_bar()

        # Create the main body of view
        self.create_body_view()

        # Create pop menu for edit
        self.create_pop_menu()

    def set_window(self):
        ''' Set the window '''
        self.title("NotePad")
        max_width, max_height = self.maxsize()
        align_center = "800x600+%d+%d" % ((max_width-800)/2,(max_height-600)/2)
        self.geometry(align_center)
        self.iconbitmap("images/win.ico")


    def create_menu_bar(self):
        ''' Create the menu'''

        # Create the root menu
        menu_bar = Menu(self)

        # Add the File sub menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", accelerator="Ctrl+N",
                command=self.new_file)
        file_menu.add_command(label="Open File", accelerator="Ctrl+O",
                command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S",
                command=self.save_file)
        file_menu.add_command(label="Save As", accelerator="Shif+Ctrl+S",
                command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exist", accelerator="Alt+F4",
                command=self.exit_notepad)


        # Add the Edit sub menu
        edit_menu = Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z",
                command=lambda:self.handle_menu_action("undo"))
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y",
                command=lambda: self.handle_menu_action("redo"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X",
                command=lambda: self.handle_menu_action("cut"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C",
                command=lambda: self.handle_menu_action("copy"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V",
                command=lambda: self.handle_menu_action("paste"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", accelerator="Ctrl+F",
                command='')
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", accelerator="Ctrl+A",
            command=self.select_all)


         # Add the View sub menu
        view_menu = Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="View", menu=view_menu)
        # Line Number
        self.is_show_line_num = IntVar()
        self.is_show_line_num.set(1)
        view_menu.add_checkbutton(label="Line Number", onvalue=0, offvalue=1,
                variable=self.is_show_line_num, command="")
        # HeighLight
        self.is_heighlight_line = IntVar()
        self.is_heighlight_line.set(0)
        view_menu.add_checkbutton(label="HeighLight", onvalue=0, offvalue=1,
                variable=self.is_show_line_num, command="")
        view_menu.add_separator()
        # Theme
        themes_menu = Menu(menu_bar, tearoff=0)
        themes_menu.add_command(label="theme1", command="")
        themes_menu.add_command(label="theme2", command="")
        view_menu.add_cascade(label="themes", menu=themes_menu)

         # Add the About sub menu
        about_menu = Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About", command="")
        about_menu.add_command(label="Help", command="")

        # Point to menu bar
        # self["menu"] = menu_bar
        self.config(menu=menu_bar)


    def create_tool_bar(self):
        ''' Create the tool bar '''

        # Create the window container of Frame
        tool_bar = Frame(self, height=15, background="white")
        tool_bar.pack(fill="x")

        # Initialize the image and Button
        for icon in self.icons:
            image = Image.open("images/%s.gif" % (icon, ))
            tool_icon = ImageTk.PhotoImage(image)
            tool_btn = Button(tool_bar, image=tool_icon,
                command=self.tool_bar_action(icon))
            tool_btn.pack(side="left")
            self.icon_res.append(tool_icon)

    def _hot_key_bind(self):
        ''' Hot key bind for notepad file '''
        self.context_text.bind("<Control-o>",self.open_file)
        self.context_text.bind("<Control-O>",self.open_file)
        self.context_text.bind("<Control-s>",self.save_file)
        self.context_text.bind("<Control-S>",self.save_file)
        self.context_text.bind("<Control-n>",self.new_file)
        self.context_text.bind("<Control-N>",self.new_file)
        self.context_text.bind("<Shift-Control-s>",self.save_as_file)
        self.context_text.bind("<Shift-Control-S>",self.save_as_file)
        self.context_text.bind("<Alt-F4>",self.exit_notepad)

    def create_body_view(self):
        ''' create the main body of view. The three views of the rings, which
        always appear in the same order, are, left to right: Line number,
        edit context and scroll bar '''

        # Display the number of line
        self.line_number_bar = Text(self, width=4, padx=3, takefocus=0,
                bd=0, background="#F0E68C",state="disable")
        self.line_number_bar.pack(side="left", fill="y")

        # Display the edit of context
        self.context_text = Text(self, wrap="word", undo=True)
        self.context_text.pack(fill="both", expand="yes")

        # Hot key bind
        self._hot_key_bind()

        # Set the area of input text
        self.context_text.tag_config("active_line", background="#EEEEE0")


        # Display the scroll bar
        scroll_bar = Scrollbar(self.context_text)
        # scrollbar and text bind
        # scroll_bar["command"]=self.context_text.yview
        # self.context_text["yscrollcommand"] = scroll_bar.set
        scroll_bar.config(command=self.context_text.yview)
        self.context_text.config(yscrollcommand=scroll_bar.set)

        scroll_bar.pack(side="right", fill="y")

    def open_file(self, event=None):
        '''Open file function '''

        # Open file and set the type of file
        input_file = filedialog.askopenfilename(
            filetypes=[("All types","*.*"), ("Normal text file", "*.txt")]
            )
        if input_file:
            self.title("{}***Notepad".format(os.path.basename(input_file)))
            self.file_name = input_file
            self.context_text.delete(1.0, END)
            with open(input_file, 'r', encoding="utf-8") as _file:
                self.context_text.insert(1.0, _file.read())

    def write_file(self, file_name):
        ''' Write file to disk'''

        try:
            content = self.context_text.get(1.0, END)
            with open(file_name, 'w', encoding="utf-8") as _file:
                _file.write(content)
            self.title("{}---NotePad".format(os.path.basename(file_name)))
        except IOError:
            messagebox.showerror("Error", "File save error")

    def save_file(self, event=None):
        ''' Save the file to disk '''

        # when self.file_name is None, write file error
        if not self.file_name:
            self.save_as_file()
        else:
            self.write_file(self.file_name)



    def new_file(self, event=None):
        ''' Create new file '''

        self.title("New file---NotePad")
        self.context_text.delete(1.0, END)
        self.file_name = None


    def save_as_file(self, event=None):
        ''' Save file as other disk'''
        input_file = filedialog.asksaveasfilename(
            filetypes=[("All types","*.*"), ("Normal text file", "*.txt")]
            )

        if input_file:
            self.file_name = input_file
            self.write_file(self.file_name)

    def exit_notepad(self, event=None):
        ''' Exit the notepad '''

        # if click ok , exit notepad
        if messagebox.askokcancel("Exit", "Are you sure you need to quit?"):
            self.destroy()

    def create_pop_menu(self):
        ''' Create the pop menu '''

        eidit_pop_lists = ["cut", "copy", "paste", "undo", "redo"]
        pop_menu = Menu(self.context_text, tearoff=0)
        for item in eidit_pop_lists:
            pop_menu.add_command(label=item, compound="left",
                command=self.tool_bar_action(item))
        pop_menu.add_separator()
        pop_menu.add_command(label="Select all", command=self.select_all)

        # Bind
        self.context_text.bind("<Button-3>", lambda event:pop_menu.tk_popup(
                event.x_root, event.y_root))


    def handle_menu_action(self, action_type):
        ''' Pop menu action '''
        if action_type == "cut":
            self.context_text.event_generate("<<Cut>>")
        elif action_type == "copy":
            self.context_text.event_generate("<<Copy>>")
        elif action_type == "paste":
            self.context_text.event_generate("<<Paste>>")
        elif action_type == "undo":
            self.context_text.event_generate("<<Undo>>")
        elif action_type == "Redo":
            self.context_text.event_generate("<<Redo>>")

        return "break"


    def tool_bar_action(self, action_type):
        ''' Create action bar'''
        def handle():
            if action_type == "open_file":
                self.open_file()
            elif action_type == "new_file" :
                self.new_file()
            elif action_type == "save":
                self.save_file()
            else:
                self.handle_menu_action(action_type)
        # Retun the handle
        return handle

    def select_all(self):
        ''' Select the all text '''
        self.context_text.tag_add("sel", 1.0, END)
        return "break"






if __name__ == '__main__':
    # Create the notepad
    notepad = NotePad()
    # Call mainloop for notepad
    notepad.mainloop()


