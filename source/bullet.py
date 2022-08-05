import math
import pygame

from settings import *


class Bullet():

    def __init__(self, game):
        self.game = game
        self.player = self.game.player
        self.x, self.y = self.player.pos
        self.angle = self.player.angle
        self.speed = BULLET_SPEED
        self.size = BULLET_SIZE
        self.killed = False

    def update(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        velocity = pygame.math.Vector2()

        velocity.x += cos_a
        velocity.y += sin_a

        if velocity.magnitude() != 0:
            velocity = velocity.normalize()

        self.x += velocity.x * self.speed * self.game.delta_time
        self.y += velocity.y * self.speed * self.game.delta_time

        self.check_collision()

    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', (self.x * 100, self.y * 100), self.size)

    def check_collision(self):
        if self.x < 0 or self.x > WIDTH / 100 or self.y < 0 or self.y > HEIGHT / 100:
            self.killed = True
            return
        for enemy in self.game.enemies:
            if enemy.x - enemy.size / 100 < self.x < enemy.x + enemy.size / 100 and enemy.y - enemy.size / 100 < self.y < enemy.y + enemy.size / 100:
                self.killed = True
                enemy.killed = True
                self.game.kills += 1
                break
