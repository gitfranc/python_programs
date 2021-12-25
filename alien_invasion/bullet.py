##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: bullet.py
# @Date: 2021-12-25 14:54:11
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 00:11:56
# @Project: alien_invasion
# @Use: describe the bullet for the game

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """docstring for Bullet"Sprite def __init__(self, arg):
        super(Bullet,Sprite.__init__()
        self.arg = arg"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # set the rect of bullet from point(0,0), set the right position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

