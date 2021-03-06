# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:01:58 2021

@author: dimpl
"""

import sys
import pygame
from game_character import GameCharacter
from settings import Settings
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        # self.bg_color = (0, 0, 255)
        self.settings.bg_color = (230, 230, 230)
        self.game_character_instance = GameCharacter(self)

        self.bullets = pygame.sprite.Group()
        # self.aliens = pygame.sprite.Group()
        # self._create_fleet()
        self.alien = Alien(self)

        # Make the Play button.
        self.play_button = Button(self, "Play", "center")
        self.you_won_button = Button(self, "You Won", "center")
        self.button_flag = "play"

        self.difficulty_level = "easy"
        self.difficulty_level = "medium"
        self.difficulty_level = "hard"

        self.easy_button = Button(self, "Easy", "top_left")
        self.medium_button = Button(self, "Medium", "top_center")
        self.hard_button = Button(self, "Hard", "top_right")

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.game_character_instance.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.game_character_instance.moving_left = True
        elif event.key == pygame.K_UP:
            self.game_character_instance.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.game_character_instance.moving_down = True
        elif event.key == pygame.K_p:
            button_clicked = True
            self._start_playing(button_clicked)
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.game_character_instance.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.game_character_instance.moving_left = False
        elif event.key == pygame.K_UP:
            self.game_character_instance.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.game_character_instance.moving_down = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.play_button.rect.collidepoint(mouse_pos):
                    button_clicked = self.play_button.rect.collidepoint(
                        mouse_pos)
                self._start_playing(button_clicked)

    def _start_playing(self, button_clicked):
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.settings.misses = 0

            if self.button_flag == "you_won":
                self.settings.increase_speed()
            elif self.button_flag == "play":
                self.settings.initialize_dynamic_settings()

            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets.
            # self.aliens.empty()

            self.bullets.empty()
            # Create a new fleet and center the ship.
            # self._create_fleet()
            self.game_character_instance.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """"Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.screen_rect = self.screen.get_rect()

        # Update bullet positions.
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self.settings.misses += 1

        if self.settings.misses >= 3:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.button_flag = "play"

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            # Get rid of any remaining aliens and bullets.
            # self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.game_character_instance.center_ship()
            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        # for alien in self.aliens.sprites():
        if self.alien.check_edges():
            self._change_fleet_direction()

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        # for alien in self.aliens.sprites():
        # alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self.alien.update()
        self._check_fleet_edges()

    def _update_screen(self):
        # Redraw the screen through each pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.game_character_instance.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.alien.draw_alien()

        # Draw the play button if the game is inactive.

        if not self.stats.game_active:
            if self.button_flag == "play":
                self.play_button.draw_button()
            elif self.button_flag == "you_won":
                self.you_won_button.draw_button()

            # self.easy_button.draw_button()
            # self.medium_button.draw_button()
            # self.hard_button.draw_button()

        for bullet in self.bullets.copy():
            if bullet.rect.colliderect(self.alien.rect):
                self.stats.game_active = False
                self.you_won_button.draw_button()
                pygame.mouse.set_visible(True)
                self.button_flag = "you_won"

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Watch for Keyboard and Mouse events.
            self._check_events()

            if self.stats.game_active:
                self.game_character_instance.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
