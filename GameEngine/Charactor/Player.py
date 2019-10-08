import pygame
import GameEngine.Charactor.playerObj as Charactor

class player:
    def __init__(self, surface, color, ground):
        self.surface = surface
        self.Player = Charactor.playerObj(self.surface, color)
        self.ground = ground
        self.jumpOrnot = False
        self.jumpV = False
        self.FlytimeCounter = 0
        self.FlytimeMax = 25
        self.MaxJumpHeight = 300
    def jump(self):
        y = self.Player.rectObj[1]
        key = pygame.key.get_pressed()

        if y >= self.MaxJumpHeight and not self.jumpV:
            self.Player.up(15)

        elif y <= self.MaxJumpHeight and self.FlytimeCounter < self.FlytimeMax:
            if key[pygame.K_SPACE]:
                self.FlytimeCounter += 1
                if y > 275:
                    self.Player.up(15)
            else:
                self.FlytimeCounter = self.FlytimeMax

        elif not self.Player.rectObj.colliderect(self.ground.groundRect) and self.FlytimeCounter >= self.FlytimeMax:
            self.jumpV = True
            self.Player.down(8)
        else:
            self.jumpV = False
            self.jumpOrnot = False
            self.FlytimeCounter = 0
    def jumpChecks(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jumpOrnot:
            self.jumpOrnot = True

        if self.jumpOrnot:

            self.jump()

    def checks(self):
        self.jumpChecks()

    def update(self):
        self.checks()
        self.Player.draw()
