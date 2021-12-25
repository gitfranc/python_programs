##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: ship.py
# @Date: 2021-12-25 14:54:11
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 00:13:10
# @Project: alien_invasion
# @Use: describe the ship of the game

import pygame


class Ship:
    ''' The class of manager the ship '''

    def __init__(self,ai_game):
        ''' init the ship and position '''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the image of the spacecraft and get its enclosing rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # For new ships, put them in the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # The flag of ship right moving
        self.moving_rights = False
        self.moving_left = False



    def update(self):
        ''' move the ship by moving_rights flag'''
        if self.moving_rights and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
        ''' Draws the ship at the specified location'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        ''' Let the ship on the center bottom of screen '''

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
