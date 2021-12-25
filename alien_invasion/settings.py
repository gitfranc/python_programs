##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: settings.py
# @Date: 2021-12-25 14:54:11
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 00:12:36
# @Project: alien_invasion
# @Use: The settins of the game

class Settings:
    ''' storage the all settins for Alien Invasion game '''

    def __init__(self):
        ''' init settings of the game '''
        # screen setting
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)
        # self.bg_color = (0,0,250)

        # the speed of ship
        self.ship_speed = 0.5
        self.ship_limit = 3

        # the color of bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        #limit the number of bullet
        self.bullet_allowed = 3

        # the speed of alien
        self.alien_speed = 1.0
        self.alien_drop_speed = 50
        # 1->right, -1->left
        self.alien_direction =1

