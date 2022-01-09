# -*- coding: utf-8 -*-
# @Author: franc
# @File: settings.py
# @Date: 2022/1/8 23:11
# @Project: paint
# @Used: The setting of draw tools

class Settings:
    """ The class for settings of draw tools """

    def __init__(self):
        """ Initialize the settings """

        # window
        self.win_width = 900;
        self.win_height = 500;

        # color
        self.fg_color = "#FF0000"
        self.bg_color = "#000000"
        self.RED = "#FF0000"
        self.GREEN = "#00FF00"
        self.YELLOW = "#FFFF00"
