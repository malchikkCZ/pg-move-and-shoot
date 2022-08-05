import pygame
import random
import sys

from settings import *
from source import Player, Crosshair, Enemy

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(GAME_RES)
        self.clock = pygame.time.Clock()

        self.bullets = []
        self.enemies = []
        self.crosshair = Crosshair(self)
        self.player = Player(self)
        self.kills = 0

        self.SPAWN_EVENT = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWN_EVENT, 500)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.SPAWN_EVENT:
                speed = random.randint(3, 9) / (10000 - self.kills)
                spawn_x, spawn_y = random.choice(SPAWN_AREA)
                self.enemies.append(Enemy(self, spawn_x, spawn_y, speed))

            self.player.fire_event(event)

    def update(self):
        self.delta_time = self.clock.tick(GAME_FPS)
        for bullet in self.bullets:
            bullet.update()
        self.crosshair.update()
        self.player.update()
        for enemy in self.enemies:
                enemy.update()

        self.bullets = [bullet for bullet in self.bullets if not bullet.killed]
        self.enemies = [enemy for enemy in self.enemies if not enemy.killed]

        pygame.display.flip()
        pygame.display.set_caption(f'KILLS: {self.kills} | FPS: {self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        for bullet in self.bullets:
            bullet.draw()
        self.crosshair.draw()
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
