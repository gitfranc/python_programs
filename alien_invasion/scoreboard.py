##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: scoreboard.py
# @Date: 2021-12-26 21:22:07
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 22:47:52
# @Project: alien_invasion
# @Use: the display the current score, max score, game level and left ship

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """ display the score """

    def __init__(self, ai_game):
        ''' Initialize the score of display '''
        self.ai_game = ai_game
        self.screen  = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # The font of score display
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial image of score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        ''' Render score as an image '''
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                self.settings.bg_color)

        # display scroe at the upper right corner of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_high_score(self):
        ''' Render high score as an image '''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        # Display the max score at the top center corner of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        ''' Render the level as image '''

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                self.settings.bg_color)

        # Put the level below to the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        ''' Display the number of left ship '''

        self.ships = Group()

        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        ''' display score '''
        self.screen.blit(self.score_image, self.score_rect)

        # Display high score
        self.screen.blit(self.high_score_image, self.high_score_rect)

        # Display the level of game
        self.screen.blit(self.level_image, self.level_rect)

        # Display the left of ships
        self.ships.draw(self.screen)

    def check_high_score(self):
        ''' check if there are new high score can be created '''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()



