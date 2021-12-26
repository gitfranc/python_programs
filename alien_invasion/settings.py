##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: settings.py
# @Date: 2021-12-25 14:54:11
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 22:05:49
# @Project: alien_invasion
# @Use: The settins of the game

class Settings:
    ''' storage the all settins for Alien Invasion game '''

    def __init__(self):
        ''' init settings of the game '''

        # screen setting
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230,230,230)
        # self.bg_color = (0,0,250)

        # ship setting
        self.ship_limit = 3

        # bullet setting
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #limit the number of bullet
        self.bullet_allowed = 3

        # alien setting
        self.alien_drop_speed = 10

        # Speed up the pace of the game
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        ''' Initiallize the dynamic settings '''

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # 1->right, -1->left
        self.alien_direction =1

        # get score
        self.alien_point = 50

    def increase_speed(self):
        ''' Increase the speed '''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)

