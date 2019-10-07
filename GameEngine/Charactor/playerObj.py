import pygame
class playerObj:
    def __init__(self,surface, color):
        self.surface = surface
        self.color = color
        self.rectObj = pygame.rect.Rect(5, 550, 50, 50)
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rectObj)

    def up(self):
        self.rectObj[1] -= 10

    def down(self):
        self.rectObj[1] += 10
