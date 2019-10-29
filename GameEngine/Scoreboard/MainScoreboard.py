import GameEngine.Scoreboard.ScoreBoardObjClasses as classes
import pygame
class Scoreboard:
    def __init__(self, surface):
        self.font = pygame.font.SysFont('Arial', 20)
        self.MainSurface = surface
        self.Score = classes.Score(self.MainSurface, self.font)
        self.Energy = classes.PlayerEnergy(self.MainSurface, self.font)
    def update(self):
        self.Score.update()
        self.Energy.update()
