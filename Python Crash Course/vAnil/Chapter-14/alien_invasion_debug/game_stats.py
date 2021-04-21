# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:01:15 2021

@author: ANIL
"""
class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = 3 #self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
