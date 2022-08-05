import math
import pygame
import sys

from settings import *
from source.bullet import Bullet


class Player:

    def __init__(self, game):
        self.game = game
        self.crosshair = self.game.crosshair
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.speed = PLAYER_SPEED
        self.size = PLAYER_SIZE

    @property
    def pos(self):
        return self.x, self.y

    def update(self):
        self.move()
        self.update_angle()

        self.check_collision()

    def draw(self):
        pygame.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 
            (self.x * 100 + 50 * math.cos(self.angle), 
             self.y * 100 + 50 * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), self.size)

    def fire_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.game.bullets.append(Bullet(self.game))

    def update_angle(self):
        dx = self.crosshair.x - self.x
        dy = self.crosshair.y - self.y
        self.angle = math.atan2(dy, dx)

    def move(self):
        velocity = pygame.math.Vector2()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            velocity.y -= 1
        if keys[pygame.K_s]:
            velocity.y += 1
        if keys[pygame.K_a]:
            velocity.x -= 1
        if keys[pygame.K_d]:
            velocity.x += 1
        
        if velocity.magnitude() != 0:
            velocity = velocity.normalize()
        
        x = self.x + velocity.x * self.speed * self.game.delta_time
        y = self.y + velocity.y * self.speed * self.game.delta_time
        x, y = self.constrain_movement(x, y)

        self.x = x
        self.y = y

    def constrain_movement(self, x, y):
        x = min(max(x, self.size / 100), (WIDTH - self.size) / 100)
        y = min(max(y, self.size / 100), (HEIGHT - self.size) / 100)
        
        return x, y

    def check_collision(self):
        for enemy in self.game.enemies:
            if enemy.x - enemy.size / 100 < self.x < enemy.x + enemy.size / 100 and enemy.y - enemy.size / 100 < self.y < enemy.y + enemy.size / 100:
                print(f'You have been eaten. You killed {self.game.kills} enemies')
                pygame.quit()
                sys.exit()
