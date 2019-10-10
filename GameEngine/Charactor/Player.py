import pygame
import GameEngine.Charactor.playerObj as Charactor
import GameEngine.Charactor.projectile as projectile
class player:
    def __init__(self, surface, color, ground):
        self.surface = surface
        self.Player = Charactor.playerObj(self.surface, color)
        self.ground = ground
        self.jumpOrnot = False
        self.jumpV = False
        self.FlytimeCounter = 0
        self.FlytimeMax = 20
        self.MaxJumpHeight = 300
        self.key = pygame.key.get_pressed()
        self.bullet = projectile.bullet(self.surface, self.Player)
    def shoot(self):
        self.bullet.isActive = True
    def jump(self):
        y = self.Player.rectObj[1]

        if y >= self.MaxJumpHeight and not self.jumpV:
            self.Player.up(int((y - 1000)**2 / 20000))

        elif y <= self.MaxJumpHeight and self.FlytimeCounter < self.FlytimeMax:
            if self.key[pygame.K_SPACE]:
                self.FlytimeCounter += 1
                if y > 275:
                    self.Player.up(30)
            else:
                self.FlytimeCounter = self.FlytimeMax

        elif not self.Player.rectObj.colliderect(self.ground.groundRect) and self.FlytimeCounter >= self.FlytimeMax:
            if self.Player.rectObj[1] < 497:
                self.Player.down(10)
            else:
                self.Player.down(1)
            self.jumpV = True

        else:
            self.jumpV = False
            self.jumpOrnot = False
            self.FlytimeCounter = 0

    def jumpChecks(self):
        if self.key[pygame.K_SPACE] and not self.jumpOrnot:
            self.jumpOrnot = True

        if self.jumpOrnot:

            self.jump()

    def shootChecks(self):
        if self.key[pygame.K_e]:
            self.shoot()

    def checks(self):
        self.key = pygame.key.get_pressed()
        self.jumpChecks()
        self.shootChecks()

    def update(self):
        self.checks()
        self.Player.draw()
        self.bullet.update(self.Player)
