import GameEngine.Obsticales.groundObj as groundObj
import pygame
class groundObstacles:
    def __init__(self, surface, color, player):
        self.playerRect = player.Player.rectObj
        self.surface = surface
        self.color = color
        self.createObj()
    def createObj(self):
        self.groundObstacle0 = groundObj.Obsticales(self.surface, self.color)
        self.groundObstacle1 = groundObj.Obsticales(self.surface, self.color, 1050)
        self.groundObstacle2 = groundObj.Obsticales(self.surface, self.color, 1300)
        self.groundObstacle3 = groundObj.Obsticales(self.surface, self.color, 1350)
        self.groundObstacle4 = groundObj.Obsticales(self.surface, self.color, 1400)

    def GROUP_PlayerCollisionCheck(self):
        self.PlayerCollisionCheck(self.groundObstacle0)
        self.PlayerCollisionCheck(self.groundObstacle1)
        self.PlayerCollisionCheck(self.groundObstacle2)
        self.PlayerCollisionCheck(self.groundObstacle3)
        self.PlayerCollisionCheck(self.groundObstacle4)


    def PlayerCollisionCheck(self, groundObstacleObj):
        if groundObstacleObj.rectObj.colliderect(self.playerRect):
            print("cool")

    def draw(self):
        self.GROUP_PlayerCollisionCheck()
        self.groundObstacle0.update()
        self.groundObstacle1.update()
        self.groundObstacle2.update()
        self.groundObstacle3.update()
        self.groundObstacle4.update()
