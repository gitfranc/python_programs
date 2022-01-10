##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: franc
# @Email: caifei521@163.com
# @File: notepad.py
# @Date: 2022-01-03 11:28:55
# @Last Modified by: franc
# @Last Modified time: 2022-01-04 23:13:51
# @Project: python_programs
# @Use: The main function of Notepad

import os
from tkinter import Tk
from tkinter import filedialog, messagebox, Menu, Frame, Text
from tkinter import Toplevel, Entry
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button
from tkinter import IntVar, END, StringVar
from PIL import Image, ImageTk

from settings import Settings

class NotePad(Tk):

    def __init__(self):
        """ Initialize the notepad """
        super().__init__()
        self.settings = Settings()

        self.icon_res = []
        self.context_text = None
        self.line_number_bar = None
        self.file_name = None
        self.scroll_bar = None
        self.is_show_line_num = IntVar()
        self.is_show_line_num.set(1)

        self.is_highlight_line = IntVar()
        self.is_highlight_line.set(1)

        # theme of settings
        self.theme_choice = StringVar()
        self.theme_choice.set("Default")

        # font of settings
        self.font_choice = StringVar()
        self.font_choice.set("Consalos")

        # Set the window
        self.setWindow()

        # Create Widgets for notepad
        self.createWidgets()

    def createWidgets(self):
        """ Create the widgets for the notepad """

        # Create the menu bar
        self.createMenuBar()
        # Create the toolbar
        self.createToolBar()
        # Create the main body of view
        self.createBodyView()
        # Create pop menu for edit
        self.createPopMenu()

    def getCenterScreen(self, width, height):
        """ Get the center of screen position """
        # Get the max screen of width and height
        max_width, max_height = self.maxsize()
        align_center = "%dx%d+%d+%d" % (width, height, (max_width - width) / 2,
                                        (max_height - height) / 2)
        return align_center

    def setWindow(self):
        """ Set the window """
        self.title("NotePad")
        align_center = self.getCenterScreen(self.settings.win_width,
                                              self.settings.win_height)
        self.geometry(align_center)
        self.iconbitmap("images/win.ico")

    def createMenuBar(self):
        """ Create the menu"""

        # Create the root menu
        menu_bar = Menu(self)

        # Add the File sub menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", accelerator="Ctrl+N",
                              command=self.newFile)
        file_menu.add_command(label="Open File", accelerator="Ctrl+O",
                              command=self.openFile)
        file_menu.add_command(label="Save", accelerator="Ctrl+S",
                              command=self.saveFile)
        file_menu.add_command(label="Save As", accelerator="Shif+Ctrl+S",
                              command=self.saveAsFile)
        file_menu.add_separator()
        file_menu.add_command(label="Exist", accelerator="Alt+F4",
                              command=self.exitNotepad)

        # Add the Edit sub menu
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z",
                              command=lambda: self.handleMenuAction("undo"))
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y",
                              command=lambda: self.handleMenuAction("redo"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X",
                              command=lambda: self.handleMenuAction("cut"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C",
                              command=lambda: self.handleMenuAction("copy"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V",
                              command=lambda: self.handleMenuAction("paste"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", accelerator="Ctrl+F",
                              command=self.searchTextDialog)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", accelerator="Ctrl+A",
                              command=self.selectAll)

        # Add the View sub menu
        view_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=view_menu)
        # Line Number
        view_menu.add_checkbutton(label="Line Number", onvalue=1, offvalue=0,
                                  variable=self.is_show_line_num,
                                  command=self.updateLineNum)
        # HighLight
        view_menu.add_checkbutton(label="HighLight", onvalue=1, offvalue=0,
                                  variable=self.is_highlight_line,
                                  command=self.updateLineHighlight)

        # Settings
        settings_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        # font menu
        font_menu = Menu(menu_bar, tearoff=0)
        for key in sorted(self.settings.font_families):
            font_menu.add_radiobutton(label=key, variable=self.font_choice,
                                          command=self.updateFont)
        settings_menu.add_cascade(label="font", menu=font_menu)
        settings_menu.add_separator()

        # Theme
        themes_menu = Menu(menu_bar, tearoff=0)
        for key in sorted(self.settings.theme_colors):
            themes_menu.add_radiobutton(label=key, variable=self.theme_choice,
                                        command=self.changeTheme)
        settings_menu.add_cascade(label="themes", menu=themes_menu)

        # Add the About sub menu
        about_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About",
                               command=lambda: self.showMessage("about"))
        about_menu.add_command(label="Help",
                               command=lambda: self.showMessage("help"))

        # Point to menu bar
        # self["menu"] = menu_bar
        self.config(menu=menu_bar)

    def getFontSelect(self):
        """ Get the font select """
        select_font = self.font_choice.get()
        font_selected = self.settings.font_families[select_font]
        return  font_selected

    def updateLineNumFont(self):
        """ Update the line number bar font """

        select_font = self.getFontSelect()
        self.line_number_bar.config(state="normal")
        self.line_number_bar.config(font=select_font)
        self.line_number_bar.config(state="disable")

    def updateFont(self):
        """ Update the font, which line number bar and context """

        # Get the select font
        font_selected = self.getFontSelect()
        # Set the context font
        self.context_text.config(font=font_selected)

        # Set the line number bar font
        self.updateLineNumFont()


    def createToolBar(self):
        """ Create the toolbar """

        # Create the window container of Frame
        tool_bar = Frame(self, height=15, background="white")
        tool_bar.pack(fill="x")

        # Initialize the image and Button
        for icon in self.settings.icons:
            image = Image.open("images/%s.gif" % (icon,))
            tool_icon = ImageTk.PhotoImage(image)
            tool_btn = Button(tool_bar, image=tool_icon,
                              command=self.toolbarAction(icon))
            tool_btn.pack(side="left")
            self.icon_res.append(tool_icon)

    def _hotKeyBind(self):
        """ Hot key bind for notepad file """
        self.context_text.bind("<Control-o>", self.openFile)
        self.context_text.bind("<Control-O>", self.openFile)
        self.context_text.bind("<Control-s>", self.saveFile)
        self.context_text.bind("<Control-S>", self.saveFile)
        self.context_text.bind("<Control-n>", self.newFile)
        self.context_text.bind("<Control-N>", self.newFile)
        self.context_text.bind("<Shift-Control-s>", self.saveAsFile)
        self.context_text.bind("<Shift-Control-S>", self.saveAsFile)
        self.context_text.bind("<Alt-F4>", self.exitNotepad)
        # Update line num when any key input
        self.context_text.bind("<Any-KeyPress>", lambda e:self.updateLineNum())

        # Mouse wheel control the context, line num and scroll bar as the same
        self.context_text.bind("<MouseWheel>", lambda e: self.mouseWheel(e))
        self.line_number_bar.bind("<MouseWheel>", lambda e: self.mouseWheel(e))
        self.scroll_bar.bind("<MouseWheel>", lambda e: self.mouseWheel(e))

    def scrollBarCommand(self, *yy):
        """ Scroll bar control context and line number bar at the same """
        # yy is that scroll bar move to point
        self.context_text.yview(*yy)
        self.line_number_bar.yview(*yy)

    def mouseWheel(self, event):
        """ Mouse wheel control the line number, context and scroll bar"""

        # When y positive is 1, and y negative is -1
        self.line_number_bar.yview_scroll(int(-1 * (event.delta)), "units")
        self.context_text.yview_scroll(int(-1 * (event.delta)), "units")
        return "break"

    def createBodyView(self):
        """ create the main body of view. The three views of the rings, which
        always appear in the same order, are, left to right: Line number,
        edit context and scroll bar """

        # Display the number of line
        self.line_number_bar = Text(self, width=4, padx=3, takefocus=0,
                                    bd=0, background="#F0E68C")
        # Config the line number bar ,such as center
        self.line_number_bar.tag_config("all_line",justify="center")
        self.line_number_bar.pack(side="left", fill="y")


        # Display the edit of context
        self.context_text = Text(self, wrap="word", undo=True, font="Consalos 10")
        self.context_text.pack(fill="both", expand=1)

        # Set the current line tag
        self.context_text.tag_config("active_line", background="#EEEEE0")

        # Display the scroll bar
        self.scroll_bar = Scrollbar(self.context_text)
        # Scrollbar and text bind
        self.scroll_bar.config(command=self.scrollBarCommand)
        self.context_text.config(yscrollcommand=self.scroll_bar.set)
        # scrollbar and line number bind
        self.line_number_bar.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.pack(side="right", fill="y")

        # Hot key bind
        self._hotKeyBind()

    def updateView(self):
        """ Update the view when open and new file and so on """
        # Update the line num display
        self.updateLineNum()
        # Update the line highlight display
        self.updateLineHighlight()

    def openFile(self, event=None):
        """Open file function """

        # Open file and set the type of file
        input_file = filedialog.askopenfilename(
            filetypes=[("All types", "*.*"), ("Normal text file", "*.txt")]
        )
        if input_file:
            self.title("{}***Notepad".format(os.path.basename(input_file)))
            self.file_name = input_file
            self.context_text.delete(1.0, END)
            with open(input_file, 'r', encoding="utf-8") as _file:
                self.context_text.insert(1.0, _file.read())

        # Should update view when open file
        self.updateView()


    def writeFile(self, file_name):
        """ Write file to disk"""

        try:
            content = self.context_text.get(1.0, END)
            with open(file_name, 'w', encoding="utf-8") as _file:
                _file.write(content)
            self.title("{}---NotePad".format(os.path.basename(file_name)))
        except IOError:
            messagebox.showerror("Error", "File save error")

    def saveFile(self, event=None):
        """ Save the file to disk """

        # when self.file_name is None, write file error
        if not self.file_name:
            self.saveAsFile()
        else:
            self.writeFile(self.file_name)

    def newFile(self, event=None):
        """ Create new file """

        self.title("New file---NotePad")
        self.context_text.delete(1.0, END)
        self.file_name = None

        # Should update view when open file
        self.updateView()

    def saveAsFile(self, event=None):
        """ Save file as other disk """
        input_file = filedialog.asksaveasfilename(
            filetypes=[("All types", "*.*"), ("Normal text file", "*.txt")]
        )

        if input_file:
            self.file_name = input_file
            self.writeFile(self.file_name)

    def exitNotepad(self, event=None):
        """ Exit the notepad """

        # if click ok , exit notepad
        if messagebox.askokcancel("Exit", "Are you sure you need to quit?"):
            self.destroy()

    def createPopMenu(self):
        """ Create the pop menu """

        edit_pop_lists = ["cut", "copy", "paste", "undo", "redo"]
        pop_menu = Menu(self.context_text, tearoff=0)
        for item in edit_pop_lists:
            pop_menu.add_command(label=item, compound="left",
                                 command=self.toolbarAction(item))
        pop_menu.add_separator()
        pop_menu.add_command(label="Select all", command=self.selectAll)

        # Bind
        self.context_text.bind("<Button-3>", lambda event: pop_menu.tk_popup(
            event.x_root, event.y_root))

    def handleMenuAction(self, action_type):
        """ Pop menu action """
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

    def toolbarAction(self, action_type):
        """ Create action bar """

        def handle():
            if action_type == "openFile":
                self.openFile()
            elif action_type == "newFile":
                self.newFile()
            elif action_type == "save":
                self.saveFile()
            elif action_type == "find":
                self.searchTextDialog()
            else:
                self.handleMenuAction(action_type)

        # Return the handle
        return handle

    def selectAll(self):
        """ Select the all text """
        self.context_text.tag_add("sel", 1.0, END)
        return "break"

    def updateLineNum(self):
        """ Display the line number """
        # Set the line number bar state to normal
        self.line_number_bar.config(state="normal")

        if self.is_show_line_num.get():
            # Get the row and column for all context
            row, col = self.context_text.index(END).split(".")

            # Insert the "\n" every line
            line_num_content = "\n".join(str(i) for i in range(1, int(row)))
            self.line_number_bar.delete(1.0, END)
            self.line_number_bar.insert(1.10, line_num_content)
            self.line_number_bar.tag_remove("all_line",1.0, END)
            self.line_number_bar.tag_add("all_line", 1.0, END)
        else:
            self.line_number_bar.delete(1.0, END)
            self.line_number_bar.tag_remove("all_line_center", 1.0, END)
        # Set the line number bar state to disable
        self.line_number_bar.config(state="disable")

    def updateLineHighlight(self):
        """ Highlight tht current line """
        if self.is_highlight_line.get():
            self.context_text.tag_remove("active_line", 1.0, END)
            self.context_text.tag_add("active_line", "insert linestart",
                                      "insert lineend+1c")
            self.context_text.after(200, self.updateLineHighlight)
        else:
            self.context_text.tag_remove("active_line", 1.0, END)

    def searchTextDialog(self):
        """ Create the search dialog """

        search_dialog = Toplevel(self)
        search_dialog.title("Search text")
        max_width, max_height = self.maxsize()
        align_center = self.getCenterScreen(self.settings.search_win_width,
                                              self.settings.search_win_height)
        search_dialog.geometry(align_center)
        # search_dialog.resizable(False, False)

        Label(search_dialog, text="Search All").grid(row=0, column=0,
                                                     sticky="e")
        search_text = Entry(search_dialog, width=25)
        search_text.grid(row=0, column=1, padx=2, pady=2, sticky="we")
        search_text.focus_set()

        # Ignore the case
        ignore_case_value = IntVar()
        Checkbutton(search_dialog, text="Ignore Case",
                    variable=ignore_case_value,
                    ).grid(row=1, column=1, sticky="we", padx=2, pady=2)

        Button(search_dialog, text="Find",
               command=lambda: self.searchTextResult(
                   search_text.get(), ignore_case_value.get(), search_dialog,
                   search_text)).grid(row=0, column=2, sticky="we", padx=2)

        def close_search_dialog():
            self.context_text.tag_remove("match", 1.0, END)
            search_dialog.destroy()

        search_dialog.protocol("WM_DELETE_WINDOW", close_search_dialog)

        return "break"

    def searchTextResult(self, key, ignore_case, search_dialog, search_text):
        """ Search text by word an word """

        self.context_text.tag_remove("match", 1.0, END)
        matches_found = 0
        if key:
            start_pos = 1.0
            while True:
                start_pos = self.context_text.search(key, start_pos,
                                                     nocase=ignore_case,
                                                     stopindex=END)
                if not start_pos:
                    break
                end_pos = "{}+{}c".format(start_pos, len(key))
                self.context_text.tag_add("match", start_pos, end_pos)
                matches_found += 1
                start_pos = end_pos

            self.context_text.tag_config("match", foreground="red",
                                         background="yellow")
            search_text.focus_set()
            search_dialog.title("Find %d matches " % matches_found)

    def changeTheme(self):
        """ Change the theme """

        selected_theme = self.theme_choice.get()
        fg_bg = self.settings.theme_colors[selected_theme]
        fg_color, bg_color = fg_bg.split(".")
        self.context_text.config(fg=fg_color, bg=bg_color)

    def showMessage(self, item_type):
        """ About and Help display a message box """

        if item_type == "about":
            messagebox.showinfo("About", "This is a sample notepad!")
        else:
            messagebox.showinfo("Help", "This is a help words", icon="question")

    def notepadMain(self):
        """ Main loop for notepad """

        # Call mainloop for notepad
        self.mainloop()


if __name__ == '__main__':
    # Create the notepad
    notepad = NotePad()
    notepad.notepadMain()
