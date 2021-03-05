# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:32:14 2021

@author: dimpl
"""
import pygame


class GameCharacter:
    """Defining characters of the game."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings_instance = ai_game.ai_settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("ship_right.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement Flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Update the ship's x value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings_instance.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings_instance.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw character image at it's current location."""
        self.screen.blit(self.image, self.rect)
