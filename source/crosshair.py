import pygame


class Crosshair:

    def __init__(self, game):
        self.game = game
        self.x, self.y = 3, 3

        self.rect = pygame.Rect(self.x, self.y, 1, 1)
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.x = self.rect.centerx / 100
        self.y = self.rect.centery / 100

    def draw(self):
        pass

    @property
    def pos(self):
        return self.x, self.y
