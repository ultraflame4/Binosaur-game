import GameEngine.Obsticales.groundObj as groundObj
import pygame
class groundObstacles:
    def __init__(self, surface, color, player, scoreBoard):
        self.playerRect = player.Player.rectObj
        self.PlayerBullet = player.bullet
        self.surface = surface
        self.color = color
        self.Scoreboard = scoreBoard
        self.createObj()
    def createObj(self):
        self.groundObstacle0 = groundObj.Obsticales(self.surface, self.color, self.playerRect)
        self.groundObstacle1 = groundObj.Obsticales(self.surface, self.color, self.playerRect, 1050)
        self.groundObstacle2 = groundObj.Obsticales(self.surface, self.color, self.playerRect, 1300)
        self.groundObstacle3 = groundObj.Obsticales(self.surface, self.color, self.playerRect, 1350)
        self.groundObstacle4 = groundObj.Obsticales(self.surface, self.color, self.playerRect, 1400)

    def GROUP_PlayerCollisionCheck(self):
        self.PlayerCollisionCheck(self.groundObstacle0)
        self.PlayerCollisionCheck(self.groundObstacle1)
        self.PlayerCollisionCheck(self.groundObstacle2)
        self.PlayerCollisionCheck(self.groundObstacle3)
        self.PlayerCollisionCheck(self.groundObstacle4)

    def GROUP_PlayerCollisionSpeedChange(self, amt=1):
        self.groundObstacle0.speed += amt
        self.groundObstacle1.speed += amt
        self.groundObstacle2.speed += amt
        self.groundObstacle3.speed += amt
        self.groundObstacle4.speed += amt

    def PlayerCollisionCheck(self, groundObstacleObj):
        if groundObstacleObj.rectObj.colliderect(self.playerRect):
            self.Scoreboard.playerCollisions.remove(5)
            self.GROUP_PlayerCollisionSpeedChange(-3)

        elif groundObstacleObj.jumpOver():
            self.Scoreboard.playerCollisions.add(10)
            if groundObstacleObj.speed < 5:
                self.GROUP_PlayerCollisionSpeedChange(0.5)
            else:
                self.GROUP_PlayerCollisionSpeedChange(0.01)

        if groundObstacleObj.bulletCollisionCheck(self.PlayerBullet, self.Scoreboard):
            if groundObstacleObj.speed < 5:
                self.GROUP_PlayerCollisionSpeedChange(0.5)
            else:
                self.GROUP_PlayerCollisionSpeedChange(0.01)



    def draw(self):
        self.GROUP_PlayerCollisionCheck()
        self.groundObstacle0.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle1.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle2.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle3.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle4.update(self.PlayerBullet, self.Scoreboard)
