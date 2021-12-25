class Settings:
    ''' storage the all settins for Alien Invasion game '''

    def __init__(self):
        ''' init settings of the game '''
        # screen setting
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)
        # self.bg_color = (0,0,250)

        # the speed of ship
        self.ship_speed = 0.3

        # the color of bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        #limit the number of bullet
        self.bullet_allowed = 3

