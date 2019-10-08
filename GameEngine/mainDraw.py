import pygame
import GameEngine.mainGuiclasses as classes
import GameEngine.Charactor.Player as CharactorClass
import GameEngine.Obsticales as ObsticalClasses
class mainGui:
    def __init__(self,surface,theme):
        self.surface = surface
        self.theme = theme
        self.createObj()
    def createObj(self):
        self.ground = classes.ground(self.surface, self.theme)
        self.Player = CharactorClass.player(self.surface, self.theme, self.ground)
        self.GroundObsticals = ObsticalClasses.ground.groundObstacles(self.surface, (0, 255, 0), self.Player)
    def update(self):
        self.surface.fill((255,255,255))
        self.ground.draw()
        self.Player.update()
        self.GroundObsticals.draw()
