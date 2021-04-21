# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:45:29 2021

@author: ANIL
"""
import pygame

class Ship:
    """Aclasstomanagetheship."""
    def __init__(self,ai_game):
        """Initializetheshipandsetitsstartingposition."""
        self.screen=ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        #Loadtheshipimageandgetitsrect.
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        #Starteachnewshipatthebottomcenterofthescreen.
        self.x = float(self.rect.x)
        self.rect.midbottom=self.screen_rect.midbottom
        
        self.y = float(self.rect.y)
        
        # self.x = self.screen_rect.right/2
        # self.y = self.screen_rect.bottom/2
        # self.x = self.screen_rect.centerx - self.rect.width/2
        # self.y = self.screen_rect.centery - self.rect.height/2
        
        self.x = self.screen_rect.right/2
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        """Drawtheshipatitscurrentlocation."""
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        if self.moving_up and self.rect.top >0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            
            
            
        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y