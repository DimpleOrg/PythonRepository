# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:37:46 2021

@author: dimpl
"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed settings
        # self.ship_speed = 1
        self.ship_limit = 3

        # Bullet settings
        # self.bullet_speed = 1.1
        self.bullet_width = 30
        self.bullet_height = 200
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
        self.misses = 0

        # Alien settings
        # self.alien_speed = 1.1
        self.alien_width = 100
        self.alien_height = 65
        self.alien_color = (0, 0, 0)

        # fleet_direction of 1 represents right; -1 represents left.
        # self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def initialize_easy_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.1
        self.alien_speed = 1.1

    def initialize_medium_settings(self):
        self.ship_speed = 2.5
        self.bullet_speed = 2.1
        self.alien_speed = 2.1

    def initialize_hard_settings(self):
        self.ship_speed = 2.5
        self.bullet_speed = 2.1
        self.alien_speed = 2.1
