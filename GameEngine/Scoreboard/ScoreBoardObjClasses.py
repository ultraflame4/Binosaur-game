import pygame
class PlayerObjCollisionBoard:
    def __init__(self, surface, font):
        self.collisions = 0
        self.surface = surface
        self.font = font
    def add(self, amt=1):
        self.collisions += 1
        print(amt)
    def remove(self, amt=1):
        self.collisions -= 1

    def update(self):
        score = self.font.render(("Score: " + str(self.collisions)), True, (255,255,0))
        self.surface.blit(score, (0, 0))
