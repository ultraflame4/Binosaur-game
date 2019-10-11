import pygame
import GameEngine.mainGuiclasses as classes
import GameEngine.Charactor.Player as CharactorClass
import GameEngine.Obsticales as ObsticalClasses
import GameEngine.Scoreboard.MainScoreboard as scoreBoard
class mainGui:
    def __init__(self,surface,theme):
        self.surface = surface
        self.theme = theme
        self.createObj()
    def createObj(self):
        self.ground = classes.ground(self.surface, (102, 51, 0))
        self.scoreBoard = scoreBoard.Scoreboard(self.surface)
        self.Player = CharactorClass.player(self.surface, (50,50,50), self.ground, self.scoreBoard)
        self.GroundObsticals = ObsticalClasses.ground.groundObstacles(self.surface, (50, 100, 0), self.Player, self.scoreBoard)
    def update(self):
        self.surface.fill((0,0,0))
        self.scoreBoard.update()
        self.Player.update()
        self.ground.draw()
        self.GroundObsticals.draw()
