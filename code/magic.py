import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player):
        """
        Initialize the MagicPlayer.

        Args:
            animation_player (AnimationPlayer): Instance of AnimationPlayer for creating particles.
        """
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('../audio/heal.wav'),
            'flame': pygame.mixer.Sound('../audio/Fire.wav')
        }

    def heal(self, player, strength, cost, groups):
        """
        Perform healing magic.

        Args:
            player (Player): The player object to be healed.
            strength (int): The amount of health to be restored.
            cost (int): The energy cost of the healing.
            groups (list): List of sprite groups to add particles to.

        """
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center, groups)

    def flame(self, player, cost, groups):
        """
        Perform flame magic.

        Args:
            player (Player): The player object casting the flame.
            cost (int): The energy cost of the flame.
            groups (list): List of sprite groups to add particles to.

        """
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()

            # Determine flame direction based on player status
            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            else:
                direction = pygame.math.Vector2(0, 1)

            # Create flame particles along the direction
            for i in range(1, 6):  # Adjust the range for desired length of flame
                if direction.x:  # Horizontal flame
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)
                else:  # Vertical flame
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)

