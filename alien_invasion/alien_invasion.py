# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: alien_invasion.py
# @Date: 2021-12-25 14:54:11
# @Last Modified by: franc
# @Last Modified time: 2021-12-26 00:06:43
# @Project: alien_invasion
# @Use: alien invasion main loop function, display window , ship and bullets.

import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    '''The class that manage game resources and behavior '''

    def __init__(self):
        '''Initialize the game and create the game resources '''
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Create an instance to count game information
        self.stats = GameStats(self)

        self.ship = Ship(self)

        # create the bullet group
        self.bullets = pygame.sprite.Group()

        # create the alien group
        self.aliens = pygame.sprite.Group()

        # Set the background color
        self.bg_color = (230, 230, 230)

        self._create_fleet()

    def _create_alien(self, alien_number, row_number):
        ''' create a new aline and add the aliens'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        ''' create the group of aliens '''

        # get the number of alien in the first line
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # Calculate how many rows of aliens  can fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def __update_ship_info(self):
        self.ship.screen = self.screen
        self.ship.settings = self.settings
        self.ship.screen_rect = self.screen.get_rect()
        self.ship.rect.midbottom = self.ship.screen_rect.midbottom
        self.ship.x = float(self.ship.rect.x)

    def _full_screen(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.__update_ship_info()

    def _defaut_screen(self):
        self.settings.screen_width = 600
        self.settings.screen_height = 400
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.__update_ship_info()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self, event):
        ''' key down event '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_rights = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_a:
            self._full_screen()
        elif event.key == pygame.K_ESCAPE:
            self._defaut_screen()

    def _check_keyup_events(self, event):
        ''' key up event '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_rights = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        ''' Monitor the events of keybord and mouse '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        ''' update the screen info'''
        # re-draw the screen by colors
        self.screen.fill(self.settings.bg_color)

        # draw the ship in screen
        self.ship.blitme()

        # draw the bullets in screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw the aliens in screen
        self.aliens.draw(self.screen)

        # Makes the recently drawn screen visible
        pygame.display.flip()

    def _check_bullet_alien_collisions(self):
        ''' Responding to the collisions of bullet and alien, delete them '''
        collisions = pygame.sprite.groupcollide(self.bullets,
                                        self.aliens, True, True)

        # create some new aliens when alien are empty
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _update_bullets(self):

        # update the bullets position
        self.bullets.update()

        # delete the dismiss bulletss
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()



    def _change_alien_direction(self):
        ''' Move the entire group of aliens down and change their direction '''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1

    def _check_aliens_edges(self):
        '''Do somethins when some aliens on the edges of screen'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_alien_direction()
                break

    def _ship_hit(self):
        ''' the action of collision between ship and alien '''

        # set the ship left is one
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
        else:
            self.stats.game_active = False

        # clear the left of aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # create some new aliens and put the ship into bottom of screen
        self._create_fleet()
        self.ship.center_ship()

        # sleep
        sleep(0.5)


    def _check_aliens_bottom(self):
        ''' check if any alien on the bottom of screen or not '''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _update_aliens(self):
        '''
        check if some aliens is on the edges of screen and update all aliens
        position
        '''
        self._check_aliens_edges()

        #check the collisions of ship and aliens
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        # check if any alien on the bottom of screen or not
        self._check_aliens_bottom()

        self.aliens.update()



    def run_game(self):
        '''start main loop of the game '''
        while True:
            # check the key event for user
            self._check_events()

            # update the game status when game_active is True
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            # update the screen
            self._update_screen()


if __name__ == '__main__':
    # Create a game instance and run it
    ai = AlienInvasion()
    ai.run_game()
