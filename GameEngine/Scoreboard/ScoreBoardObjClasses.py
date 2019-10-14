import pygame
class Score:
    def __init__(self, surface, font):
        self.value = 0
        self.surface = surface
        self.font = font

    def add(self, amt=1):
        self.value += amt

    def remove(self, amt=1):
        self.value -= amt

    def update(self):
        score = self.font.render(("Score: " + str(self.value)), True, (255,255,0))
        self.surface.blit(score, (0, 0))

class PlayerEnergy:
    def __init__(self,surface, font):
        self.value = 0
        self.font = font
        self.holdValue = 0
        self.surface = surface
    def add(self, amt=1):
        self.value += 1

    def remove(self, amt=1):
        self.value -= 1

    def update(self):
        self.holdValue += 0.07
        self.value = int(self.holdValue)
        Energy = self.font.render(("Energy: " + str(self.value)), True, (255,255,0))
        self.surface.blit(Energy, (0, 20))
