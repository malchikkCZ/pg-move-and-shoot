import math
import pygame

from settings import *


class Enemy:

    def __init__(self, game, pos_x, pos_y, speed=ENEMY_SPEED):
        self.game = game
        self.player = self.game.player
        self.x = pos_x
        self.y = pos_y
        self.angle = ENEMY_ANGLE
        self.speed = speed
        self.size = ENEMY_SIZE
        self.killed = False

    def update(self):
        self.update_angle()
        self.move()

    def draw(self):
        # pygame.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 
        #     (self.x * 100 + WIDTH * math.cos(self.angle), 
        #      self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'grey', (self.x * 100, self.y * 100), self.size)

    def update_angle(self):
        dx = self.player.x - self.x
        dy = self.player.y - self.y
        self.angle = math.atan2(dy, dx)

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        velocity = pygame.math.Vector2()

        velocity.x += cos_a
        velocity.y += sin_a

        if velocity.magnitude() != 0:
            velocity = velocity.normalize()

        self.x += velocity.x * self.speed * self.game.delta_time
        self.y += velocity.y * self.speed * self.game.delta_time
