# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:50:23 2021

@author: ANIL
"""

class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (199, 21, 123)
        self.bullets_allowed = 3