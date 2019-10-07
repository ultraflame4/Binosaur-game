import pygame
class Obsticales:
    def __init__(self,surface, color):
        self.surface = surface
        self.theme = color
        self.rectObj = pygame.rect.Rect(700, 550, 20, 50)

    def move(self):
        self.rectObj.move_ip(-1, 0)

    def update(self):
        pygame.draw.rect(self.surface, self.theme, self.rectObj)
