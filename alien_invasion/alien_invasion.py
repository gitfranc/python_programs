import sys
import pygame

from settings import Settings
from ship import Ship
from airplane import Airplane
from bullet import Bullet


class AlienInvasion:
    '''The class that manage game resources and behavior '''

    def __init__(self):
        '''Initialize the game and create the game resources '''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # self.airplane = Airplane(self)

        # create the bullet group
        self.bullets = pygame.sprite.Group()

        # Set the background color
        self.bg_color = (230, 230, 230)

    def __update_ship_info(self):
        self.ship.screen = self.screen
        self.ship.settings = self.settings
        self.ship.screen_rect = self.screen.get_rect()
        self.ship.rect.midbottom = self.ship.screen_rect.midbottom
        self.ship.x = float(self.ship.rect.x)

    def _full_screen(self):
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
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


    def _check_keyup_events(self,event):
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

        # self.airplane.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Makes the recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):

        # update the bullets position
        self.bullets.update()

        # delete the dismiss bulletss
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def run_game(self):
        '''start main loop of the game '''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    # Create a game instance and run it
    ai = AlienInvasion()
    ai.run_game()
