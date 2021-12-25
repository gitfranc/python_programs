##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: alien.py
# @Date: 2021-12-25 16:32:06
# @Last Modified by: franc
# @Last Modified time: 2021-12-25 22:41:53
# @Project: alien_invasion
# @Use: describe the alien info for alien invasion

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    ''' describe the single alien '''

    def __init__(self,ai_game):
        ''' initialize the alien and set the initial position '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the image of alien and get the rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #every alien is in corner of top-left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien of precise horizontal locations
        self.x = float(self.rect.x)

    def check_edges(self):
        '''If aliens are on the edge of the screen, return True '''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        '''move the alien left or right'''
        self.x += (self.settings.alien_speed * self.settings.alien_direction)
        self.rect.x = self.x



