import pygame
class ground:
    def __init__(self,surface, color):
        self.surface = surface
        self.groundRect = pygame.rect.Rect(0, 600, 1000, 10)
        self.color = color
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.groundRect)
