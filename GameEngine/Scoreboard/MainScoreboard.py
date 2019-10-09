import GameEngine.Scoreboard.ScoreBoardObjClasses as classes
import pygame
class Scoreboard:
    def __init__(self, surface):
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.MainSurface = surface
        self.playerCollisions = classes.PlayerObjCollisionBoard(self.MainSurface, self.font)

    def update(self):
        self.playerCollisions.update()
