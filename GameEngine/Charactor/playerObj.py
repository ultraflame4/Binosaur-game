import pygame
class playerObj:
    def __init__(self,surface, color):
        self.surface = surface
        self.color = color
        self.rectObj = pygame.rect.Rect(50, 500, 20, 50)
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rectObj)

    def up(self, amt=10):
        self.rectObj[1] -= amt

    def down(self, amt=10):
        self.rectObj[1] += amt
