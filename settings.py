class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_speed = 1.5
        self.ship_up_speed = -0.8

        # moon settings
        self.moon_speed = 0.5
        self.moon_direction = 1

        # Meteor settings
        self.meteor_speed = 0.9
        self.meteor_direction = 1

        # UFO settings
        self.ufo_speed = 0.3
        self.ufo_direction = 1