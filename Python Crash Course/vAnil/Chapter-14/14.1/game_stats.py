# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:01:15 2021

@author: ANIL
"""

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
    
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit