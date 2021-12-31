##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: settings.py
# @Date: 2021-12-30 23:57:32
# @Last Modified by: franc
# @Last Modified time: 2022-01-01 00:30:21
# @Project: calculator
# @Use: The settings for calculator

class Settings:
    ''' The settings of calculator '''

    def __init__(self, cal):

        ''' Intitialize the Settings '''
        self.win_title = "Calculator"
        self.win_width = 300
        self.win_height = 560


        self.widget_width = 75
        self.widget_height = 70


        self.color_input_bg = "#393943"
        self.color_num_fg = "#DCDCDC"
        self.color_btn_fg = "#909194"
        self.color_btn_bg = "#22222C"

