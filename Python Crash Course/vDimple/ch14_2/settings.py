# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:37:46 2021

@author: dimpl
"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed settings
        self.ship_speed = 1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 30
        self.bullet_height = 55
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.1
        self.alien_width = 100
        self.alien_height = 65
        self.alien_color = (0, 0, 0)

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
