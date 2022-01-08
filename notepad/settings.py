# -*- coding: utf-8 -*-
# @Author: franc
# @File: settings
# @Date: 2022/1/5 11:38
# @Project: notepad
# @Used: The settings of notepad

class Settings:
    """ The class for describe the notepad settings """

    def __init__(self):
        """ Initialize the settings """

        # The icons of notepad toolbars
        self.icons = ["new_file", "open_file", "save", "cut", "copy", "paste",
             "undo", "redo", "find"]
        # The theme of notepad
        self. theme_colors = {
            "Default": "#000000.#FFFFFF",
            "Night": "#FFFFFF.#000000",
        }

        self.font_families = {
            "Consalos": ("Consalos", 10),
            "Arial": ("Arial", 10),
            "Courier": ("Courier", 10),
        }

        # The settings of root window
        self.win_width = 800
        self.win_height = 600

        # The settings of search window
        self.search_win_width = 350
        self.search_win_height = 80





