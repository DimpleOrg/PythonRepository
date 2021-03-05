# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:28:24 2021

@author: dimpl
"""
import pygame


class GameCharacter:
    """A class to manage game character"""

    def __init__(self, ai_game):
        """initialize the character and set its starting position"""

        # we assign the screen
        # to an attribute of Ship, so we can access it easily in all the methods in this
        # class.
        self.screen = ai_game.screen
        self.settings_instance = ai_game.settings
        # we access the screen’s rect attribute using the get_rect() method
        # and assign it to self.screen_rect. Doing so allows us to place the ship in the
        # correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character image and get its rect.

        # This function returns a surface representing the
        # ship, which we assign to self.image
        self.image = pygame.image.load("ship.bmp")

        # When the image is loaded, we call
        # get_rect() to access the ship surface’s rect attribute so we can later use it
        # to place the ship.
        self.rect = self.image.get_rect()

        # self.rect.height = 650

        # Start the character at the bottom left corner of the screen.
        # Pygame uses these rect attributes to position the ship
        # image so it’s centered horizontally and aligned with the bottom of the
        # screen.
        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement Flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        # Update the ship's x value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings_instance.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings_instance.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings_instance.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings_instance.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw character image at it's current location."""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
