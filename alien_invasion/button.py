##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: button.py
# @Date: 2021-12-26 20:21:28
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 20:40:10
# @Project: alien_invasion
# @Use: describe a play button for the game

import pygame.font

class Button():
    """docstring for Button"""
    def __init__(self, ai_game, msg):
        ''' Initialize the property of button '''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set the size of button and other proopers
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create the rect of button and put it into center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Create the text of button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        ''' Render 'msg' as an image and put it into center of button '''
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        ''' display the button '''

        # Draw a button filled with color, and then draw the text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)









