import pygame
import GameEngine.mainGuiclasses as classes
class mainGui:
    def __init__(self,surface,theme):
        self.surface = surface
        self.theme = theme
        self.createObj()
    def createObj(self):
        self.ground = classes.ground(self.surface, self.theme)

    def update(self):
        self.surface.fill((255,255,255))
        self.ground.draw()
