# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 06:58:30 2021

@author: dimpl
"""

import pygame
import sys


class NewGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 300))

    def check_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(event.key)


if __name__ == '__main__':
    ng = NewGame()
    ng.check_events()
