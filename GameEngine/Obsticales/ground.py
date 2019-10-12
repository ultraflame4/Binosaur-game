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
            if self.Scoreboard.Energy.value > 0:
                self.Scoreboard.Energy.remove(50)

            if self.Scoreboard.Score.value > 0:
                self.Scoreboard.Score.remove(10)
            else:
                self.Scoreboard.Score.value = 0

            self.GROUP_PlayerCollisionSpeedChange(-1)

        elif groundObstacleObj.jumpOver():
            self.Scoreboard.Score.add(5)


    def GROUP_bulletCollisioncheck(self):
        self.bulletCollisionCheck(self.groundObstacle0)
        self.bulletCollisionCheck(self.groundObstacle1)
        self.bulletCollisionCheck(self.groundObstacle2)
        self.bulletCollisionCheck(self.groundObstacle3)
        self.bulletCollisionCheck(self.groundObstacle4)

    def bulletCollisionCheck(self, obstacle):
        if obstacle.rectObj.colliderect(self.PlayerBullet.rect):
            print(str(self.PlayerBullet.isReady))
            self.PlayerBullet.isActive = False
            if self.PlayerBullet.isReady:
                obstacle.rectObj[0] = -12
            self.PlayerBullet.isReady = False
    def gameSpeedUpdate(self):
        self.GROUP_PlayerCollisionSpeedChange(0.003)
    def draw(self):
        self.gameSpeedUpdate()
        self.GROUP_bulletCollisioncheck()
        self.GROUP_PlayerCollisionCheck()
        self.groundObstacle0.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle1.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle2.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle3.update(self.PlayerBullet, self.Scoreboard)
        self.groundObstacle4.update(self.PlayerBullet, self.Scoreboard)
