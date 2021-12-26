##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: game_stats.py
# @Date: 2021-12-25 23:31:44
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 22:29:39
# @Project: alien_invasion
# @Use: Track the game of Alien Invasion statistics

class GameStats:
    ''' describe the game of statistics'''

    def __init__(self, ai_game):
        ''' initialize the statistics '''
        self.settings = ai_game.settings;
        self.high_score = 0
        self.level = 1
        self.reset_stats()

        # the game is active default
        self.game_active = False
    def reset_stats(self):
        ''' initialize the statistics of variables that may change '''

        self.ship_left = self.settings.ship_limit
        self.score = 0


