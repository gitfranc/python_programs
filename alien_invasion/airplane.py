import pygame


class Airplane:
    ''' The class of manager the ship '''

    def __init__(self,ai_game):
        ''' init the airplane and position '''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image of the spacecraft and get its enclosing rectangle
        self.image = pygame.image.load("images/feiji.bmp")
        self.rect = self.image.get_rect()

        # For new airplane, put them in the bottom center of the screen
        self.rect.centery = self.screen_rect.centery


    def blitme(self):
        ''' Draws the airplane at the specified location'''
        self.screen.blit(self.image,self.rect)
