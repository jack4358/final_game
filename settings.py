class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_speed = 1.0
        self.ship_up_speed = -0.3

        # moon settings
        self.moon_speed = 0.5
        self.moon_direction = 1

        # Meteor settings
        self.meteor_speed = 0.7
        self.meteor_direction = 1

        # UFO settings
        self.ufo_speed = 0.6
        self.ufo_up_speed = -0.6
        self.ufo_down_speed = 0.6
